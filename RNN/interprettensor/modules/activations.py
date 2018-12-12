import tensorflow as tf


def apply(input_tensor, act):
    if act in globals():
        return globals()[act](input_tensor)
    else:
        raise ValueError("Activation function not available")

def tanh(input_tensor):
    return tf.nn.tanh(input_tensor)

def relu(input_tensor):
    return tf.nn.relu(input_tensor)

def elu(input_tensor):
    return tf.nn.elu(input_tensor)

def linear(input_tensor):
    return input_tensor

def lrelu(input_tensor, leak=0.2):
    return tf.maximum(input_tensor, leak*input_tensor)

def sigmoid(input_tensor):
    return tf.nn.sigmoid(input_tensor)
