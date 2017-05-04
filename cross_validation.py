import numpy as np
import sys, os
from dataSet import DataSet
import pandas
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/hybrid")
from hybrid_classifier import HybridClassifier
from evaluate_module import EvaluateModule
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/rna")
from rna_classifier import RnaClassifier


class CrossValidation(object):
	iteration = 1
	dts = None
	classifier = None
	teste_sub_data_set = None
	training_sub_data_set = None
	evaluate = None
	method = None

	def __init__(self):
		print("init")
		self.dts = DataSet()
		self.evaluate = EvaluateModule()

	def run(self):
		print("Iniciando Cross validation:")
		#for self.iteration in range(1,11):
		self.fold_execution()

	def fold_execution(self):
		print("-- FOLD " + str(self.iteration) + " --")
		self.load_training_data()
		self.load_test_data()

		self.classifier.setDataSet(self.training_sub_data_set)
		self.classifier.setTestDataSet(self.teste_sub_data_set)

		self.classifier.run()
		
		self.evaluate.setTestDataSet(self.teste_sub_data_set)
		self.evaluate.run()

	def load_training_data(self):
		for i in range(1,11):
			if( (11 - i) != self.iteration):
				print("Carregando sub base " + str(i) + "...")
				new_sub_data_set = self.dts.load_sub_data_set("sub_data_set_" + str(i) + ".csv")
				
				print("AAAA")
				print(new_sub_data_set.values)

				if (i==1):
					self.training_sub_data_set = new_sub_data_set
				else:
					self.training_sub_data_set = self.dts.concat_sub_data_set(self.training_sub_data_set, new_sub_data_set)
		print(self.training_sub_data_set)

	def load_test_data(self):
		print("Carregando sub base para teste: sub base " + str(11-self.iteration) + "...")
		self.teste_sub_data_set = self.dts.load_sub_data_set("sub_data_set_" + str(11-self.iteration) + ".csv")
		print(self.teste_sub_data_set)

	def setMethod(self, method):
		self.method = method

	def getMethod(self):
		return method

	def setClassifier(self, classifier):
		self.classifier = classifier

	def getClassifier(self):
		return classifier
