
"""Functions to use Quick Draw data."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import functools
import os

flags = tf.flags
flags.DEFINE_string("training_data", "quickdraw_data/training.tfrecord-00000-of-00010",'Path to training data (tf.Example in TFRecord format)')
flags.DEFINE_string("eval_data", "quickdraw_data/eval.tfrecord-00000-of-00010",'Path to eval data (tf.Example in TFRecord format)')
flags.DEFINE_string("classes_file", "quickdraw_data/training.tfrecord.classes",'Path to classes info (tf.Example in TFRecord format)')
FLAGS = flags.FLAGS


def get_train_data(data_dir):
    train_file_names = [data_dir+f for f in os.listdir(data_dir) if 'training.tfrecord-' in f]
    return train_file_names


def get_eval_data(data_dir):
    eval_file_names = [data_dir+'eval.tfrecord-00000-of-00010']
    return eval_file_names


def get_input_fn(mode, tfrecord_pattern, batch_size):
    """Creates an input_fn that stores all the data in memory.

    Args:
     mode: one of tf.contrib.learn.ModeKeys.{TRAIN, INFER, EVAL}
     tfrecord_pattern: path to a TF record file created using create_dataset.py.
     batch_size: the batch size to output.

    Returns:
      A valid input_fn for the model estimator.
    """
    def _get_input_tensors(features, labels):
        """Converts the input dict into inks, lengths, and labels tensors."""
        # features[ink] is a sparse tensor that is [8, batch_maxlen, 3]
        # inks will be a dense tensor of [8, maxlen, 3]
        # shapes is [batchsize, 2]
        shapes = features["shape"]
        # lengths will be [batch_size]
        lengths = tf.squeeze(
            tf.slice(shapes, begin=[0, 0], size=[batch_size, 1]))
        inks = tf.reshape(features["ink"], [batch_size, -1, 3])
        if labels is not None:
            labels = tf.squeeze(labels)
        return inks, lengths, labels

    def _parse_tfexample_fn(example_proto, mode):
        """Parse a single record which is expected to be a tensorflow.Example."""
        feature_to_type = {
            "ink": tf.VarLenFeature(dtype=tf.float32),
            "shape": tf.FixedLenFeature([2], dtype=tf.int64),
            "class_index": tf.FixedLenFeature([1], dtype=tf.int64)
        }
        parsed_features = tf.parse_single_example(example_proto, feature_to_type)
        labels = parsed_features["class_index"]
        parsed_features["ink"] = tf.sparse_tensor_to_dense(parsed_features["ink"])
        return parsed_features, labels

    dataset = tfrecord_pattern.map(functools.partial(_parse_tfexample_fn, mode=mode))
    if mode == tf.estimator.ModeKeys.TRAIN:
        dataset = dataset.shuffle(buffer_size=10000)
    if mode != tf.estimator.ModeKeys.PREDICT:
        dataset = dataset.repeat()
    dataset = dataset.padded_batch(batch_size, padded_shapes=dataset.output_shapes)
    iterator = dataset.make_one_shot_iterator()

    X, y = iterator.get_next()
    inks, lengths, labels = _get_input_tensors(X, y)

    return inks, lengths, labels


class Dataset():
    def __init__(self, data_dir=None):
        self.data_dir = data_dir
        self.train_data_names = get_train_data(data_dir)
        self.eval_data_names = get_eval_data(data_dir)

    def get_num_classes(self):
        classes_path = self.data_dir + 'training.tfrecord.classes'
        with tf.gfile.GFile(classes_path, "r") as f:
            classes = [x for x in f]
        num_classes = len(classes)
        return num_classes

    def get_classes(self):
        classes_path = self.data_dir + 'training.tfrecord.classes'
        with tf.gfile.GFile(classes_path, "r") as f:
            classes = [x for x in f]
        return classes

    def get_data(self, mode=None, batch_size=None):
        if mode == 'train':
            dataset = tf.data.TFRecordDataset(self.train_data_names)
        else:
            dataset = tf.data.TFRecordDataset(self.eval_data_names)
        return get_input_fn(mode=mode, tfrecord_pattern=dataset, batch_size=batch_size)