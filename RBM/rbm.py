import tensorflow as tf
import numpy as np
import cv2

# RBM is unsupervised, generative model.
# DBM(Deep Boltzmann Machine) is stack of RBM, and used for pre-training of multi-layer NN
# DBM is trained in greedy manner, which is consist of v~h_1 RBM, h_1~h_2 RBM, ... h_k-1~h_k RBM
# And it is fine-tuned using appropriate output data such as class.
# This code is RBM with single hidden layer. It's not DBM.

class RBM:
    # vd : dimension of visible node
    # hd : dimension of hidden node
    # lr : learning rate
    # k : sampling iteration number. CD-k, recons, etc.
    def __init__(self, vd, hd, lr=1.0, k=1):
        # parameter placeholders of RBM
        self.W = tf.placeholder('float32', [vd, hd])
        self.hb = tf.placeholder('float32', [hd])
        self.vb = tf.placeholder('float32', [vd])

        # parameter values of RBM
        self.w_val = np.zeros([vd, hd], np.float32)
        self.vb_val = np.zeros([vd], np.float32)
        self.hb_val = np.zeros([hd], np.float32)
        self.lr = lr
        self.k = k

        # first and last node
        self.vi = tf.placeholder('float32', [None, vd])
        self.hi = tf.placeholder('float32', [None, hd])

    # forward operation
    def v2h(self, v_sample):
        _hi = tf.nn.sigmoid(tf.matmul(v_sample, self.W) + self.hb)
        hi = tf.nn.relu(tf.sign(_hi - tf.random_uniform(tf.shape(_hi))))
        return hi

    # backward operation
    def h2v(self, h_sample):
        _vi = tf.nn.sigmoid(tf.matmul(h_sample, tf.transpose(self.W)) + self.vb)
        vi = tf.nn.relu(tf.sign(_vi - tf.random_uniform(tf.shape(_vi))))
        return vi

    def h2v_no_gibbs(self, h_sample):
        _vi = tf.nn.sigmoid(tf.matmul(h_sample, tf.transpose(self.W)) + self.vb)
        return _vi

    # propagation in visible node
    def v2v(self, v_sample):
        hi = self.v2h(v_sample)
        vi = self.h2v(hi)
        return vi

    def v2v_no_gibbs(self, v_sample):
        _hi = tf.nn.sigmoid(tf.matmul(v_sample, self.W) + self.hb)
        _vi = tf.nn.sigmoid(tf.matmul(_hi, tf.transpose(self.W)) + self.vb)
        return _vi

    # propagation in hidden node
    def h2h(self, h_sample):
        vi = self.h2v(h_sample)
        hi = self.v2h(vi)
        return hi

    def get_model(self, X, sess):
        self.sess = sess
        alpha = self.lr
        self.v0 = X
        self.h0 = self.v2h(self.v0)
        hs = [self.h0]
        for i in range(self.k-1):
            hs.append(self.h2h(hs[i]))
        self.vk = self.h2v(hs[-1])
        self.hk = self.v2h(self.vk)
        self.err = tf.reduce_mean(tf.square(self.v0 - self.vk))
        w_pos_grad = tf.matmul(tf.transpose(self.v0), self.h0)
        w_neg_grad = tf.matmul(tf.transpose(self.vk), self.hk)
        CD = (w_pos_grad - w_neg_grad) / tf.to_float(tf.shape(self.v0)[0])
        self.update_w = self.W + alpha * CD
        self.update_vb = self.vb + alpha * tf.reduce_mean(self.v0 - self.vk, 0)
        self.update_hb = self.hb + alpha * tf.reduce_mean(self.h0 - self.hk, 0)

    def train(self, input):
        if len(input.shape) == 1:
            batch_input = np.zeros([1, input.shape[0]])
            batch_input[0, :] = input
        else:
            batch_input = input
        cur_w = self.sess.run(self.update_w, feed_dict={self.v0: batch_input, self.W: self.w_val, self.vb: self.vb_val, self.hb: self.hb_val})
        cur_vb = self.sess.run(self.update_vb, feed_dict={self.v0: batch_input, self.W: self.w_val, self.vb: self.vb_val, self.hb: self.hb_val})
        cur_hb = self.sess.run(self.update_hb, feed_dict={self.v0: batch_input, self.W: self.w_val, self.vb: self.vb_val, self.hb: self.hb_val})
        self.w_val = cur_w
        self.vb_val = cur_vb
        self.hb_val = cur_hb

    def get_cost(self, input):
        if len(input.shape) == 1:
            batch_input = np.zeros([1, input.shape[0]])
            batch_input[0, :] = input
        else:
            batch_input = input
        return self.sess.run(self.err, feed_dict={self.v0: batch_input, self.W: self.w_val, self.vb: self.vb_val, self.hb: self.hb_val})

    def get_recons(self, input):
        if len(input.shape) == 1:
            batch_input = np.zeros([1, input.shape[0]])
            batch_input[0, :] = input
        else:
            batch_input = input

        vrs = [self.v0]
        for i in range(self.k-1):
            vrs.append(self.v2v_no_gibbs(vrs[i]))
        self.vr = self.v2v_no_gibbs(vrs[-1])

        return self.sess.run(self.vr, feed_dict={self.v0: batch_input, self.W: self.w_val, self.vb: self.vb_val, self.hb: self.hb_val})

    def recons_visualize(self, input):
        recons = self.get_recons(input)

        batch_num = input.shape[0]
        temp_hw = np.int32(np.ceil(batch_num ** 0.5))
        recons_imgs = np.zeros([temp_hw*28, temp_hw*28])
        input_imgs = np.zeros([temp_hw*28, temp_hw*28])

        count = 0
        for i in range(temp_hw):
            for j in range(temp_hw):
                recons_imgs[(28*i):(28*(i+1)), (28*j):(28*(j+1))] = np.reshape(recons[count, :], (28, 28))
                input_imgs[(28*i):(28*(i+1)), (28*j):(28*(j+1))] = np.reshape(input[count, :], (28, 28))
                count += 1
                if count >= batch_num:
                    break
        return np.int32(input_imgs*255), np.int32(recons_imgs*255)

    def filter_visualize(self):
        temp_hw = np.int32(np.ceil(self.hb_val.shape[0] ** 0.5))
        temp_images = np.zeros([temp_hw*28, temp_hw*28])
        count = 0
        for i in range(temp_hw):
            for j in range(temp_hw):
                count += 1
                if count > self.hb_val.shape[0]:
                    break
                temp_images[(28*i):(28*(i+1)), (28*j):(28*(j+1))] = np.reshape(self.w_val[:, temp_hw*i+j], [28, 28])
        return np.int32((temp_images + 1) * 127.5)
