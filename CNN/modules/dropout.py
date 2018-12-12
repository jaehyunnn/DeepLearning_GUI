import tensorflow as tf
from CNN.modules.module import Module
import CNN.modules.variables as variables
import pdb
import CNN.modules.activations as activations

from math import ceil

from tensorflow.python.framework import ops
from tensorflow.python.framework import sparse_tensor
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import sparse_ops


class Dropout(Module):
    '''
    Dropout Layer
    '''

    def __init__(self, name='dropout', keep_prob=0.5):
        self.name = name
        self.keep_prob = keep_prob
        Module.__init__(self)

    def forward(self, input_tensor, batch_size=10, img_dim=28):
        self.input_tensor = input_tensor
        with tf.name_scope(self.name):
            self.activations = tf.nn.dropout(self.input_tensor, keep_prob=self.keep_prob,name=self.name)
            tf.summary.histogram('activations', self.activations)
        return self.activations

    def clean(self):
        self.activations = None