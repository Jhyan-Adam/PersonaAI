from tensorflow.python.keras.layers.core import Activation
import ChatReader as cr
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

class AITraining:
    
    checkpoint_path = './chatCheckpoints/cp.ckpt'
    (x_train, y_train) = (cr.chatCrawler(cr.chat))

    def createModel(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.LSTM()
        ])



    #def trainModel(self, model, x_train, y_train, checkpoint_path):

    #TODO This is for new LSTM backend

        