import tensorflow as tf
from modules.sequential import Sequential
from modules.linear import Linear
from modules.softmax import Softmax
from modules.relu import Relu
from modules.tanh import Tanh
from modules.sigmoid import Sigmoid
from modules.dropout import Dropout
from modules.elu import Elu
from modules.convolution import Convolution
from modules.avgpool import AvgPool
from modules.maxpool import MaxPool

def nn(phase):
    net = Sequential([Convolution(output_depth=10,input_depth=1,batch_size=1000, input_dim=28, stride_size=1, pad='VALID'),
Relu(),
AvgPool(),

Convolution(output_depth=25,stride_size=1, act ='relu', pad='VALID'),
AvgPool(),

Convolution(kernel_size=4,output_depth=100,stride_size=1, act ='relu', pad='VALID'),
AvgPool(),

Convolution(kernel_size=1, output_depth=10,stride_size=1, pad='VALID'),
Softmax(),
])
    return net
