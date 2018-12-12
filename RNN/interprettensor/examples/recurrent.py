from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")
from RNN.interprettensor.modules.sequential import Sequential
from RNN.interprettensor.modules.linear import Linear
from RNN.interprettensor.modules.softmax import Softmax
from RNN.interprettensor.modules.relu import Relu
from RNN.interprettensor.modules.tanh import Tanh
from RNN.interprettensor.modules.convolution1d import Convolution1d
from RNN.interprettensor.modules.recurrent import Recurrent
from RNN.interprettensor.modules.avgpool import AvgPool
from RNN.interprettensor.modules.maxpool import MaxPool
from RNN.interprettensor.modules.utils import Utils, Summaries

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pandas as pd
os.environ["CUDA_VISIBLE_DEVICES"]="0"

flags = tf.flags
logging = tf.logging

# flags.DEFINE_integer("max_steps", 100000,'Number of steps to run trainer.')
# flags.DEFINE_integer("test_every", 1000,'Number of steps to run trainer.')
flags.DEFINE_integer("show_every", 100,'Number of steps to run trainer.')
# flags.DEFINE_float("learning_rate", 0.001,'Initial learning rate')
# flags.DEFINE_float("dropout", 0.7, 'Keep probability for training dropout.')

# flags.DEFINE_string("summaries_dir", 'quickdraw_logs1','Summaries directory')
# flags.DEFINE_boolean("save_model", False,'Save the trained model')
# flags.DEFINE_boolean("reload_model", True,'Restore the trained model')
# flags.DEFINE_string("checkpoint_dir", 'quickdraw_rnn_model','Checkpoint dir')
# flags.DEFINE_string("checkpoint_reload_dir", 'quickdraw_rnn_model_best','Checkpoint dir')
# flags.DEFINE_string("data_dir", 'quickdraw_data/','Directory for storing data')


flags.DEFINE_string("num_conv", "[48, 64, 96]",'Number of conv layers along with number of filters per layer.')
flags.DEFINE_string("conv_len", "[5, 5, 3]",'Length of the convolution filters.')
flags.DEFINE_integer("num_layers", 2,'Number of recurrent neural network layers.')
flags.DEFINE_integer("num_nodes", 128,'Number of node per recurrent network layer.')
# flags.DEFINE_integer("batch_size", 16,'Number of steps to run trainer.')
flags.DEFINE_integer("test_batch_size", 100,'Number of steps to run trainer.')
flags.DEFINE_boolean("batch_norm", False,'Whether to enable batch normalization or not.')

FLAGS = flags.FLAGS


import RNN.interprettensor.examples.quickdraw as quickdraw


def train(worker=None):
    FLAGS.test_every = 1000
    FLAGS.summaries_dir = 'RNN/interprettensor/examples/quickdraw_logs1'
    FLAGS.checkpoint_dir = 'RNN/interprettensor/examples/quickdraw_rnn_model'
    FLAGS.checkpoint_reload_dir = 'RNN/interprettensor/examples/quickdraw_rnn_model_best'
    FLAGS.data_dir = 'RNN/interprettensor/examples/quickdraw_data/'

    qd = quickdraw.Dataset(FLAGS.data_dir)

    def nn(l):
        return Sequential([Convolution1d(output_depth=48, input_depth=3, batch_size=FLAGS.batch_size,
                                         act='relu', kernel_size=5, stride_size=1, pad='SAME'),
                           Convolution1d(output_depth=64, input_depth=48, batch_size=FLAGS.batch_size,
                                         act='relu', kernel_size=5, stride_size=1, pad='SAME'),
                           Convolution1d(output_depth=96, input_depth=64, batch_size=FLAGS.batch_size,
                                         act='relu', kernel_size=3, stride_size=1, pad='SAME'),
                           Recurrent(num_layers=FLAGS.num_layers, num_nodes=FLAGS.num_nodes, direction='bidirectional',
                                     batch_size=FLAGS.batch_size, input_depth=96, var=True, lengths=l),
                           Linear(output_dim=qd.get_num_classes(), batch_size=FLAGS.batch_size,
                                  input_dim=FLAGS.num_nodes * 2)
                           ])

    X, l, y = qd.get_data(mode=tf.estimator.ModeKeys.TRAIN, batch_size=FLAGS.batch_size)
    X_, l_, y_ = qd.get_data(mode=tf.estimator.ModeKeys.EVAL, batch_size=FLAGS.test_batch_size)

    config = tf.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True
    with tf.Session() as sess:

        with tf.name_scope('input'):
            input_tensor = tf.placeholder(tf.float32, [None, None, 3])
            length_tensor = tf.placeholder(tf.int64, [None])
            label_tensor = tf.placeholder(tf.int64, [None])

        with tf.variable_scope('model'):
            net = nn(length_tensor)
            op = net.forward(input_tensor)
            trainer = net.fit(output=op, ground_truth=label_tensor, loss='sparse_softmax_crossentropy', optimizer='adam', opt_params=[FLAGS.learning_rate])

        with tf.name_scope('accuracy'):
            predictions = tf.argmax(op, axis=1)
            accuracy = tf.reduce_mean(tf.cast(tf.equal(predictions, label_tensor), tf.float32))
        tf.summary.scalar('accuracy', accuracy)

        merged = tf.summary.merge_all()
        train_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/train', sess.graph)
        test_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/test')

        print(tf.trainable_variables())

        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())

        mean_acc = 0
        utils = Utils(sess, FLAGS.checkpoint_reload_dir)
        if FLAGS.reload_model:
            utils.reload_model()
        for i in range(FLAGS.max_steps):
            if i % FLAGS.test_every == 0:  # test-set accuracy
                import timeit
                start = timeit.default_timer()
                inks, lengths, labels = sess.run([X_, l_, y_])
                summary, acc = sess.run([merged, accuracy],
                                        feed_dict={input_tensor: inks, length_tensor: lengths, label_tensor: labels})
                stop = timeit.default_timer()
                acc_msg = 'Error-rate at step %s: %f' % (i, 1 - acc)
                worker.train_msg.emit(acc_msg)  # send signal
                print(acc_msg)
                test_writer.add_summary(summary, i)
                print('Runtime: %f' % (stop - start))

                # save model if required
                if FLAGS.save_model:
                    utils.checkpoint_dir = FLAGS.checkpoint_dir
                    utils.save_model()
            inks, lengths, labels = sess.run([X, l, y])
            summary, _, acc = sess.run([merged, trainer.train, accuracy],
                                       feed_dict={input_tensor: inks, length_tensor: lengths, label_tensor: labels})
            train_writer.add_summary(summary, i)
            mean_acc += acc

            if i % FLAGS.show_every == 0:
                acc_msg = 'Error-rate at step %s: %f' % (i, 1 - (mean_acc/FLAGS.show_every))
                worker.train_msg.emit(acc_msg)  # send signal
                print(acc_msg)
                mean_acc = 0
            if i == FLAGS.max_steps-1:
                acc_msg = 'Error-rate at step %s: %f' % (i, 1 - acc)
                worker.train_msg.emit(acc_msg)  # send signal
                print(acc_msg)

        train_writer.close()
        test_writer.close()


