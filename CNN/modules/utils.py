import numpy as np
import tensorflow as tf

class Summaries():
    def __init__(self, summaries_dir, sub_dir=None, graph=None, name="summaries"):
        self.summaries_dir = summaries_dir
        self.sub_dir = sub_dir
        self.writer = self.create_writer(graph)

    def create_writer(self, graph=None):
        return tf.train.SummaryWriter(self.summaries_dir + '/' + self.sub_dir, graph)
        

class Utils():
    def __init__(self, session, checkpoint_dir=None, var_list = None, name="utils"):
        self.name = name
        self.session = session
        self.checkpoint_dir = checkpoint_dir
        if var_list:
            self.saver = tf.train.Saver(var_list)
        else:
            self.saver = tf.train.Saver()
        

    def reload_model(self, dataset='MNIST'):
        if self.checkpoint_dir is not None:
            ckpt = tf.train.get_checkpoint_state(self.checkpoint_dir)
            if ckpt and ckpt.model_checkpoint_path:
                print('Reloading from -- '+self.checkpoint_dir+'/%s_model.ckpt'%(dataset))
                self.saver.restore(self.session, ckpt.model_checkpoint_path)

    def save_model(self, dataset='MNIST'):
        import os
        if not os.path.exists(self.checkpoint_dir):
            os.system('mkdir '+self.checkpoint_dir)
        save_path = self.saver.save(self.session, self.checkpoint_dir+'/%s_model.ckpt'%(dataset),write_meta_graph=False)
