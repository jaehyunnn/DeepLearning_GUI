
import copy
import sys
import numpy as np
from RNN.interprettensor.modules.module import Module
from RNN.interprettensor.modules.train import Train
na = np.newaxis

# -------------------------------
# Sequential layer
# -------------------------------
class Sequential(Module):
    '''
    Top level access point and incorporation of the neural network implementation.
    Sequential manages a sequence of computational neural network modules and passes
    along in- and outputs.
    '''

    def __init__(self,modules):
        '''
        Constructor

        Parameters
        ----------
        modules : list, tuple, etc. enumerable.
            an enumerable collection of instances of class Module
        '''
        Module.__init__(self)
        self.modules = modules


    def forward(self,X):
        '''
        Realizes the forward pass of an input through the net

        Parameters
        ----------
        X : numpy.ndarray
            a network input.

        Returns
        -------
        X : numpy.ndarray
            the output of the network's final layer
        '''
        if 'conv2d' in self.modules[0].name:
            if self.modules[0].batch_size is None or self.modules[0].input_depth is None or self.modules[0].input_dim is None:
                raise ValueError('Expects batch_input_shape= AND input_depth= AND input_dim= for the first layer ')
        elif 'linear' in self.modules[0].name:
            if self.modules[0].batch_size is None or self.modules[0].input_dim is None:
                raise ValueError('Expects batch_input_shape= AND input_dim= for the first layer ')
        
        
        print('Forward Pass ... ')
        print('------------------------------------------------- ')
        
        for m in self.modules:
            m.batch_size=self.modules[0].batch_size
            print(m.name+'::',end=' ')
            print(X.get_shape().as_list())
            X = m.forward(X)
            
        print('\n'+ '------------------------------------------------- ')
        
        return X

    def clean(self):
        '''
        Removes temporary variables from all network layers.
        '''
        for m in self.modules:
            m.clean()

    def fit(self,output=None,ground_truth=None,loss='CE', optimizer='Adam', opt_params=[]):
        return Train(output,ground_truth, loss, optimizer, opt_params)
