import numpy as np
from keras.callbacks import CSVLogger
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder



class RnaModule(object):
	data_set_samples = []
	data_set_labels = []
	test_data_set_samples = []
	test_data_set_labels = []

	def __init__(self, data_set, test_data_set):
		print((len(data_set[1])-1))
		self.data_set_samples = data_set[:,0:(len(data_set[0])-1)]
		self.data_set_labels = data_set[:,(len(data_set[0])-1)]
		self.test_data_set_samples = test_data_set[:,0:(len(test_data_set[0])-1)]
		self.test_data_set_labels = test_data_set[:,(len(test_data_set[0])-1)]

		print(self.data_set_samples)
		print(self.data_set_labels)
		print(self.test_data_set_samples)
		print(self.test_data_set_labels)

	def generate_model(self):
		model = Sequential()
		model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
		model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
		model.add(Dense(1, init='normal', activation='tanh'))
		
		#Compile model
		model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])