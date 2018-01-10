import sys, os
import pandas 
import time
import numpy

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../knn")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../rna")

from knn_module import KnnModule
from rna_module import RnaModule

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../..")
from dataSet import DataSet

class HybridClassifier(object):
	iteration = 0
	data_set = None
	test_data_set = None
	knn = None
	rna = None
	upper_threshold = 0.7
	lower_threshold = -0.7
	intermediate_range_samples = []
	rna_classified_samples = []
	result_path = ""
	training_time = 0
	test_time = 0
	limite_faixa_sup = 0
        limite_faixa_inf = 0


	def __init__(self):
		print("init")

	def run(self):
		self.rna_classified_samples= []
		self.intermediate_range_samples = []

		print("run hybrid classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)
		self.knn.setDataSet(self.data_set)
		training_time_start = time.time()
		outputs_training, predictions = self.rna.generateHybridModel()
		print (predictions)

		positivos = 0
		negativos = 0
		valor_negativo = 0
		valor_positivo = 0

		positivos_serie =  pandas.Series([outputs_training[0]])
		negativos_serie =  pandas.Series([outputs_training[0]])
		
		for i in range(0,len(outputs_training)):
			if(predictions[i] == 0 ):
				negativos = negativos + 1
				valor_negativo = valor_negativo + outputs_training[i]
				negativos_serie[i] = outputs_training[i]
			elif(predictions[i] == 1):
				positivos = positivos + 1
				valor_positivo = valor_positivo + outputs_training[i]
				positivos_serie[i] = outputs_training[i]

		#self.upper_threshold = valor_positivo / positivos
		#self.lower_threshold = valor_negativo / negativos
		print(positivos_serie.values)
		print(negativos_serie.values)
		self.upper_threshold = positivos_serie.median()
		self.lower_threshold = negativos_serie.median()
		print( positivos_serie.mean())
		print( negativos_serie.mean())
		print( positivos_serie.std())
		print( negativos_serie.std())
		print("TOPO: ", self.upper_threshold)
		print("baixo: ", self.lower_threshold)
		#exit()
		self.knn.buildExamplesBase()
		self.training_time = time.time() - training_time_start

	
		list_position_rna_classified_samples = []
		list_position_intermediate_range_samples = []

		test_time_start = time.time()
		self.predictions_rna = self.rna.predict()
		self.test_time = time.time() - test_time_start

		#print(len(self.predictions_rna))
		tamanho_predicao = len(self.predictions_rna)
		tamanho_data_set = len(self.test_data_set.values)
		posicao_classe = len(self.test_data_set.values[0]) - 2
		#exit()

		if (self.verifyClassesPredictions(predictions) == True):
			print("!")
			for i in range(0,len(self.predictions_rna)):
				#print("indice: " + str(i) + "  total: " + str(tamanho_predicao))
				#print("Valor original: ") 
				#print(self.test_data_set.values[i,posicao_classe])
				print("Valor da predicao: ") 
				print(self.predictions_rna[i])
				if(self.predictions_rna[i] > (self.upper_threshold - self.limite_faixa_sup) ):
				#if(self.predictions_rna[i] > 0 ):
					#print("CLASSIFICACAO CONFIAVEL!")
					self.test_data_set.set_value(i, 'classe', 1)
					#self.rna_classified_samples.append(self.test_data_set.values[i,:])
					#list_position_rna_classified_samples.append(i)
				elif( self.predictions_rna[i] < (self.lower_threshold + self.limite_faixa_inf)):
					#print("CLASSIFICACAO CONFIAVEL!")
					self.test_data_set.set_value(i, 'classe', 0)
					#self.rna_classified_samples.append(self.test_data_set.values[i,:])
					#list_position_rna_classified_samples.append(i)
				else:
					#print("FAIXA INTERMEDIARIA!")
					self.intermediate_range_samples.append(self.test_data_set.values[i,:])
					list_position_intermediate_range_samples.append(i)

			
			del(self.predictions_rna)
			#print("Exemplos classificados pela RNA:")
			#print(self.rna_classified_samples)
			#exit()
			print("Exemplos da faixa intermediaria:")
			print(self.intermediate_range_samples)

			#print(self.test_data_set.columns)

			print("----")
			#print(list_position_rna_classified_samples)
			#exit()
	 
			#print(self.rna_classified_samples.index(1))

			dataframe_rna_classified_samples = pandas.DataFrame(
					data= self.rna_classified_samples,
					index= list_position_rna_classified_samples,
					columns= self.test_data_set.columns)

			print(dataframe_rna_classified_samples)

			DataSet.saveResults( self.result_path + "rna_classification/", self.iteration, dataframe_rna_classified_samples)
			del(dataframe_rna_classified_samples)
			del(list_position_rna_classified_samples)
		else:
			for i in range(0,len(self.predictions_rna)):
				self.intermediate_range_samples.append(self.test_data_set.values[i,:])
				list_position_intermediate_range_samples.append(i)

			print(dataframe_intermediate_range_samples)
	                

		dataframe_intermediate_range_samples = pandas.DataFrame(
			data= self.intermediate_range_samples,
			index= list_position_intermediate_range_samples,
			columns= self.test_data_set.columns)

		self.knn.setTestDataSet(dataframe_intermediate_range_samples)
		DataSet.saveResults( self.result_path + "knn_classification/", self.iteration, dataframe_intermediate_range_samples)

		test_time_start = time.time()
		self.predictions_knn = self.knn.run()
		self.test_time = self.test_time + (time.time() - test_time_start)
		
		del(self.data_set)
		del(dataframe_intermediate_range_samples)
		
		#print(dataframe_intermediate_range_samples)
		print(self.predictions_knn) 
		print(list_position_intermediate_range_samples)
		
		#exit()
		for i in range(0,len(self.predictions_knn)):
			#print("Predicao knn: ") 
			#print(self.predictions_knn[i])
			#print("list_position")
			#print(list_position_intermediate_range_samples[i])
			#dataframe_intermediate_range_samples.set_value(list_position_intermediate_range_samples[i], 'classe', self.predictions_knn[i])
			#print(dataframe_intermediate_range_samples.values[i])
			self.test_data_set.set_value(list_position_intermediate_range_samples[i], 'classe', self.predictions_knn[i])
			#dataframe_intermediate_range_samples.values[i][]
			#print("valor original: ")
			#print(self.test_data_set.values[list_position_intermediate_range_samples[i],len(self.test_data_set.values[i]) - 2])
			#print("valor da rna:" )
			#print(self.predictions_rna[list_position_intermediate_range_samples[i]])
		#exit()
		#print(dataframe_intermediate_range_samples)
		print(self.test_data_set)


		DataSet.saveResults( self.result_path + "final_method_classification/", self.iteration, self.test_data_set)
		del(self.test_data_set)

	def verifyClassesPredictions(self, predictions):
		sair = 0
		for i in range(0,len(predictions)):
			if (predictions[i] == 0):
				sair = 1
			elif ((predictions[i] == 1) & (sair == 1 )):
				return True
		return False

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

	def setResultPath(self, result_path):
		self.result_path = result_path

	def getTrainingTime(self):
		return self.training_time

	def getTestTime(self):
		return self.test_time

	def setLimiteFaixaSup(self, limite_faixa):
		self.limite_faixa_sup = limite_faixa

        def setLimiteFaixaInf(self, limite_faixa):
		self.limite_faixa_inf = limite_faixa
