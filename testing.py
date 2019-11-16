import requests
from pathlib import Path
from typing import Union

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

'''
Random file used to test parts how the code
was doing
'''

def plot_fig(fig, title):
    im = fig
    im = im.astype(np.float32) / 255.
    im = im.reshape(28, 28)
    
    plt.title(title)
    plt.imshow(im, cmap='gray')
    plt.axis('off')
    plt.show()

model = tf.keras.models.load_model('my_model')

data = np.load('noised-MNIST.npz')
x, y, x_submission = data.values()
x = x.reshape((-1, 28, 28, 1))

y_pred = model.predict_classes(x)

def plot_confusion_matrix(y_true, y_pred,
                            cmap=plt.cm.Blues):

    title = 'Confusion matrix'
    cm = confusion_matrix(y_true, y_pred)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        
    _, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(cm.shape[1]),
            yticks=np.arange(cm.shape[0]),
            title=title,
            ylabel='True label',
            xlabel='Predicted label')

print(classification_report(y, y_pred))
plot_confusion_matrix(y, y_pred)
plt.show()