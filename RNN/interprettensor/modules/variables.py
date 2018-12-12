import tensorflow as tf




def weights(weights_shape, initializer=tf.truncated_normal_initializer(stddev=0.01), name=''):
    weights_shape = weights_shape
    #import pdb;pdb.set_trace()
    return tf.get_variable(name+'/weights', shape=weights_shape, initializer=initializer)


def biases( bias_shape, initializer = tf.constant_initializer(0.0), name =''):
    bias_shape = bias_shape
    return tf.get_variable(name+'/biases', bias_shape, initializer=initializer)

