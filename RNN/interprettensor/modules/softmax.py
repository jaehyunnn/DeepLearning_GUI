

import tensorflow as tf
from modules.module import Module



class Softmax(Module):
    '''
    Softmax Layer
    '''

    def __init__(self, name='softmax'):
        self.name = name
        Module.__init__(self)
        
    def forward(self,input_tensor):
        self.input_tensor = input_tensor
        with tf.name_scope(self.name):
            #with tf.name_scope('activations'):
            self.activations = tf.nn.softmax(self.input_tensor, name=self.name)
            tf.summary.histogram('activations', self.activations)
        return self.activations

    def clean(self):
        self.activations = None

    
