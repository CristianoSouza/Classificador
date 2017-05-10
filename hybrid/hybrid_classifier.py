import sys, os
import pandas

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../knn")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../rna")

from knn_module import KnnModule
from rna_module import RnaModule
from dataSet import DataSet

class HybridClassifier(object):
	data_set = None
	test_data_set = None
	knn = None
	rna = None
	upper_threshold = 0.2
	lower_threshold = 0.6
	intermediate_range_samples = []
	rna_classified_samples = []

	def __init__(self):
		print("init")

	def run(self):
		print("run hybrid classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)

		self.rna.generateModel()
		self.predictions = self.rna.predict()
		
		for i in range(0,len(self.predictions)):
			print("Valor original: ") 
			print(self.test_data_set.values[i,len(self.test_data_set.values[i]) - 2])
			print("Valor da predicao: ") 
			print(self.predictions[i])

			if(self.predictions[i] > self.upper_threshold):
				print("CLASSIFICACAO CONFIAVEL!")
				self.test_data_set.set_value(i, 'classe', 1)
				self.rna_classified_samples.append(self.test_data_set.values[i,:])
			elif( self.predictions[i] < self.lower_threshold):
				print("CLASSIFICACAO CONFIAVEL!")
				self.test_data_set.set_value(i, 'classe', 0)
				self.rna_classified_samples.append(self.test_data_set.values[i,:])
			else:
				print("FAIXA INTERMEDIARIA!")
				self.intermediate_range_samples.append(self.test_data_set.values[i,:])

		print("Exemplos classificados pela RNA:")
		print(self.rna_classified_samples)
		print("Exemplos da faixa intermediaria:")
		print(self.intermediate_range_samples)

		print(self.test_data_set.columns)

		print(self.rna_classified_samples[0][0:7])
		print("----")
		print(self.rna_classified_samples[0][0])


		#print(self.rna_classified_samples.index(1))

		dataframe_rna_classified_samples = pandas.DataFrame(
				data= self.rna_classified_samples,
				index= self.rna_classified_samples[0].index('0'),
				columns= self.test_data_set.columns )

		print(dataframe_rna_classified_samples)
		exit()
		#self.knn.setDataSet()
		#self.knn.setTestDataSet()

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

	def setUpperThreshold(self, upper_threshold):
		self.upper_threshold = upper_threshold

	def getUpperThreshold(self):
		return self.upper_threshold

	def setLowerThreshold(self, lower_threshold):
		self.lower_threshold = lower_threshold

	def getLowerThreshold(self):
		return lower_threshold
