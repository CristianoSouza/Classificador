import pandas
import os
import random

class DataSet(object):

	file_name = ""
	test_file_name = ""
	dataframe_data_set = []
	partition_size = 0

	def __init__(self):
		print "init"

	def setFileName(self, file_name):
		self.file_name = file_name

	def loadData(self):
		self.dataframe_data_set = pandas.read_csv("bases/" + self.file_name)
		self.partitionDataSet()

	def getDataSet(self):
		return self.data_set

	def selectExamples(self):
		lista = range(0, self.dataframe_data_set.shape[0])

		tamanho = len(lista)
		print lista
		'''for a in range(0,tamanho):
			#self.dataframe_data_set.scdet_value(a,'po', 15)
			self.dataframe_data_set.loc[a, 'posicaoOriginal'] = a


		print("saiu for")
'''
		file_path = "bases/sub_bases/"

		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			print("nao existe")
			os.makedirs(directory)
		else:
			print("exists")	

		data_set = []
		data_set_posicoes = []
		len_attributes = len(self.dataframe_data_set.values[0,:])
		for i in range(0,10):
			sub_data_set = []
			posicoes = random.sample(lista,self.partition_size)
			len_posicoes = len(posicoes)
			print(i)

			arquivo = open("bases/sub_bases/sub_data_set_" + str(i+1) + ".csv", 'w') 
			for k in range(0,len(self.dataframe_data_set.columns)):
				texto = str(self.dataframe_data_set.columns[k])
				arquivo.write(texto) 
				if(k+1 < len(self.dataframe_data_set.columns)):
					arquivo.write(""",""") 
				else:
					arquivo.write("""
""")	
			arquivo.close()

			for j in range(0,len_posicoes):
				lista.remove(posicoes[j])
				texto = ""
				print(str(i) + " - " + str(j))
				for k in range(0,len_attributes):
					texto += str(self.dataframe_data_set.values[posicoes[j],k])
					if(k+1 < len_attributes):
						texto += ""","""
					else:
						texto +="""
""" 
				arquivo = open("bases/sub_bases/sub_data_set_" + str(i+1) + ".csv", 'w') 
				arquivo.write(texto) 
				arquivo.close()
				#sub_data_set.append(self.dataframe_data_set.values[posicoes[j],:])
				#print(sub_data_set)


			'''sub_dataframe = pandas.DataFrame(
				data= sub_data_set,
				#index=range((i*self.partition_size),((i*self.partition_size) + self.partition_size) ), 
				index= range(0,len(sub_data_set)),
				columns= self.dataframe_data_set.columns )
				
			print(sub_dataframe)
			print()
			file_path = "bases/sub_bases/"

			directory = os.path.dirname(file_path)
			if not os.path.exists(directory):
				print("nao existe")
				os.makedirs(directory)
			else:
				print("exists")	

			sub_dataframe.to_csv("bases/sub_bases/sub_data_set_" + str(i+1) + ".csv", sep=',')
'''
	def partitionDataSet(self):
		print('Quatidade de exemplos:', self.dataframe_data_set.shape[0])
		self.partition_size = (self.dataframe_data_set.shape[0] / 10)
		print('10 Particoes de tamanho: ', self.partition_size)	

		self.selectExamples()

	@classmethod
	def loadSubDataSet(self, file_name):
		sub_dataframe_data_set = pandas.read_csv("bases/sub_bases/" + file_name)
		return sub_dataframe_data_set

	@classmethod
	def concatSubDataSet(self, data_frame1, data_frame2):
		frames = [data_frame1, data_frame2]
		return pandas.concat(frames)

	@classmethod
	def loadResult(self, iteration, path):
		return pandas.read_csv("results/" + path + "cross_" + str(iteration) + "_final_result.csv")

	@classmethod
	def saveResults(self, method, iteration, data_frame):
		file_path = "results/" + method + "/"

		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			print("nao existe")
			os.makedirs(directory)
		else:
			print("exists")	

		data_frame.to_csv( file_path + "cross_" + str(iteration) + "_final_result.csv", sep=',', index=False)





 