import pandas as pd
import os
import tensorflow as tf

MAX_FEATURES = 10000
SEQUENCE_LENGTH = 2000
BATCH_SIZE = 16
SEED = 1000
AUTOTUNE = tf.data.AUTOTUNE
VOCAB_SIZE = 1500

train = pd.read_csv("../data/sentiment-analysis-on-movie-reviews/train.tsv", sep = '\t')
test = pd.read_csv("../data/sentiment-analysis-on-movie-reviews/test.tsv", sep = '\t')

data_directory = os.path.join("../data/sentiment-analysis-on-movie-reviews")