from rna_module import RnaModule
import pandas

class RnaClassifier(object):

	data_set = None
	test_data_set = None
	rna = None
	predictions = None
	iteration = 0

	def __init__(self):
		print "aa"

	def run(self):
		print("RUN RNA classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)

		self.rna.generateModel()
		self.predictions = self.rna.predictClasses()
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

		file_path = "results/rna/"

		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			print("nao existe")
			os.makedirs(directory)
		else:
			print("exists")	

		self.test_data_set.to_csv("results/rna/cross_" + str(self.iteration) + "_final_result.csv", sep=',')

	def setDataSet(self, data_set):
		self.data_set = data_set

	def getDataSet(self):
		return self.data_set

	def setTestDataSet(self, test_data_set):
		self.test_data_set = test_data_set

	def getTestDataSet(self):
		return self.test_data_set

	def setRna(self, rna):
		self.rna = rna

	def getRna(self):
		return self.rna

	def setIteration(self, iteration):
		self.iteration = iteration