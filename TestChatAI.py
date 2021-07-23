import os
import AITraining as AIt
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

class TestChatAI():
    os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
    AIObj = AIt.AITraining()

    try:
        model = AIObj.createModel()
        model = AIObj.trainModel(model, AIObj.x_train, AIObj.y_train, AIObj.checkpoint_path)
        
    except (IOError, ValueError) as err:
        model = AIObj.createModel()
        model.load_weights(AIObj.checkpoint_path)

    print(tf.version.VERSION)