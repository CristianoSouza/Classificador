import sys, os, pandas
from cross_validation import CrossValidation
from preprocessor import Preprocessor
from dataSet import DataSet

data_set = pandas.read_csv("bases/KDD99/teste.csv")

lista = range(0, data_set.shape[0])

tamanho = len(lista)
print lista
print(data_set.values[5])
for a in range(0,tamanho):
	if ((data_set.values[a][41] == 'smurf.') | (data_set.values[a][41] == "smurf.")):
		print("smurfff")
		print(data_set.values[a][41])
		data_set.loc[a, 'classe'] = '1'	
		print(data_set.values[a][41])	
	else:
		print(data_set.values[a][41])





