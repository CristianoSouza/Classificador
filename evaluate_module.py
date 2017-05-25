from dataSet import DataSet

class EvaluateModule(object):

	number_false_positives = 0
	number_false_negatives = 0
	number_true_positives = 0
	number_true_negatives = 0

	test_data_set = None
	iteration = 0
	path = ""


	def __init__(self):
		print("init")

	def run(self):
		self.number_false_positives = 0
		self.number_false_negatives = 0
		self.number_true_positives = 0
		self.number_true_negatives = 0		
		print("RUN evaluate method")
		result_dataframe = DataSet.loadResult(self.iteration, self.path)
		print(result_dataframe)
		posicao_classe = len(result_dataframe.values[0]) -2
		for i in range(0,len(result_dataframe.values)):
			#print("Real: " + str(self.test_data_set.values[i,posicao_classe]) + " -- predito: " + str(result_dataframe.values[i,posicao_classe]))
			if(self.test_data_set.values[i,posicao_classe] == 0):
				if (result_dataframe.values[i,posicao_classe] == 0):
					#print("FALSO E CLASSIFICOU COMO FALSO")
					self.number_true_negatives+=1
				else:
					#print("FALSO E CLASSIFICOU COMO VERDADEIRO")
					self.number_false_positives+=1

			elif(self.test_data_set.values[i,posicao_classe] == 1):
				if (result_dataframe.values[i,posicao_classe] == 1):
					#print("VERDADEIRO E CLASSIFICOU COMO VERDADEIRO")
					self.number_true_positives+=1
				else:
					#print("VERDADEIRO E CLASSIFICOU COMO FALSO")
					self.number_false_negatives+=1

		arquivo = open('results/' + self.path + 'final_info_' + str(self.iteration) + '.txt', 'w') 
		texto = """		MATRIZ DE CONFUSAO
             Predicao      
		 ATAQUE    NORMAL  
	   |--------||--------|
ATAQUE |   """ + str(self.number_true_positives) + """    ||   """+ str(self.number_false_negatives) + """    |
	   |--------||--------|
NORMAL |   """+ str(self.number_false_positives) + """    ||   """+ str(self.number_true_negatives) + """    |
	   |--------||--------|
		"""
		arquivo.write(texto) 
		arquivo.close()

	def setTestDataSet(self, test_data_set):
		self.test_data_set = test_data_set

	def setPath(self, path):
		self.path = path

	def setNumberFalsePositives(self, number_false_positives):
		self.number_false_positives = number_false_positives

	def getNumberFalsePositives(self):
		return number_false_positives

	def setNumberFalseNegatives(self, number_false_negatives):
		self.number_false_negatives = number_false_negatives

	def getNumberFalseNegatives(self):
		return number_false_negatives

	def setNumberTruePositives(self, number_true_positives):
		self.number_true_positives = number_true_positives

	def getNumberTruePositives(self):
		return number_true_positives

	def setNumberTrueNegatives(self, number_true_negatives):
		self.number_true_negatives = number_true_negatives

	def setNumberTrueNegatives(self):
		return number_true_negatives

	def setIteration(self, iteration):
		self.iteration = iteration
