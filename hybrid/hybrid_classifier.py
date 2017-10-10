import sys, os
import pandas
import numpy

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../knn")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../rna")

from knn_module import KnnModule
from rna_module import RnaModule
from dataSet import DataSet

class HybridClassifier(object):
	iteration = 0
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
		self.rna_classified_samples= []
		self.intermediate_range_samples = []

		print("run hybrid classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)

		self.rna.generateModel()
		self.predictions_rna = self.rna.predict()
		
		list_position_rna_classified_samples = []
		list_position_intermediate_range_samples = []
		print(len(self.predictions_rna))
		tamanho_data_set = len(self.test_data_set.values)
		posicao_classe = len(self.test_data_set.values[0]) - 2
		#exit()
		for i in range(0,len(self.predictions_rna)):
			print("indice: " + str(i) + "  total: " + str(tamanho_data_set))
			print("Valor original: ") 
			print(self.test_data_set.values[i,posicao_classe])
			print("Valor da predicao: ") 
			print(self.predictions_rna[i])

			if(self.predictions_rna[i] > self.upper_threshold):
				print("CLASSIFICACAO CONFIAVEL!")
				self.test_data_set.set_value(i, 'classe', 1)
				#self.rna_classified_samples.append(self.test_data_set.values[i,:])
				#list_position_rna_classified_samples.append(i)
			elif( self.predictions_rna[i] < self.lower_threshold):
				print("CLASSIFICACAO CONFIAVEL!")
				self.test_data_set.set_value(i, 'classe', 0)
				#self.rna_classified_samples.append(self.test_data_set.values[i,:])
				#list_position_rna_classified_samples.append(i)
			else:
				print("FAIXA INTERMEDIARIA!")
				self.intermediate_range_samples.append(self.test_data_set.values[i,:])
				list_position_intermediate_range_samples.append(i)
	

		print("Exemplos classificados pela RNA:")
		#print(self.rna_classified_samples)
		#exit()
		print("Exemplos da faixa intermediaria:")
		print(self.intermediate_range_samples)

		print(self.test_data_set.columns)

		print("----")
		print(list_position_rna_classified_samples)
		#exit()
 
		#print(self.rna_classified_samples.index(1))

		'''dataframe_rna_classified_samples = pandas.DataFrame(
				data= self.rna_classified_samples,
				index= list_position_rna_classified_samples,
				columns= self.test_data_set.columns)

		print(dataframe_rna_classified_samples)

		DataSet.saveResults("hybrid/rna_classification", self.iteration, dataframe_rna_classified_samples)
		'''
		
		dataframe_intermediate_range_samples = pandas.DataFrame(
			data= self.intermediate_range_samples,
			index= list_position_intermediate_range_samples,
			columns= self.test_data_set.columns)

		print(dataframe_intermediate_range_samples)

		self.knn.setDataSet(self.data_set)
		self.knn.setTestDataSet(dataframe_intermediate_range_samples)


		self.predictions_knn = self.knn.run()
		
		print(dataframe_intermediate_range_samples)
		print(self.predictions_knn) 
		print(list_position_intermediate_range_samples)
		
		#exit()
		for i in range(0,len(self.predictions_knn)):
			print("Predicao knn: ") 
			print(self.predictions_knn[i])
			print("list_position")
			print(list_position_intermediate_range_samples[i])
			dataframe_intermediate_range_samples.set_value(list_position_intermediate_range_samples[i], 'classe', self.predictions_knn[i])
			print(dataframe_intermediate_range_samples.values[i])
			self.test_data_set.set_value(list_position_intermediate_range_samples[i], 'classe', self.predictions_knn[i])
			#dataframe_intermediate_range_samples.values[i][]
			#print("valor original: ")
			#print(self.test_data_set.values[list_position_intermediate_range_samples[i],len(self.test_data_set.values[i]) - 2])
			#print("valor da rna:" )
			#print(self.predictions_rna[list_position_intermediate_range_samples[i]])
		#exit()
		print(dataframe_intermediate_range_samples)
		print(self.test_data_set)

		DataSet.saveResults("hybrid/knn_classification", self.iteration, dataframe_intermediate_range_samples)

		DataSet.saveResults("hybrid/final_method_classification", self.iteration, self.test_data_set)

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
