### Requirements
    tensorflow >= 1.0.0
    python >= 3
    opencv >= 3.2.0 
    
# Features

This TF-wrapper considers single layer Restricted Boltzmann Machine.
This example handles dimension reduction of MNIST in unsupervised manner.

Number of hidden nodes can be modified by
flags.DEFINE_integer("hidden_dim", 100, 'Dimension of hidden node.')

And number of visible-hidden iteration can be modified by 
flags.DEFINE_integer("k", 1, 'Sampling iteration number.')

Test code contains filter visualization and reconstruction of image using dimension-reduced hidden vectors.