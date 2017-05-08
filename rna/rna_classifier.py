from rna_module import RnaModule


class RnaClassifier(object):

	data_set = None
	test_data_set = None
	rna = None

	def __init__(self):
		print "aa"

	def run(self):
		print("RUN RNA classifier")
		self.rna.setDataSet(self.data_set)
		self.rna.setTestDataSet(self.test_data_set)

		self.rna.generateModel()
		predictions = self.rna.predict()

		print predictions


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