import tensorflow as tf
from modules.module import Module
import modules.variables as variables
import pdb
import modules.activations as activations

from math import ceil

from tensorflow.python.framework import ops
from tensorflow.python.framework import sparse_tensor
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import sparse_ops


class Convolution1d(Module):
    '''
    Convolutional Layer
    '''

    def __init__(self, output_depth, batch_size=None, input_dim = None, input_depth=None, kernel_size=5, stride_size=1, act = 'linear', batch_norm = False, batch_norm_params = {'momentum':0.9, 'epsilon':1e-5, 'training':False ,'name':'bn'}, keep_prob=1.0, pad = 'SAME', weights_init= tf.truncated_normal_initializer(stddev=0.01), bias_init= tf.constant_initializer(0.0), name="conv1d"):
        self.name = name
        #self.input_tensor = input_tensor
        Module.__init__(self)
        
        
        self.batch_size = batch_size
        self.input_dim = input_dim
        self.input_depth = input_depth
        

        self.output_depth = output_depth
        self.kernel_size = kernel_size
        self.stride_size = stride_size
        self.act = act
        self.keep_prob = keep_prob
        self.batch_norm = batch_norm
        self.batch_norm_params = batch_norm_params

        self.pad = pad

        self.weights_init = weights_init
        self.bias_init = bias_init

        

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
        self.in_N, self.in_w, self.in_depth = self.input_tensor.get_shape().as_list()
        
        # init weights
        self.weights_shape = [self.kernel_size, self.input_depth, self.output_depth]
        self.strides = self.stride_size
        with tf.name_scope(self.name):
            self.weights = variables.weights(self.weights_shape, initializer=self.weights_init, name=self.name)
            self.biases = variables.biases(self.output_depth, initializer=self.bias_init, name=self.name)
        
        with tf.name_scope(self.name):
            conv = tf.nn.conv1d(self.input_tensor, self.weights, stride = self.strides, padding=self.pad)
            #conv = tf.Print(conv, [tf.shape(conv)], "conv1: ")
            #shape = conv.get_shape().as_list()
            #conv = tf.reshape(tf.nn.bias_add(conv, self.biases), conv.get_shape().as_list())
            #conv = tf.nn.bias_add(conv, self.biases)
            #conv = tf.reshape(conv, shape)

            if self.batch_norm:
                self.momentum = self.batch_norm_params['momentum']
                self.epsilon = self.batch_norm_params['epsilon']
                self.training = self.batch_norm_params['training']
                self.bn_name = self.batch_norm_params['name'] 
                conv = tf.contrib.layers.batch_norm(conv, decay=self.momentum, 
                                        updates_collections=None, epsilon=self.epsilon,
                                                      scale=True, is_training=self.training, scope=self.bn_name)

            if isinstance(self.act, str): 
                self.activations = activations.apply(conv, self.act)
            elif hasattr(self.act, '__call__'):
                self.activations = self.act(conv)
            if self.keep_prob<1.0:
                self.activations = tf.nn.dropout(self.activations, keep_prob=self.keep_prob)
            
            tf.summary.histogram('activations', self.activations)
            tf.summary.histogram('weights', self.weights)
            tf.summary.histogram('biases', self.biases)

        return self.activations

    def clean(self):
        self.activations = None
        self.R = None
