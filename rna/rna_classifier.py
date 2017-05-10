from rna_module import RnaModule
import pandas
import os
from dataSet import DataSet

class RnaClassifier(object):

	data_set = None
	test_data_set = None
	rna = None
	predictions = None
	iteration = 0

	def __init__(self):
		print "aa"

	def run(self):
		print("RUN RNA classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)

		self.rna.generateModel()
		self.predictions = self.rna.predictClasses()
		self.saveResults()

	def saveResults(self):
		for i in range(0,len(self.predictions)):
			self.test_data_set.set_value(i,'classe',self.predictions[i])

		DataSet.saveResults("rna", self.iteration, self.test_data_set)	

	def setDataSet(self, data_set):
		self.data_set = data_set

	def getDataSet(self):
		return self.data_set

	def setTestDataSet(self, test_data_set):
		self.test_data_set = test_data_set

	def getTestDataSet(self):
		return self.test_data_set

	def setRna(self, rna):
		self.rna = rna

	def getRna(self):
		return self.rna

	def setIteration(self, iteration):
		self.iteration = iteration