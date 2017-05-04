import numpy as np
import sys, os
from cross_validation import CrossValidation
from dataSet import DataSet
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/rna")
from rna_classifier import RnaClassifier


#dts = DataSet("base_iris.csv")
#dts.load_data()

print("load data")

cross = CrossValidation()

#for i_fold in range(0,10):

#	sub_data_set = dts.load_sub_data_set("sub_data_set_" + str(i_fold+1 ) + ".csv")

#	print(sub_data_set[:,1:])

	#rna = RnaModule(dts.get_data_set(), sub)

	#knn = KnnModule(dts.get_data_set(), dts.get_test_data_set())