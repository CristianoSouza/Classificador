import numpy as np
import sys, os
from cross_validation import CrossValidation
from dataSet import DataSet
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/hybrid")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/rna")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/knn")

from knn_classifier import KnnClassifier
from rna_classifier import RnaClassifier
from hybrid_classifier import HybridClassifier
from rna_module import RnaModule
from knn_module import KnnModule

dts = DataSet()
dts.setFileName("base_iris.csv")
dts.loadData()
#dts.loadResult()


print("load data")
knn = KnnModule()
knn_classifier = KnnClassifier()
knn_classifier.setKnn(knn)

rna = RnaModule()
rna.setNumberNeuronsImputLayer(4)
rna.setActivationFunctionImputLayer("tanh")
rna.setNumberNeuronsHiddenLayer(4)
rna.setActivationFunctionHiddenLayer("tanh")
rna.setNumberNeuronsOutputLayer(1)
rna.setActivationFunctionOutputLayer("tanh")

rna_classifier = RnaClassifier()
rna_classifier.setRna(rna)

cross = CrossValidation()
cross.setClassifier(rna_classifier)
#cross.setClassifier(knn_classifier)
cross.run()