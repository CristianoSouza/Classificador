from knn_module import KnnModule
import pandas
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from dataSet import DataSet

class KnnClassifier(object):

	data_set = None
	test_data_set = None
	predictions = []
        result_path = ""
	knn = None

	def __init__(self):
		print "Knn classifier"

	def run(self):
		print "RUN Knn classifier"
		print(self.data_set)
		self.knn.setDataSet(self.data_set)
		self.knn.setTestDataSet(self.test_data_set)
		self.predictions = self.knn.run()
		print("Predicao knn: ")
		print(self.predictions)
		self.saveResults()

	def saveResults(self):
		data_set = self.test_data_set[:] 
		for i in range(0,len(self.predictions)):
			print("ALTERANDO VALOR DA CLASSE")
			data_set.set_value(i,'classe',self.predictions[i])
		DataSet.saveResults(self.result_path, self.iteration, data_set)

	def setDataSet(self, data_set):
		self.data_set = data_set

	def getDataSet(self):
		return self.data_set

	def setTestDataSet(self, test_data_set):
		self.test_data_set = test_data_set

	def getTestDataSet(self):
		return self.test_data_set

	def setKnn(self, knn):
		self.knn = knn

	def getKnn(self):
		return self.knn

	def setIteration(self, iteration):
		self.iteration = iteration

        def setResultPath(self, result_path):
            self.result_path = result_path
