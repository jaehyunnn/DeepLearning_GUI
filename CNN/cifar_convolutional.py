
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

sys.path.append(".")
from CNN.modules.linear import Linear
from CNN.modules.softmax import Softmax
from CNN.modules.relu import Relu
from CNN.modules.tanh import Tanh
from CNN.modules.convolution import Convolution
from CNN.modules.avgpool import AvgPool
from CNN.modules.maxpool import MaxPool
from CNN.modules.utils import Utils, Summaries
import CNN.input_data

import tensorflow as tf
import numpy as np
import pdb
import scipy.io as sio
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


from Model import nn

flags = tf.flags
logging = tf.logging

"""
flags.DEFINE_integer("max_steps", 100000, 'Number of steps to run trainer.')
flags.DEFINE_integer("batch_size", 100, 'Number of steps to run trainer.')
flags.DEFINE_integer("test_every", 5, 'Number of steps to run trainer.')
flags.DEFINE_float("learning_rate", 0.005, 'Initial learning rate')
flags.DEFINE_string("data_dir", 'data', 'Directory for storing data')
flags.DEFINE_string("summaries_dir", 'logs', 'Summaries directory')
flags.DEFINE_boolean("save_model", True, 'Save the trained model')
flags.DEFINE_boolean("reload_model", False, 'Restore the trained model')
flags.DEFINE_string("checkpoint_dir", 'cifar_trained_model2', 'Checkpoint dir')
flags.DEFINE_string("checkpoint_reload_dir", 'cifar_trained_model2', 'Checkpoint dir')
flags.DEFINE_integer("Class", 10, 'Number of class.')
"""

FLAGS = flags.FLAGS

from tensorflow.keras.datasets.cifar10 import load_data

def next_batch(num, data, labels):
    '''
    Return a total of `num` random samples and labels. 
    '''
    idx = np.arange(0, len(data))
    np.random.shuffle(idx)
    idx = idx[:num]
    data_shuffle = [data[i] for i in idx]
    labels_shuffle = [labels[i] for i in idx]

    return np.asarray(data_shuffle), np.asarray(labels_shuffle)

def train(tag, worker, image_dir=None):
    FLAGS.max_steps = 100000
    FLAGS.reload_model= False

    # Import data
    config = tf.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True
    if tag == 'train':
        FLAGS.batch_size = 100
    elif tag == 'test':
        FLAGS.batch_size = 1
    with tf.Session(config=config) as sess:

        # with tf.Session() as sess:
        # Input placeholders
        with tf.name_scope('input'):
            x = tf.placeholder(tf.float32, shape=[None, 32, 32, 3])
            y_ = tf.placeholder(tf.float32, shape=[None, 10])
            phase = tf.placeholder(tf.bool, name='phase')

        with tf.variable_scope('model'):
            net = nn(phase)
            inp = tf.reshape(x, [FLAGS.batch_size, 32, 32, 3])
            op = net.forward(inp)
            y = tf.reshape(op, [FLAGS.batch_size, 10])

            trainer = net.fit(output=y, ground_truth=y_, loss='softmax_crossentropy', optimizer='adam',
                              opt_params=[FLAGS.learning_rate])
        with tf.name_scope('accuracy'):
            accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)), tf.float32))
        tf.summary.scalar('accuracy', accuracy)

        # Merge all the summaries and write them out to /tmp/mnist_logs (by default)
        merged = tf.summary.merge_all()
        train_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/train', sess.graph)
        test_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/test')

        tf.global_variables_initializer().run()

        utils = Utils(sess, FLAGS.checkpoint_reload_dir)
        if FLAGS.reload_model:
            utils.reload_model(dataset='CIFAR10')
        (x_train, y_train), (x_test, y_test) = load_data()
        y_train_one_hot = tf.squeeze(tf.one_hot(y_train, 10), axis=1)
        y_test_one_hot = tf.squeeze(tf.one_hot(y_test, 10), axis=1)
        if tag=='train':
            for i in range(FLAGS.max_steps):
                d = next_batch(FLAGS.batch_size, x_train, y_train_one_hot.eval())
                inp = {x: d[0], y_: d[1], phase: True}
                summary, _, acc, op2 = sess.run(
                    [merged, trainer.train, accuracy, y], feed_dict=inp)
                # train_writer.add_summary(summary, i)
                acc_msg = 'Error-rate at step %s: %f' % (i, 1-acc)
                worker.train_msg.emit(acc_msg)# send signal
                print(acc_msg)
                Utils.save_model(self=utils, dataset='CIFAR10')

        if tag == 'test':  # test-set accuracy
            FLAGS.batch_size = 1
            image_dir = image_dir
            print('INPUT:',image_dir)

            utils = Utils(sess, FLAGS.checkpoint_reload_dir)
            utils.reload_model(dataset='CIFAR10')

            d = io.imread(image_dir).astype('float32')
            d = d.reshape([1, 32, 32, 3])
            test_inp = {x: d, phase: False}
            # pdb.set_trace()

            import timeit
            start = timeit.default_timer()

            logit = sess.run([y], feed_dict=test_inp)
            logit = logit[0].squeeze()
            print(logit)
            pred = np.argmax(logit)

            cls = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
            stop = timeit.default_timer()
            print('Runtime: %f' % (stop - start))
            # test_writer.add_summary(summary, i)
            prob_msg = '''
<Probability>
airplane      : %.2f
automobile  : %.2f
bird            : %.2f
cat             : %.2f
deer           : %.2f
dog            : %.2f
frog            : %.2f
horse         : %.2f
ship           : %.2f
truck          : %.2f\n
                    ''' % (
            logit[0], logit[1], logit[2], logit[3], logit[4], logit[5], logit[6], logit[7], logit[8], logit[9])
            pred_msg='Predict: %s'%(cls[pred])
            worker.test_msg.emit([prob_msg, pred_msg])
            print(pred_msg)
            # pdb.set_trace()

        train_writer.close()
        test_writer.close()



def run(tag='train', worker=None, image_dir=None):
    if tf.gfile.Exists(FLAGS.summaries_dir):
        tf.gfile.DeleteRecursively(FLAGS.summaries_dir)
    tf.gfile.MakeDirs(FLAGS.summaries_dir)
    train(tag, worker, image_dir)

"""
if __name__ == '__main__':
    tf.app.run()
"""