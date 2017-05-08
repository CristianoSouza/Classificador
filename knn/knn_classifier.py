from knn_module import KnnModule
import pandas
import os

class KnnClassifier(object):

	data_set = None
	test_data_set = None
	predictions = []

	knn = None

	def __init__(self):
		print "Knn classifier"

	def run(self):
		print "RUN Knn classifier"
		self.knn.setDataSet(self.data_set)
		self.knn.setTestDataSet(self.test_data_set)
		self.predictions = self.knn.run()
		print("Predicao knn: ") 
		print(self.predictions)
		self.saveResults()

	def saveResults(self):
		print(self.test_data_set.values[:,len(self.test_data_set.values[1,:])-2])
		print(self.test_data_set)

		print(self.predictions)

		self.predictions[4] = 5
		print(self.predictions)

		for i in range(0,len(self.predictions)):
			self.test_data_set.set_value(i,'classe',self.predictions[i])

		print(self.test_data_set)

		file_path = "results/knn/"

		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			print("nao existe")
			os.makedirs(directory)
		else:
			print("exists")	

		self.test_data_set.to_csv("results/knn/cross_" + str(self.iteration) + "_final_result.csv", sep=',')

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

	def setIteration(self, iteration):
		self.iteration = iteration