#DataFlair Automatic Music Generation Project
#load all the libraries
from music21 import *
import glob
from tqdm import tqdm
import numpy as np
import random
from tensorflow.keras.layers import LSTM,Dense,Input,Dropout
from tensorflow.keras.models import Sequential,Model,load_model
from sklearn.model_selection import train_test_split