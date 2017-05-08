import numpy as np
import pandas 
from sklearn import neighbors

class KnnModule(object):
	data_set_samples = []
	data_set_labels = []
	test_data_set_samples = []
	test_data_set_labels = []
	k_neighbors = 1

	def __init__(self):
		print("init knn module")

	def run(self):
		for weights in ['uniform', 'distance']:
   	 		# we create an instance of Neighbours Classifier and fit the data.
    		clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
			#clf = neighbors.KNeighborsClassifier(self.k_neighbors, weights='uniform')
    		#aa.fit(self.data_set_samples, self.data_set_labels)
    		predictions = clf.predict(self.test_data_set_samples)
    		print(clf.score(self.test_data_set_samples,self.test_data_set_labels))

	def setDataSet(self, data_set):
		self.data_set_samples = data_set.values[:,0:(len(data_set.values[0])-1)]
		self.data_set_labels = data_set.values[:,(len(data_set.values[0])-1)]
		#print(self.data_set_samples)
		#print(self.data_set_labels)
	
	def setTestDataSet(self, test_data_set):
		self.test_data_set_samples = test_data_set.values[:,0:(len(test_data_set.values[0])-1)]
		self.test_data_set_labels = test_data_set.values[:,(len(test_data_set.values[0])-1)]		
		#print(self.test_data_set_samples)
		#print(self.test_data_set_labels)		

	def setKNeighbors(self, k_neighbors):
		self.k_neighbors = k_neighbors

	def getKNeighbors(self):
		return self.k_neighbors