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

	number_neurons_imput_layer = 0
	number_neurons_hidden_layer = 0
	number_neurons_output_layer = 0

	activation_function_imput_layer = "relu"
	activation_function_hidden_layer = "relu"
	activation_function_output_layer = "sigmoid"

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

	def generateModel(self):
		model = Sequential()
		model.add(Dense(self.number_neurons_imput_layer, input_dim=4, init='normal', activation=self.activation_function_imput_layer))
		model.add(Dense(self.number_neurons_hidden_layer, input_dim=4, init='normal', activation=self.activation_function_hidden_layer))
		model.add(Dense(self.number_neurons_output_layer, init='normal', activation=self.activation_function_output_layer))
		
		#Compile model
		model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

	def setNumberNeuronsImputLayer(self, number):
		self.number_neurons_imput_layer = number

	def getNumberNeuronsImputLayer(self):
		return self.number_neurons_imput_layer

	def setNumberNeuronsHiddenLayer(self, number):
		self.number_neurons_hidden_layer = number

	def getNumberNeuronsHiddenLayer(self):
		return self.number_neurons_hidden_layer

	def setNumberNeuronsOutputLayer(self, number):
		self.number_neurons_output_layer = number

	def getNumberNeuronsOutputLayer(self):
		return self.number_neurons_output_layer


	def setActivationFunctionImputLayer(self, activation_function):
		self.activation_function_imput_layer = activation_function

	def getActivationFunctionImputLayer(self):
		return self.activation_function_imput_layer

	def setActivationFunctionsHiddenLayer(self, activation_function):
		self.activation_function_hidden_layer = activation_function

	def getActivationFunctionHiddenLayer(self):
		return self.activation_function_hidden_layer

	def setActivationFunctionOutputLayer(self, activation_function):
		self.activation_function_output_layer = activation_function

	def getActivationFunctionOutputLayer(self):
		return self.activation_function_output_layer