
import sys, os
from preprocessor import Preprocessor
from dataSet import DataSet
dts = DataSet()
dts.setFilePath("experimento6/bases/sub_bases_nslkdd_12_attribute/")
#dts.setFileName("base_iris.csv")
#dts.setFileName("SmallTrainingSet.csv")
#dts.setFileName("winequality-red.csv")
#dts.setFileName("NSL_KDD-master/20PercentTrainingSet.csv")
#dts.setFileName("NSL_KDD-master/KDDTrain+binary_class.csv")
#dts.setFileName("NSL_KDD-master/SmallTrainingSet.csv")
#dts.setFileName("NSL_KDD-master/SmallTrainingSetFiveClass.csv")

#dts.setFileName("../../../KDD99/kddcup10%.csv")

dts.setFileName("NSL_KDD-master/KDDTrain+binary_class_12_attribute.csv")
#os.system('cls' if os.name == 'nt' else 'clear')

print("load data")
dts.loadData()



"""#CONFIGURACAO DO KNN
knn = KnnModule()
knn.setKNeighbors(1)
knn_classifier = KnnClassifier()
knn_classifier.setKnn(knn)


#CONFIGURACAO DO KNN CLUSTERIZADO
clustered_knn = ClusteredKnnModule()
#numero de clusters baseado na quantidade de classes
clustered_knn.setNClusters(5)
clustered_knn.setKNeighbors(1)
clustered_knn_classifier = ClusteredKnnClassifier()
clustered_knn_classifier.setKnn(clustered_knn)

#CONFIGURACAO DO KNN CLUSTERIZADO E COM DENSIDADE
clustered_density_knn = ClusteredDensityKnnModule()
#numero de clusters baseado na quantidade de classes
clustered_density_knn.setNClusters(5)
clustered_density_knn.setKNeighbors(1)
clustered_density_knn_classifier = ClusteredDensityKnnClassifier()
clustered_density_knn_classifier.setKnn(clustered_density_knn)


#CONFIGURACAO DA REDE NEURAL 
rna = RnaModule()
rna.setNumberNeuronsImputLayer(12)
#rna.setNumberNeuronsImputLayer(4)
rna.setActivationFunctionImputLayer("tanh")
rna.setImputDimNeurons(12)
#rna.setImputDimNeurons(4)
rna.setNumberNeuronsHiddenLayer(12)
rna.setActivationFunctionHiddenLayer("tanh")
rna.setNumberNeuronsOutputLayer(1)
rna.setActivationFunctionOutputLayer("tanh")
rna_classifier = RnaClassifier()
rna_classifier.setRna(rna)


#METODO HIBRIDO 
hybrid_classifier = HybridClassifier()
hybrid_classifier.setLowerThreshold(-0.8)
hybrid_classifier.setUpperThreshold(0.8)
hybrid_classifier.setRna(rna)
hybrid_classifier.setKnn(knn)


#PREPROCESSADOR PARA ATRIBUTOS CATEGORICOS
preprocessor = Preprocessor()
#preprocessor.setColumnsCategory(['protocol_type','service','flag'])
preprocessor.setColumnsCategory(['service','flag'])

evaluate = EvaluateModule()

cross = CrossValidation()

#DEFINIR A ITERACAO QUE O CROSS VALIDATION ESTA
cross.setIteration(1)

cross.setPreprocessor(preprocessor)
#cross.setFilePath("bases/sub_bases_20_nslkdd/")
#cross.setFilePath("bases/sub_bases_train+_nslkdd/")
#cross.setFilePath("bases/sub_bases_nslkdd_tcp_attribute/")
cross.setFilePath("bases/sub_bases_nslkdd_12attribute/")
#cross.setFilePath("bases/sub_bases_nslkdd_20attribute/")
#cross.setFilePath("bases/sub_bases_iris/")
#cross.setFilePath("bases/sub_bases_winequality-red/")
#cross.setFilePath("bases/sub_bases_SmallTrainingSet/")
#cross.setFilePath("bases/sub_bases_small_training_set1000/")
#cross.setFilePath("bases/sub_bases_small_training_set_five_class/")
#cross.setFilePath("bases/sub_bases/")

#cross.setClassifier(rna_classifier)
#cross.setClassifier(knn_classifier)
#cross.setClassifier(clustered_knn_classifier)
#cross.setClassifier(clustered_density_knn_classifier)
cross.setClassifier(hybrid_classifier)
cross.setEvaluateModule(evaluate)
cross.run()"""
