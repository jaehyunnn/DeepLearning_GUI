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

flags = tf.flags

flags.DEFINE_integer("input_dim", 784, 'Dimension of input node.')
flags.DEFINE_integer("hidden_dim", 100, 'Dimension of hidden node.')
# flags.DEFINE_integer("max_steps", 10000,'Number of steps to run trainer.')
flags.DEFINE_integer("check_every", 100,'Number of steps to run trainer.')
# flags.DEFINE_integer("batch_size", 100, 'Size of mini-batch.')
flags.DEFINE_integer("k", 1, 'Sampling iteration number.')
# flags.DEFINE_float("learning_rate", 0.1,'Initial learning rate')
# flags.DEFINE_string("data_dir", 'RBM/data','Directory for storing data')
# flags.DEFINE_boolean("save_model", True,'Save the trained model')
# flags.DEFINE_boolean("reload_model", False,'Restore the trained model')
# flags.DEFINE_string("checkpoint_dir", 'RBM/checkpoint','Checkpoint dir')
# flags.DEFINE_string("checkpoint_reload_dir", 'RBM/checkpoint','Checkpoint dir')

FLAGS = flags.FLAGS

def feed_dict(mnist, train):
    if train:
        xs, ys = mnist.train.next_batch(FLAGS.batch_size)
    else:
        xs, ys = mnist.test.next_batch(FLAGS.batch_size)
    return xs, ys

def train(worker=None):
    FLAGS.max_steps = 50000
    FLAGS.checkpoint_dir = 'RBM/checkpoint'
    FLAGS.checkpoint_reload_dir = 'RBM/checkpoint'
    FLAGS.data_dir = 'RBM/data'
    FLAGS.save_model = True

    if not os.path.exists(FLAGS.checkpoint_dir):
        os.makedirs(FLAGS.checkpoint_dir)
    if not os.path.exists(FLAGS.checkpoint_reload_dir):
        os.makedirs(FLAGS.checkpoint_reload_dir)

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
            f = np.load(FLAGS.checkpoint_reload_dir+'/weight.npz', encoding='latin1');
            rbm_model.w_val = f['arr_0'][0]
            rbm_model.vb_val = f['arr_0'][1]
            rbm_model.hb_val = f['arr_0'][2]

        errors = []
        for i in range(FLAGS.max_steps+1):
            batch, _ = feed_dict(mnist, True)
            rbm_model.train(batch)
            errors.append(rbm_model.get_cost(batch))
            if i % FLAGS.check_every == 0:
                acc_msg = 'Iterations: %d \treconstruction error: %f' % (i,np.mean(errors))
                worker.train_msg.emit(acc_msg)  # send signal
                print(acc_msg); errors = [];

        if FLAGS.save_model:
            weight_save = [rbm_model.w_val, rbm_model.vb_val, rbm_model.hb_val]
            path=FLAGS.checkpoint_dir+'/weight'
            np.savez(path, weight_save)
            print('Save to--[%s]'%path)

def run(worker=None):
    train(worker=worker)

"""
if __name__ == '__main__':
    tf.app.run()
"""