def test(worker=None):
    FLAGS.test_every = 1000
    FLAGS.summaries_dir = 'RNN/interprettensor/examples/quickdraw_logs1'
    FLAGS.checkpoint_dir = 'RNN/interprettensor/examples/quickdraw_rnn_model'
    FLAGS.checkpoint_reload_dir = 'RNN/interprettensor/examples/quickdraw_rnn_model_best'
    FLAGS.data_dir = 'RNN/interprettensor/examples/quickdraw_data/'

    qd = quickdraw.Dataset(FLAGS.data_dir)

    def nn(l):
        return Sequential([Convolution1d(output_depth=48, input_depth=3, batch_size=FLAGS.batch_size,
                                         act='relu', kernel_size=5, stride_size=1, pad='SAME'),
                           Convolution1d(output_depth=64, input_depth=48, batch_size=FLAGS.batch_size,
                                         act='relu', kernel_size=5, stride_size=1, pad='SAME'),
                           Convolution1d(output_depth=96, input_depth=64, batch_size=FLAGS.batch_size,
                                         act='relu', kernel_size=3, stride_size=1, pad='SAME'),
                           Recurrent(num_layers=FLAGS.num_layers, num_nodes=FLAGS.num_nodes, direction='bidirectional',
                                     batch_size=FLAGS.batch_size, input_depth=96, var=True, lengths=l),
                           Linear(output_dim=qd.get_num_classes(), batch_size=FLAGS.batch_size,
                                  input_dim=FLAGS.num_nodes * 2)
                           ])

    X, l, y = qd.get_data(mode=tf.estimator.ModeKeys.PREDICT, batch_size=1)
    config = tf.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True
    with tf.Session() as sess:
        with tf.name_scope('input'):
            input_tensor = tf.placeholder(tf.float32, [None, None, 3])
            length_tensor = tf.placeholder(tf.int64, [None])
            label_tensor = tf.placeholder(tf.int64, [None])

        with tf.variable_scope('model'):
            net = nn(length_tensor)
            op = net.forward(input_tensor)

        with tf.name_scope('accuracy'):
            predictions = tf.argmax(op, axis=1)
            accuracy = tf.reduce_mean(tf.cast(tf.equal(predictions, label_tensor), tf.float32))

        utils = Utils(sess, FLAGS.checkpoint_reload_dir)
        utils.reload_model()

        classes = qd.get_classes()

        # for i in range(1000):
        from random import randint
        i = randint(1, 1000)
        import timeit
        start = timeit.default_timer()
        inks, lengths, labels = sess.run([X, l, y])
        prd_label, acc = sess.run([predictions, accuracy],
                                  feed_dict={input_tensor: inks, length_tensor: [lengths], label_tensor: [labels]})

        stop = timeit.default_timer()
        if acc:
            print('Correct')
        else:
            print('Wrong')
        print('Runtime: %f' % (stop - start))
        label = classes[prd_label[0]]
        gtlabel = classes[labels]
        strokes = np.where(inks[0, :, -1] == 1)

        list = [label, gtlabel]
        csv = pd.DataFrame(list)
        csv.to_csv('RNN/result/result.csv',header=True)

        for j in range(1, len(inks[0, :, 0])):
            inks[0, j, 0:2] = inks[0, j, 0:2] + inks[0, j-1, 0:2]
        start = 0
        # title = "%s (%s)" % (label[:-1], gtlabel[:-1])

        fig = plt.figure()
        plot = fig.add_subplot(111)
        for s in strokes[0]:
            plot.plot(-1*inks[0, start:s+1, 0], -1*inks[0, start:s+1, 1], '-')
            start = s+1
        # plt.title(title, fontsize=32)
        # plt.pause(2)
        fig.savefig('RNN/result/result.png')

        worker.test_msg.emit('end')
            # res = input('Run for another example ([y]/n): ')
            # if res == 'n':
            #     break

"""
def main(_):
    if tf.gfile.Exists(FLAGS.summaries_dir):
        tf.gfile.DeleteRecursively(FLAGS.summaries_dir)
    tf.gfile.MakeDirs(FLAGS.summaries_dir)
    with tf.Graph().as_default():
        train()
        # test()


if __name__ == '__main__':
    tf.app.run()
"""