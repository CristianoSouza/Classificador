import numpy as np
import pandas
import os
from sklearn import neighbors
from sklearn.cluster import MiniBatchKMeans

class ClusteredKnnModule(object):
	data_set_samples = []
	data_set_labels = []
	test_data_set_samples = []
	test_data_set_labels = []
	distance = []
	clusters = []
	indices = []
	k_neighbors = 5

	def __init__(self):
		print("init knn module")

	def run(self):
		print(self.data_set_samples[0])
		#exit()
		self.findClusters()
		self.findNearestNeighbors()
		print(self.distance)

		clf = neighbors.KNeighborsClassifier(self.k_neighbors, weights='distance')
		clf.fit(self.data_set_samples, self.data_set_labels)

		predictions = clf.predict(self.test_data_set_samples)
		return predictions

	def findClusters(self):
		kmeans = MiniBatchKMeans(n_clusters=2, random_state=0).fit(self.data_set_samples)
		for i in range(0,10):
			print(kmeans.labels_[i])
		#print(kmeans.labels_)
		predicao = kmeans.predict(self.data_set_samples)
		print(predicao)
		print("Centros de cluster")
		print(kmeans.cluster_centers_)
		distance_clusters = kmeans.fit_transform(self.data_set_samples)

		print("Preparando clusters...")
		print( len(kmeans.cluster_centers_))
		for i in range(0, len(kmeans.cluster_centers_)):
			print(i)
			self.clusters.append([])
			self.indices.append([])

		print(self.clusters)
		for i in range(0,len(self.data_set_samples)):
			dist = 0
			for j in distance_clusters[i]:
				dist+= j 
			self.distance.append(dist)

			self.indices[kmeans.labels_[i]].append(i)
			self.clusters[kmeans.labels_[i]].append(self.data_set_samples[i]) 

		print(self.distance)
		print(self.clusters)

	def findNearestNeighbors(self):
		print("Procurando distancia para vizinho mais proximo...")
		print(len(self.clusters))
	 	for i in range(0, len(self.clusters)):
			clf = neighbors.NearestNeighbors(n_neighbors=2)
			print("Cluster:")
			print(self.clusters[i])
			clf.fit(self.clusters[i])
			for j in  range(0, len(self.clusters[i])):
				print("Exemplo: ", self.clusters[i][j])
				print("original", self.data_set_samples[self.indices[i][j]])
				neighbor = clf.kneighbors(self.clusters[i][j], return_distance=True)
				print("distancia neighbor", neighbor[0][0][1])
				print(self.indices[i][j])
				self.distance[self.indices[i][j]]+= neighbor[0][0][1]

		print(self.distance)
		exit()

	def setDataSetClustering(self, data_set):
		self.data_set_samples = data_set.values[:,0:(len(data_set.values[0])-1)]
		print(self.data_set_samples)

	def setDataSet(self, data_set):
		self.data_set_samples = data_set.values[:,0:(len(data_set.values[0])-2)]
		self.data_set_labels = data_set.values[:,(len(data_set.values[0])-2)]
		#print(self.data_set_samples)
		#print(self.data_set_labels)
	
	def setTestDataSet(self, test_data_set):
		self.test_data_set_samples = test_data_set.values[:,0:(len(test_data_set.values[0])-2)]
		self.test_data_set_labels = test_data_set.values[:,(len(test_data_set.values[0])-2)]		
		#print(self.test_data_set_samples)
		#print(self.test_data_set_labels)	

	def setKNeighbors(self, k_neighbors):
		self.k_neighbors = k_neighbors

	def getKNeighbors(self):
		return self.k_neighbors