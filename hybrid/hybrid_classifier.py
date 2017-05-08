import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../knn")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../rna")

from knn_module import KnnModule
from rna_module import RnaModule

class HybridClassifier(object):
	data_set = None
	test_data_set = None
	knn = None
	rna = None

	def __init__(self):
		print("init")

	def run(self):
		print("run hybrid classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)

		self.rna.generateModel()
		self.predictions = self.rna.predict()
		self.saveResults()

	def saveResults(self):
		print("save results")

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

	def setRna(self, rna):
		self.rna = rna

	def getRna(self):
		return self.rna

	def setIteration(self, iteration):
		self.iteration = iteration