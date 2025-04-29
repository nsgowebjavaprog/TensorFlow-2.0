# import tensorflow as tf

# print(tf.__version__)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  

import tensorflow as tf

# Initialize a TensorFlow session

x = tf.constant(4, shape=(), dtype=tf.float32)  # ([[1, 2, 3], [4, 5, 6]])
print(x)

y = tf.constant([[1,2,3], [4,5,6]])
print(y)

# Maths Operations


# Indexing



# Reshape