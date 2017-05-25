import numpy as np
from keras.callbacks import CSVLogger
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils
from sklearn.model_selection import StratifiedKFold


class RnaModule(object):
	data_set_samples = []
	data_set_labels = []
	test_data_set_samples = []
	test_data_set_labels = []

	number_neurons_imput_layer = 0
	number_neurons_hidden_layer = 0
	number_neurons_output_layer = 0

	dim_imput_layer = 0

	activation_function_imput_layer = "relu"
	activation_function_hidden_layer = "relu"
	activation_function_output_layer = "sigmoid"

	model = None

	def __init__(self):
		print("init rna module")

	def generateModel(self):
		self.model = Sequential()
		self.model.add(Dense(self.number_neurons_imput_layer, input_dim=self.dim_imput_layer, init='normal', activation=self.activation_function_imput_layer))
		self.model.add(Dense(self.number_neurons_hidden_layer, init='normal', activation=self.activation_function_hidden_layer))
		self.model.add(Dense(self.number_neurons_output_layer, init='normal', activation=self.activation_function_output_layer))
	
		self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
		print(self.data_set_samples)
		csv_logger = CSVLogger('training.log')

		fit = self.model.fit(self.data_set_samples, self.data_set_labels, nb_epoch=150, batch_size=10, callbacks=[csv_logger])

	def predict(self):

		predictions = self.model.predict(self.test_data_set_samples)
		return predictions

	def predictClasses(self):
		predictions = self.model.predict_classes(self.test_data_set_samples)
		print("BASEEE:")
		print(self.test_data_set_samples)
		print("BASEEE:")
		print(self.test_data_set_labels)
		return predictions

	def setDataSet(self, data_set):
		self.data_set_samples = data_set.values[:,0:(len(data_set.values[0])-2)]
		self.data_set_labels = data_set.values[:,(len(data_set.values[0])-2)]
		#print(self.data_set_samples)
		#print(self.data_set_labels)
	
	def setTestDataSet(self, test_data_set):
		self.test_data_set_samples = test_data_set.values[:,0:(len(test_data_set.values[0])-2)]
		self.test_data_set_labels = test_data_set.values[:,(len(test_data_set.values[0])-2)]		
		#print(self.test_data_set_samples)
		#print(self.test_data_set_labels)

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

	def setActivationFunctionHiddenLayer(self, activation_function):
		self.activation_function_hidden_layer = activation_function

	def getActivationFunctionHiddenLayer(self):
		return self.activation_function_hidden_layer

	def setActivationFunctionOutputLayer(self, activation_function):
		self.activation_function_output_layer = activation_function

	def getActivationFunctionOutputLayer(self):
		return self.activation_function_output_layer

	def setDimImputLayer(self, dim_imput_layer):
		self.dim_imput_layer = dim_imput_layer

	def getDimImputLayer(self):
		return self.dim_imput_layer