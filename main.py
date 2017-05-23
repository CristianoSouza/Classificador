import numpy as np
import sys, os
from cross_validation import CrossValidation
from dataSet import DataSet
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/hybrid")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/clusteredKnn")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/rna")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/knn")

from knn_classifier import KnnClassifier
from rna_classifier import RnaClassifier
from hybrid_classifier import HybridClassifier
from clustered_knn_classifier import ClusteredKnnClassifier
from rna_module import RnaModule
from knn_module import KnnModule
from clustered_knn_module import ClusteredKnnModule

dts = DataSet()
dts.setFilePath("bases/sub_bases/")
#dts.setFileName("base_iris.csv")
#dts.setFileName("NSL_KDD-master/20PercentTrainingSet.csv")
#dts.setFileName("NSL_KDD-master/KDDTrain+.csv")
#dts.loadData()
#dts.loadResult()

#os.system('cls' if os.name == 'nt' else 'clear')

print("load data")
knn = KnnModule()
knn_classifier = KnnClassifier()
knn_classifier.setKnn(knn)

clustered_knn = ClusteredKnnModule()
clustered_knn_classifier = ClusteredKnnClassifier()
clustered_knn_classifier.setKnn(clustered_knn)

rna = RnaModule()
rna.setNumberNeuronsImputLayer(10)
rna.setActivationFunctionImputLayer("tanh")
rna.setNumberNeuronsHiddenLayer(4)
rna.setActivationFunctionHiddenLayer("tanh")
rna.setNumberNeuronsOutputLayer(1)
rna.setActivationFunctionOutputLayer("tanh")

rna_classifier = RnaClassifier()
rna_classifier.setRna(rna)

hybrid_classifier = HybridClassifier()
hybrid_classifier.setLowerThreshold(-1.2)
hybrid_classifier.setUpperThreshold(0.6)
hybrid_classifier.setRna(rna)
hybrid_classifier.setKnn(knn)

cross = CrossValidation()
#cross.setFilePath("bases/sub_bases_20_nslkdd/")
cross.setFilePath("bases/sub_bases_iris/")
#cross.setFilePath("bases/sub_bases/")

#cross.setClassifier(rna_classifier)
#cross.setClassifier(knn_classifier)
cross.setClassifier(clustered_knn_classifier)
#cross.setClassifier(hybrid_classifier)
cross.run()