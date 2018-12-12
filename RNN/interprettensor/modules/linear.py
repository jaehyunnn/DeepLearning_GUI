import tensorflow as tf
from modules.module import Module
import modules.variables as variables
import modules.activations as activations

class Linear(Module):
    '''
    Linear Layer
    '''

    def __init__(self, output_dim, batch_size=None, input_dim = None, act = 'linear', batch_norm = False, batch_norm_params = {'momentum':0.9, 'epsilon':1e-5, 'training':False,'name':'bn'}, keep_prob=tf.constant(1.0), weights_init= tf.truncated_normal_initializer(stddev=0.01), bias_init= tf.constant_initializer(0.0), name="linear"):
        self.name = name
        Module.__init__(self)

        self.input_dim = input_dim
        self.output_dim = output_dim
        self.batch_size = batch_size
        self.act = act
        self.batch_norm = batch_norm
        self.batch_norm_params = batch_norm_params
        
        self.keep_prob = keep_prob

        self.weights_init = weights_init
        self.bias_init = bias_init
        
    def forward(self, input_tensor):
        self.input_tensor = input_tensor
        inp_shape = self.input_tensor.get_shape().as_list()

        if len(inp_shape)!=2:
            import numpy as np
            self.input_dim =  np.prod(inp_shape[1:])
            self.input_tensor = tf.reshape(self.input_tensor,[inp_shape[0], self.input_dim])
        else:
            self.input_dim = inp_shape[1]
        self.weights_shape = [self.input_dim, self.output_dim]
        with tf.name_scope(self.name):
            self.weights = variables.weights(self.weights_shape, initializer=self.weights_init, name=self.name)
            self.biases = variables.biases(self.output_dim, initializer=self.bias_init, name=self.name)

            
        with tf.name_scope(self.name):
            linear = tf.nn.bias_add(tf.matmul(self.input_tensor, self.weights), self.biases, name=self.name)
            if self.batch_norm:
                self.momentum = self.batch_norm_params['momentum']
                self.epsilon = self.batch_norm_params['epsilon']
                self.training = self.batch_norm_params['training']
                self.bn_name = self.batch_norm_params['name'] 
                linear = tf.contrib.layers.batch_norm(linear, decay=self.momentum, 
                                        updates_collections=None, epsilon=self.epsilon,
                                                      scale=True, is_training=self.training, scope=self.bn_name)
                                        
            if isinstance(self.act, str): 
                self.activations = activations.apply(linear, self.act)
            elif hasattr(self.act, '__call__'):
                self.activations = self.act(conv)

            def dropout_check_false():
                #print('Dropout adjusted 1.0')
                return tf.constant(1.0)
                
            def dropout_check_true():
                return tf.multiply(self.keep_prob, 1)
                
            # dropout_check = self.keep_prob<=tf.constant(1.0)
            
            # dropout = tf.cond(dropout_check, dropout_check_true, dropout_check_false)
            
            # self.activations = tf.nn.dropout(self.activations, keep_prob=dropout)
            #activations = activation_fn(conv, name='activation')
            tf.summary.histogram('activations', self.activations)
            tf.summary.histogram('weights', self.weights)
            tf.summary.histogram('biases', self.biases)
            
        return self.activations

    def check_input_shape(self):
        if len(self.input_shape)!=2:
            raise ValueError('Expected dimension of input tensor: 2')


    # def lrp(self, R):
    #     return self._simple_lrp(R)

    def clean(self):
        self.activations = None
        self.R = None
