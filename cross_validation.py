import numpy as np
import sys, os
from dataSet import DataSet
import pandas
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/hybrid")
from hybrid_classifier import HybridClassifier
from evaluate_module import EvaluateModule
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/rna")
from rna_classifier import RnaClassifier
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/knn")
from knn_classifier import KnnClassifier


class CrossValidation(object):
	iteration = 1
	dts = None
	classifier = None
	teste_sub_data_set = None
	training_sub_data_set = None
	evaluate = None
	method = None
	file_path = ""
	preprocessor = None

	def __init__(self):
		print("init")
		self.evaluate = EvaluateModule()

	def run(self):
		print("Iniciando Cross validation:")
		#for self.iteration in range(1,11):
		self.foldExecution()

	def foldExecution(self):
		for self.iteration in range(1,11):
			print("iteracao")

			print("-- FOLD " + str(self.iteration) + " --")
			self.loadTrainingData()
			self.loadTestData()

			self.preprocessor.setDataSet(self.training_sub_data_set)
			self.preprocessor.setTestDataSet(self.teste_sub_data_set)

			self.training_sub_data_set, self.teste_sub_data_set = self.preprocessor.transformCategory()

			data_set = self.teste_sub_data_set
			self.classifier.setDataSet(self.training_sub_data_set)
			self.classifier.setTestDataSet(self.teste_sub_data_set)

			self.classifier.setIteration(self.iteration)
			self.classifier.run()
			
			self.evaluate.setTestDataSet(data_set)
			self.evaluate.setIteration(self.iteration)
			if(isinstance(self.classifier, RnaClassifier)):
				print("rna")
				self.evaluate.setPath("rna/")
			elif(isinstance(self.classifier, KnnClassifier)):
				print("knn")
				self.evaluate.setPath("knn/")
			elif(isinstance(self.classifier, HybridClassifier)):
				print("hybrid")
				self.evaluate.setPath("hybrid/final_method_classification/")
			self.evaluate.run()

	def loadTrainingData(self):
		for i in range(1,11):
			if( (11 - i) != self.iteration):
				print("Carregando sub base " + str(i) + "...")
				new_sub_data_set = DataSet.loadSubDataSet(self.file_path + "sub_data_set_" + str(i) + ".csv")
				
				print("AAAA")
				print(new_sub_data_set.values)

				if (i==1):
					self.training_sub_data_set = new_sub_data_set
				else:
					self.training_sub_data_set = DataSet.concatSubDataSet(self.training_sub_data_set, new_sub_data_set)
		print(self.training_sub_data_set)

	def loadTestData(self):
		print("Carregando sub base para teste: sub base " + str(9-self.iteration) + "...")

		self.teste_sub_data_set = DataSet.loadSubDataSet(self.file_path + "sub_data_set_" + str(11-self.iteration) + ".csv")
		print(self.teste_sub_data_set)

	def setMethod(self, method):
		self.method = method

	def getMethod(self):
		return method

	def setClassifier(self, classifier):
		self.classifier = classifier

	def getClassifier(self):
		return classifier

	def setPreprocessor(self, preprocessor):
		self.preprocessor = preprocessor

	def getPreprocessor(self):
		return preprocessor	

	def setFilePath(self, file_path):
		self.file_path = file_path

