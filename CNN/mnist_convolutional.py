from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")
from CNN.modules.sequential import Sequential
from CNN.modules.linear import Linear
from CNN.modules.softmax import Softmax
from CNN.modules.relu import Relu
from CNN.modules.tanh import Tanh
from CNN.modules.convolution import Convolution
from CNN.modules.avgpool import AvgPool
from CNN.modules.maxpool import MaxPool
from CNN.modules.activations import linear
from CNN.modules.utils import Utils, Summaries
import CNN.input_data
import tensorflow as tf
import numpy as np
import pdb
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


from Model import nn

flags = tf.flags
logging = tf.logging

flags.DEFINE_integer("max_steps", 10000,'Number of steps to run trainer.')
flags.DEFINE_integer("batch_size", 100,'Number of steps to run trainer.')
flags.DEFINE_integer("test_every", 500,'Number of steps to run trainer.')
flags.DEFINE_float("learning_rate", 0.001,'Initial learning rate')
flags.DEFINE_float("dropout", 0.7, 'Keep probability for training dropout.')
flags.DEFINE_string("data_dir", 'CNN/data','Directory for storing data')
flags.DEFINE_string("summaries_dir", 'CNN/logs','Summaries directory')
flags.DEFINE_boolean("save_model", True,'Save the trained model')
flags.DEFINE_boolean("reload_model", False,'Restore the trained model')
flags.DEFINE_string("checkpoint_dir", 'CNN/checkpoint','Checkpoint dir')
flags.DEFINE_string("checkpoint_reload_dir", 'CNN/checkpoint','Checkpoint dir')

FLAGS = flags.FLAGS

def feed_dict(mnist, train):
    if train:
        xs, ys = mnist.train.next_batch(FLAGS.batch_size)
        k = FLAGS.dropout
    else:
        xs, ys = mnist.test.next_batch(FLAGS.batch_size)
        k = 1.0
    return (2*xs)-1, ys, k


def train(tag, worker, checkpoint_dir=None, image_dir=None):
  # Import data
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
  config = tf.ConfigProto(allow_soft_placement = True)
  config.gpu_options.allow_growth = True
  with tf.Session(config=config) as sess:

    # Input placeholders
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 784], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, 10], name='y-input')
        phase = tf.placeholder(tf.bool, name='phase')
    
    with tf.variable_scope('model'):
        if tag=='test':
            FLAGS.batch_size=1
        net = nn(phase)
        inp = tf.pad(tf.reshape(x, [FLAGS.batch_size,28,28,1]), [[0,0],[2,2],[2,2],[0,0]])
        op = net.forward(inp)
        y = tf.squeeze(op)
        trainer = net.fit(output=y,ground_truth=y_,loss='softmax_crossentropy',optimizer='adam', opt_params=[FLAGS.learning_rate])
            
    with tf.name_scope('accuracy'):
        accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)), tf.float32))
    tf.summary.scalar('accuracy', accuracy)

    # Merge all the summaries and write them out to /tmp/mnist_logs (by default)
    merged = tf.summary.merge_all()
    train_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/train', sess.graph)
    test_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/test')

    tf.global_variables_initializer().run()
    
    utils = Utils(sess, FLAGS.checkpoint_reload_dir)
    ''' Reload from a list of numpy arrays '''
    if FLAGS.reload_model:
        tvars = tf.trainable_variables()
        npy_files = np.load('checkpoint/MNIST_model.npy', encoding='bytes')
        [sess.run(tv.assign(npy_files[tt])) for tt,tv in enumerate(tvars)]
        #utils.reload_model()


    if tag == 'train':
        for i in range(FLAGS.max_steps):
            d = feed_dict(mnist, True)
            inp = {x:d[0], y_: d[1], phase: False}
            summary, _ , acc, op= sess.run([merged, trainer.train,accuracy, y], feed_dict=inp)
            # save model if required
            print('Accuracy at step %s: %f' % (i, acc))
            # train_writer.add_summary(summary, i)
            acc_msg = 'Error-rate at step %s: %f' % (i, 1-acc)
            worker.train_msg.emit(acc_msg)  # send signal
            print(acc_msg)
            Utils.save_model(self=utils, epoch=(i + 1), dataset='MNIST')

    # Predict section
    if tag =='test':
        FLAGS.batch_size = 1
        FLAGS.checkpoint_reload_dir = checkpoint_dir
        image_dir = image_dir

        utils = Utils(sess, FLAGS.checkpoint_reload_dir)
        tvars = tf.trainable_variables()
        npy_files = np.load(FLAGS.checkpoint_reload_dir, encoding='bytes')
        [sess.run(tv.assign(npy_files[tt])) for tt, tv in enumerate(tvars)]
        utils.reload_model()

        d = io.imread(image_dir).astype('float32')
        d = d.reshape([1, 28 * 28])
        test_inp = {x: d, phase: False}
        # pdb.set_trace()

        import timeit
        start = timeit.default_timer()

        logit = sess.run([y], feed_dict=test_inp)
        logit = logit[0]

        pred = np.argmax(logit)
        stop = timeit.default_timer()
        print('Runtime: %f' % (stop - start))
        # test_writer.add_summary(summary, i)
        print(logit[0])
        prob_msg = '''
<Probability>
0 : %f
1 : %f
2 : %f
3 : %f
4 : %f
5 : %f
6 : %f
7 : %f
8 : %f
9 : %f\n
        '''%(logit[0], logit[1], logit[2], logit[3], logit[4], logit[5], logit[6], logit[7], logit[8], logit[9])
        pred_msg = 'Predict: %d'%(pred)
        worker.test_msg.emit([prob_msg,pred_msg])
        print(pred_msg)
        # pdb.set_trace()

    train_writer.close()
    test_writer.close()

def run(tag='train', worker=None, checkpoint_dir=None, image_dir=None):
    if tf.gfile.Exists(FLAGS.summaries_dir):
        tf.gfile.DeleteRecursively(FLAGS.summaries_dir)
    tf.gfile.MakeDirs(FLAGS.summaries_dir)
    train(tag, worker, checkpoint_dir, image_dir)

"""
#if __name__ == '__main__':
    tf.app.run()
"""