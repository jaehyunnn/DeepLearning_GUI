from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")

from RBM.rbm import RBM

import RBM.input_data as input_data

import tensorflow as tf
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

flags = tf.flags
"""
flags.DEFINE_integer("input_dim", 784, 'Dimension of input node.')
flags.DEFINE_integer("hidden_dim", 100, 'Dimension of hidden node.')
flags.DEFINE_integer("max_steps", 1000,'Number of steps to run trainer.')
flags.DEFINE_integer("check_every", 100,'Number of steps to run trainer.')
flags.DEFINE_integer("batch_size", 100, 'Size of mini-batch.')
flags.DEFINE_integer("k", 5, 'Sampling iteration number.')
flags.DEFINE_float("learning_rate", 0.1,'Initial learning rate')
flags.DEFINE_string("data_dir", 'data','Directory for storing data')
flags.DEFINE_boolean("save_model", False,'Save the trained model')
flags.DEFINE_boolean("reload_model", True,'Restore the trained model')
flags.DEFINE_string("checkpoint_dir", 'checkpoint','Checkpoint dir')
flags.DEFINE_string("checkpoint_reload_dir", 'checkpoint','Checkpoint dir')
"""
FLAGS = flags.FLAGS


def feed_dict(mnist, train):
    if train:
        xs, ys = mnist.train.next_batch(FLAGS.batch_size)
    else:
        xs, ys = mnist.test.next_batch(FLAGS.batch_size)
    return xs, ys

def test(worker=None):
    FLAGS.checkpoint_dir = 'RBM/checkpoint'
    FLAGS.checkpoint_reload_dir = 'RBM/checkpoint'
    FLAGS.data_dir = 'RBM/data'
    FLAGS.input_dim = 784
    FLAGS.hidden_dim = 100
    FLAGS.check_every = 100
    FLAGS.k = 5
    FLAGS.save_model = False
    FLAGS.reload_model = True

    if not os.path.exists('RBM/result'):
        os.makedirs('RBM/result')

    # Import data
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    config = tf.ConfigProto(allow_soft_placement = True)
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        # Input placeholders
        with tf.name_scope('input'):
            x = tf.placeholder(tf.float32, [None, FLAGS.input_dim], name='x-input')

        with tf.variable_scope('model'):
            rbm_model = RBM(FLAGS.input_dim, FLAGS.hidden_dim, lr=FLAGS.learning_rate, k=FLAGS.k)
            rbm_model.get_model(x, sess)

        if FLAGS.reload_model:
            path = FLAGS.checkpoint_reload_dir+'/weight.npz'
            f = np.load(path, encoding='latin1');
            print('Reloading from--[%s]'%path)
            rbm_model.w_val = f['arr_0'][0]
            rbm_model.vb_val = f['arr_0'][1]
            rbm_model.hb_val = f['arr_0'][2]

        test_data, _ = feed_dict(mnist, True)
        input_imgs, recons_imgs = rbm_model.recons_visualize(test_data)
        cv2.imwrite('RBM/result/input.png', input_imgs)
        cv2.imwrite('RBM/result/recons.png', recons_imgs)

        filter_imgs = rbm_model.filter_visualize()
        cv2.imwrite('RBM/result/filter.png', filter_imgs)

    worker.test_msg.emit('end')

    """
    # Display
    N_subplots = 3
    fig, axs = plt.subplots(1, N_subplots)
    axs[0].imshow(input_imgs)
    axs[0].set_title('Input images')
    axs[1].imshow(filter_imgs)
    axs[1].set_title('Filter')
    axs[2].imshow(recons_imgs)
    axs[2].set_title('Reconstructed images')
    for i in range(N_subplots):
        axs[i].axis('off')
    fig.set_dpi(150)
    plt.show()
    """

def run(worker=None):
    test(worker=worker)

"""
if __name__ == '__main__':
    tf.app.run()
"""