
class EvaluateModule(object):

	number_false_positives = 0
	number_false_negatives = 0
	number_true_positives = 0
	number_true_negatives = 0

	def __init__(self):
		print("init")

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