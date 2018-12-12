import tensorflow as tf
from CNN.modules.sequential import Sequential
from CNN.modules.linear import Linear
from CNN.modules.softmax import Softmax
from CNN.modules.relu import Relu
from CNN.modules.tanh import Tanh
from CNN.modules.sigmoid import Sigmoid
from CNN.modules.dropout import Dropout
from CNN.modules.elu import Elu
from CNN.modules.convolution import Convolution
from CNN.modules.avgpool import AvgPool
from CNN.modules.maxpool import MaxPool

def nn(phase):
    net = Sequential([Convolution(kernel_size=3, output_depth=64, input_depth=3, batch_size=32, input_dim=3,
                     act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
Convolution(kernel_size=3, output_depth=64, input_depth=64, batch_size=32,
         act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
MaxPool(),

Convolution(kernel_size=3, output_depth=128, input_depth=64, batch_size=32,
         act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
Convolution(kernel_size=3, output_depth=128, input_depth=128, batch_size=32,
         act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
MaxPool(),

Convolution(kernel_size=3, output_depth=256, input_depth=128, batch_size=32,
         act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
Convolution(kernel_size=3, output_depth=256, input_depth=256, batch_size=32,
         act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
Convolution(kernel_size=3, output_depth=256, input_depth=256, batch_size=32,
           act='relu', stride_size=1, pad='SAME',batch_norm = True,phase = phase),
MaxPool(),

Convolution(kernel_size=4, output_depth=512, stride_size=1, act='relu', pad='VALID',batch_norm = True,phase = phase),
Convolution(kernel_size=1, output_depth=512, stride_size=1, act='relu', pad='VALID',batch_norm = True,phase = phase),
Convolution(kernel_size=1, output_depth=10, stride_size=1, act='linear',pad='VALID',batch_norm = True,phase = phase),
Softmax(),
])
    return net
