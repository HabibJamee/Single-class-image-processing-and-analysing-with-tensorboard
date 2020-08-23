from tensorflow.keras.callbacks import TensorBoard
NAME = "" #model name
tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.fit(X, y,
          batch_size=10,
          epochs=3,
          validation_split=0.3,
          callbacks=[tensorboard])
          
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
from tensorflow.keras.callbacks import TensorBoard
from numpy import array
import pickle
import time
