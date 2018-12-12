
import tensorflow as tf
from CNN.modules.module import Module


from math import ceil

from tensorflow.python.framework import ops
from tensorflow.python.framework import sparse_tensor
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import sparse_ops


class MaxPool(Module):

    def __init__(self, pool_size=2, pool_stride=None, pad = 'SAME',name='maxpool'):
        self.name = name
        Module.__init__(self)
        self.pool_size = pool_size
        self.pool_kernel = [1, self.pool_size, self.pool_size, 1]
        self.pool_stride = pool_stride
        if self.pool_stride is None:
            self.stride_size=self.pool_size
        else:
            self.stride_size=self.pool_stride
        self.pool_stride=[1, self.stride_size, self.stride_size, 1] 
        self.pad = pad
        
    def forward(self,input_tensor, batch_size=10, img_dim=28):
        self.input_tensor = input_tensor
        self.in_N, self.in_h, self.in_w, self.in_depth = self.input_tensor.get_shape().as_list()
        
        with tf.name_scope(self.name):
            self.activations = tf.nn.max_pool(self.input_tensor, ksize=self.pool_kernel,strides=self.pool_stride,padding=self.pad, name=self.name )
            tf.summary.histogram('activations', self.activations)

        return self.activations

    def clean(self):
        self.activations = None
        self.R = None

