import tensorflow as tf
from modules.module import Module
import modules.variables as variables
import pdb
import modules.activations as activations

from math import ceil
import numpy as np

from tensorflow.python.framework import ops
from tensorflow.python.framework import sparse_tensor
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import sparse_ops


class Recurrent(Module):
    '''
    Recurrent Layer (Cudnn_LSTM)
    '''

    def __init__(self, num_layers, num_nodes, direction="unidirectional", batch_size=None, input_dim = None, input_depth=None, act = 'linear', keep_prob=1.0, var = False, lengths=None, weights_init= tf.truncated_normal_initializer(stddev=0.01), bias_init= tf.constant_initializer(0.0), training=True, name="lstm"):
        self.name = name
        Module.__init__(self)
        
        
        self.batch_size = batch_size
        self.input_dim = input_dim
        self.input_depth = input_depth

        self.num_layers = num_layers
        self.num_nodes = num_nodes
        self.direction = direction
        self.act = act
        self.dropout = 1.0 - keep_prob

        self.var = var
        self.lengths = lengths
        
        self.weights_init = weights_init
        self.bias_init = bias_init
        
        self.training = training
        

    def check_input_shape(self):
        inp_shape = self.input_tensor.get_shape().as_list()
        try:
            if len(inp_shape)!=3:
                mod_shape = [self.batch_size, self.input_dim, self.input_depth]
                self.input_tensor = tf.reshape(self.input_tensor, mod_shape)
        except:
            raise ValueError('Expected dimension of input tensor: 3')

    def forward(self, input_tensor):
        self.input_tensor = input_tensor
        #pdb.set_trace()
        self.check_input_shape()
        
        with tf.name_scope(self.name): 
            # [B, L, Ch] -> [L, B, Ch]
            self.input_tensor = tf.transpose(self.input_tensor, [1, 0, 2])
                   
            cell = tf.contrib.cudnn_rnn.CudnnLSTM(
                    num_layers= self.num_layers,
                    num_units= self.num_nodes,
                    name=self.name,
                    direction= self.direction)
            conv, _ = cell(self.input_tensor)
            
            if isinstance(self.act, str): 
                self.activations = activations.apply(conv, self.act)
            elif hasattr(self.act, '__call__'):
                self.activations = self.act(conv)
                
            # [L, B, Ch] -> [B, L, Ch]
            self.activations = tf.transpose(self.activations, [1, 0, 2])
        
        with tf.name_scope(self.name):
            if self.var:
                mask = tf.tile(
                    tf.expand_dims(tf.sequence_mask(self.lengths, tf.shape(self.activations)[1]), 2),
                    [1, 1, tf.shape(self.activations)[2]])
                zero_outside = tf.where(mask, self.activations, tf.zeros_like(self.activations))
                self.activations = tf.reduce_sum(zero_outside, axis=1)
                
            tf.summary.histogram('activations', self.activations)
            tf.summary.histogram('weights', cell.kernel)

        return self.activations

    def clean(self):
        self.activations = None
        self.R = None
