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
