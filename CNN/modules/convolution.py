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


class Convolution(Module):
    '''
    Convolutional Layer
    '''

    def __init__(self, output_depth, batch_size=None, input_dim = None, input_depth=None, kernel_size=5, stride_size=2, act = 'linear', batch_norm = False, batch_norm_params = {'momentum':0.9, 'epsilon':1e-5, 'training':False ,'name':'bn'}, pad = 'SAME', weights_init= tf.truncated_normal_initializer(stddev=0.01), bias_init= tf.constant_initializer(0.0), name="conv2d",phase = False):
        self.name = name
        #self.input_tensor = input_tensor
        Module.__init__(self)
        
        
        self.batch_size = batch_size
        self.input_dim = input_dim
        self.input_depth = input_depth
        self.phase = phase

        self.output_depth = output_depth
        self.kernel_size = kernel_size
        self.stride_size = stride_size
        self.act = act
        self.batch_norm = batch_norm
        self.batch_norm_params = batch_norm_params

        self.pad = pad

        self.weights_init = weights_init
        self.bias_init = bias_init

        

    def check_input_shape(self):
        inp_shape = self.input_tensor.get_shape().as_list()
        try:
            if len(inp_shape)!=4:
                mod_shape = [self.batch_size, self.input_dim,self.input_dim,self.input_depth]
                self.input_tensor = tf.reshape(self.input_tensor, mod_shape)
        except:
            raise ValueError('Expected dimension of input tensor: 4')

    def forward(self, input_tensor):
        self.input_tensor = input_tensor
        #pdb.set_trace()
        self.check_input_shape()
        self.in_N, self.in_h, self.in_w, self.in_depth = self.input_tensor.get_shape().as_list()
        
        # init weights
        self.weights_shape = [self.kernel_size, self.kernel_size, self.in_depth, self.output_depth]
        self.strides = [1,self.stride_size, self.stride_size,1]
        with tf.name_scope(self.name):
            self.weights = variables.weights(self.weights_shape, initializer=self.weights_init, name=self.name)
            self.biases = variables.biases(self.output_depth, initializer=self.bias_init, name=self.name)
        
        with tf.name_scope(self.name):
            conv = tf.nn.conv2d(self.input_tensor, self.weights, strides = self.strides, padding=self.pad)
            conv = tf.reshape(tf.nn.bias_add(conv, self.biases), conv.get_shape().as_list())

            if self.batch_norm:
                self.momentum = self.batch_norm_params['momentum']
                self.epsilon = self.batch_norm_params['epsilon']
                # self.training = self.batch_norm_params['training']
                self.training = self.phase
                self.bn_name = self.batch_norm_params['name'] 
                conv = tf.contrib.layers.batch_norm(conv, decay=self.momentum, 
                                        updates_collections=None, epsilon=self.epsilon,
                                                      scale=True, is_training=self.training)

            if isinstance(self.act, str): 
                self.activations = activations.apply(conv, self.act)
            elif hasattr(self.act, '__call__'):
                self.activations = self.act(conv)
            
            tf.summary.histogram('activations', self.activations)
            tf.summary.histogram('weights', self.weights)
            tf.summary.histogram('biases', self.biases)

        return self.activations

    def clean(self):
        self.activations = None
        self.R = None
