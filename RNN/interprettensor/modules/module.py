import tensorflow as tf


# -------------------------------
# Modules for the neural network
# -------------------------------
layer_count = 0
class Module:
    '''
    Superclass for all computation layer implementations
    '''

    def __init__(self):
        ''' The constructor '''
        global layer_count
        layer_count = layer_count + 1
        
        if hasattr(self, 'name'):
            self.name = self.name+'_'+str(layer_count)

            #self.previous_input=self.
            #print 'LAYER COUNT: '+str(layer_count)
        #values for presetting lrp decomposition parameters per layer
        self.lrp_var = None
        self.lrp_param = 1.
        #self.input_shape = self.input_shape
        # 
        # self.forward(self.input_tensor)
        
    def forward(self,X):
        ''' forward passes the input data X to the layer's output neurons '''
        return X

    def clean(self):
        ''' clean can be used to remove any temporary variables from the layer, e.g. just before serializing the layer object'''
        pass


