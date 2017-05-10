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
		data_set = []
		data_set_posicoes = []
		for i in range(0,10):
			sub_data_set = []
			posicoes = random.sample(lista,self.partition_size)

			for a in range(0, len(self.dataframe_data_set.values)):
				self.dataframe_data_set.set_value(a,'posicaoOriginal', a)

			for j in range(0,len(posicoes)):
				lista.remove(posicoes[j])
				sub_data_set.append(self.dataframe_data_set.values[posicoes[j],:])

			data_set.append(sub_data_set)
			data_set_posicoes.append(posicoes)
			print('values:', data_set[i])
		print('posicoes:', data_set_posicoes)
		return data_set, data_set_posicoes

	def partitionDataSet(self):
		print('Quatidade de exemplos:', self.dataframe_data_set.shape[0])
		self.partition_size = (self.dataframe_data_set.shape[0] / 10)
		print('10 Particoes de tamanho: ', self.partition_size)	

		examples, examples_posicoes = self.selectExamples()

		for i in range(0,10):
			print('------------')	
			print('Particao ', i )
			sub_dataframe = pandas.DataFrame(
				data= examples[i],
				#index=range((i*self.partition_size),((i*self.partition_size) + self.partition_size) ), 
				index= range(0,len(examples[i])),
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

	@classmethod
	def loadSubDataSet(self, file_name):
		sub_dataframe_data_set = pandas.read_csv("bases/sub_bases/" + file_name)
		return sub_dataframe_data_set

	@classmethod
	def concatSubDataSet(self, data_frame1, data_frame2):
		frames = [data_frame1, data_frame2]
		return pandas.concat(frames)

	def loadResult(self):
		a = pandas.read_csv("bases/sub_bases/sub_data_set_10.csv")
		print(a.values) 

	@classmethod
	def saveResults(self, method, iteration, data_frame):
		file_path = "results/" + method + "/"

		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			print("nao existe")
			os.makedirs(directory)
		else:
			print("exists")	

		data_frame.to_csv( file_path + "cross_" + str(iteration) + "_final_result.csv", sep=',')





 