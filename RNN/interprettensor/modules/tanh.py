
import tensorflow as tf
from modules.module import Module



class Tanh(Module):
    '''
    Tanh Layer
    '''

    def __init__(self,name='tanh'):
        self.name = name
        Module.__init__(self)
        
    def forward(self,input_tensor, batch_size=10, img_dim=28):
        self.input_tensor = input_tensor
        with tf.name_scope(self.name):
            #with tf.name_scope('activations'):
            self.activations = tf.nn.tanh(self.input_tensor, name=self.name )
            tf.summary.histogram('activations', self.activations)
        return self.activations

    def clean(self):
        self.activations = None
