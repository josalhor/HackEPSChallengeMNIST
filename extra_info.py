import tensorflow as tf
from tensorflow import keras
import numpy as np

'''
Confirmate the accccuracy of the model
'''

model = tf.keras.models.load_model('my_model/')
x, y, x_sub = np.load('noised-MNIST.npz').values()
x = x.reshape((-1, 28, 28, 1))

loss, acc = model.evaluate(x, y, verbose=2)
print('Restored model, accuracy: {:5.2f}%'.format(100*acc))
