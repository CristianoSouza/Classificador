from dataSet import DataSet
from preprocessor import Preprocessor


class EvaluateModule(object):

	number_false_positives = 0
	number_false_negatives = 0
	number_true_positives = 0
	number_true_negatives = 0
	classes = None
	test_data_set = None
	iteration = 0
	path = ""
	total_samples= 0
	acc_samples= 0
	err_samples=0
	tempo_execucao = 0


	def __init__(self):
		print("init")

	def run(self):
		self.number_false_positives = 0
		self.number_false_negatives = 0
		self.number_true_positives = 0
		self.number_true_negatives = 0		
		self.total_samples = 0
		self.acc_samples = 0
		self.err_samples = 0

		print("RUN evaluate method")
		result_dataframe = DataSet.loadResult(self.iteration, self.path)
	
		print(result_dataframe)

		self.classes = Preprocessor.getClassesPerColumns(self.test_data_set,'classe')

		acc_classes = []
		err_classes = []
		print(self.test_data_set.values)
		print(result_dataframe.values)
		print(len(self.test_data_set.values))
		#exit()
		if(len(self.classes) <=2 ):
			posicao_classe = len(result_dataframe.values[0]) -2
			for i in range(0,len(result_dataframe.values)):
				self.total_samples+= 1
				print("Real: " + str(self.test_data_set.values[i,posicao_classe]) + " -- predito: " + str(result_dataframe.values[i,posicao_classe]))
				if(self.test_data_set.values[i,posicao_classe] == '0' or self.test_data_set.values[i,posicao_classe] == 0 ):
					if (result_dataframe.values[i,posicao_classe] == 0 or result_dataframe.values[i,posicao_classe] == '0'):
						#print("FALSO E CLASSIFICOU COMO FALSO")
						self.number_true_negatives+=1
						self.acc_samples+=1
					else:
						#print("FALSO E CLASSIFICOU COMO VERDADEIRO")
						self.number_false_positives+=1
						self.err_samples+=1 

				elif(self.test_data_set.values[i,posicao_classe] == '1' or self.test_data_set.values[i,posicao_classe] == 1):
					if (result_dataframe.values[i,posicao_classe] == 1 or result_dataframe.values[i,posicao_classe] == '1'):
						#print("VERDADEIRO E CLASSIFICOU COMO VERDADEIRO")
						self.number_true_positives+=1
						self.acc_samples+=1
					else:
						#print("VERDADEIRO E CLASSIFICOU COMO FALSO")
						self.number_false_negatives+=1
						self.err_samples+=1 

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
		else:
			posicao_classe = len(result_dataframe.values[0]) -2
			arquivo = open('results/' + self.path + 'final_info_' + str(self.iteration) + '.txt', 'w') 
			texto = """		MATRIZ DE CONFUSAO
	             Predicao      
			 ACC    ERR  
|--------||--------|

"""	
			for i in range(0,len(self.classes)):
				acc_classes.append(0)
				err_classes.append(0)
			for i in range(0,len(result_dataframe.values)):
				print(self.test_data_set.values[i,posicao_classe])
				print(result_dataframe.values[i,posicao_classe])
				#exit()
				self.total_samples+= 1
				print("Real: " + str(self.test_data_set.values[i,posicao_classe]) + " -- predito: " + str(result_dataframe.values[i,posicao_classe]))

				if(self.test_data_set.values[i,posicao_classe] == "normal"):
					if (result_dataframe.values[i,posicao_classe] ==  "normal"):
						acc_classes[0]+=1
						self.acc_samples+=1
					else:
						err_classes[0]+=1
						self.err_samples+=1 
				elif(self.test_data_set.values[i,posicao_classe] != "normal"):
					if(result_dataframe.values[i,posicao_classe] != "normal"):
						acc_classes[1]+=1
						self.acc_samples+=1
					else:
						err_classes[1]+=1
						self.err_samples+=1 

			for i in range(0,len(acc_classes)):		
				texto+=  """ 	|   """ + str(acc_classes[i]) + """    || 	""" + str(err_classes[i]) + """ | 		
|--------||--------|
"""

		texto+= """TOTAL DE EXEMPLOS: """ + str(self.total_samples) + """ 	|   
|--------||--------|
"""
		texto+= """TOTAL DE EXEMPLOS CORRETOS: """ + str(self.acc_samples) + """ 	|   
|--------||--------|
"""
		texto+= """TOTAL DE EXEMPLOS ERRADOS: """ + str(self.err_samples) + """ 	|   
|--------||--------|
"""
		texto+= """PORCENTAGEM ACERTOS: """ + str((100/float(self.total_samples)) * self.acc_samples) + """ 	|   
|--------||--------|
"""
		texto+= """PORCENTAGEM ERROS: """ + str((100/float(self.total_samples)) * self.err_samples) + """ 	|   
|--------||--------|
"""			
		texto+="""TEMPO DE EXECUCAO: """ + str(self.tempo_execucao) + """  ||| """
		arquivo.write(texto) 
		arquivo.close()
		'''
		posicao_classe = len(result_dataframe.values[0]) -2
		arquivo = open('results/' + self.path + 'final_info_' + str(self.iteration) + '.txt', 'w') 
		texto = """		MATRIZ DE CONFUSAO
             Predicao      
		 ACC    ERR  
|--------||--------|
"""

		for i in range(0,len(self.classes)):
			acc_classes.append(0)
			err_classes.append(0)
		for i in range(0,len(result_dataframe.values)):
			print(self.test_data_set.values[i,posicao_classe])
			print(result_dataframe.values[i,posicao_classe])
			#exit()
			self.total_samples+= 1
			for j in range(0,len(self.classes)):
				print("Real: " + str(self.test_data_set.values[i,posicao_classe]) + " -- predito: " + str(result_dataframe.values[i,posicao_classe]))
				if(self.test_data_set.values[i,posicao_classe] == self.classes[j]):
					if (result_dataframe.values[i,posicao_classe] ==  self.classes[j]):
						#print("ACERTOU")
						acc_classes[j]+=1
						self.acc_samples+=1
					else:
						#print("ERROUUU!")
						err_classes[j]+=1
						self.err_samples+=1 

		for i in range(0,len(acc_classes)):		
			texto+= str(self.classes[i]) + """ 	|   """ + str(acc_classes[i]) + """    || 	""" + str(err_classes[i]) + """ | 		
|--------||--------|
"""
	texto+= """TOTAL DE EXEMPPLOS: """ + str(self.total_samples) + """ 	|   
|--------||--------|
"""
	texto+= """TOTAL DE EXEMPPLOS CORRETOS: """ + str(self.acc_samples) + """ 	|   
|--------||--------|
"""
	texto+= """TOTAL DE EXEMPPLOS ERRADOS: """ + str(self.err_samples) + """ 	|   
|--------||--------|
"""
	texto+= """PORCENTAGEM ACERTOS: """ + str((100/float(self.total_samples)) * self.acc_samples) + """ 	|   
|--------||--------|
"""
	texto+= """PORCENTAGEM ERROS: """ + str((100/float(self.total_samples)) * self.err_samples) + """ 	|   
|--------||--------|
"""
	'''
	
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

	def getNumberTrueNegatives(self):
		return self.number_true_negatives

	def setIteration(self, iteration):
		self.iteration = iteration

	def setClasses(self, classes):
		self.classes = classes

	def getClasses(self):
		return self.classes

	def setTempoExecucao(tempo_execucao):
		self.tempo_execucao = tempo_execucao
