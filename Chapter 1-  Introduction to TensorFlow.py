import tensorflow as tf
from tensorflow import constant

d0 = tf.ones((1, ))
# print(d0.numpy())

d1 = tf.ones((2, ))
# print(d1.numpy())

d2 = tf.ones((2, 4))
# print(d2.numpy())

d3 = tf.zeros((3, 5, 2))
# print(d3.numpy())

a = tf.constant(26, shape=[5, 3])
print(a.numpy())

b = tf.constant([30, 11, 1374, 26], shape= [2, 2])
print(b.numpy())

c = tf.fill([2, 3], 5)
print(c.numpy())
