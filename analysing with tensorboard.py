from tensorflow.keras.callbacks import TensorBoard
NAME = "" #model name
tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.fit(X, y,
          batch_size=10,
          epochs=3,
          validation_split=0.3,
          callbacks=[tensorboard])
          

