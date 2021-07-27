import ChatReader as cr
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

class AITraining:
    
    checkpoint_path = './chatCheckpoints/cp.ckpt'
    (x_train, y_train) = (cr.chatCrawler(cr.chat))

    def createModel(self):
        model = tf.keras.models.Sequential([  
            tf.keras.layers.Flatten(input_shape=(1, 3)),
            tf.keras.layers.Dense(6, activation='relu', name='layer1'),
            tf.keras.layers.Dense(10, activation='relu', name='layer2'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(6, activation='relu', name='layer3')
        ])

        model.compile(optimizer='adam',
                    loss=tf.keras.losses.CategoricalCrossentropy(
                        from_logits=True),
                    metrics=['accuracy'])

        return model


    def trainModel(self, model, x_train, y_train, checkpoint_path):
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path,
                                                        save_weights_only=True,
                                                        verbose=1)
        model.fit(x_train, y_train, epochs=6, callbacks=[cp_callback])
        model.save_weights('./chatCheckpoints/ckPtWeights')

        predictions = model(self.x_train[: 1]).numpy()
        predictions
        tf.nn.softmax(predictions).numpy()

        return model





