import sys, os, pandas

#data_set = pandas.read_csv("bases/NSL_KDD-master/KDDTrain+binary_class_20_attribute.csv"data_set = pandas.read_csv("../KDD99CUP/KDDTrain+binary_class.csv")
data_set = pandas.read_csv("../KDDCUP99/kddcup10.csv")

lista = range(0, data_set.shape[0])

tamanho = len(lista)

print tamanho
for a in range(0,tamanho):
        if( (data_set.values[a]['classe'] == "normal.") | (data_set.values[a]['classe'] == 'normal.')):
            data_set.loc[a,'classe'] = '0'
        else:
            data_set.loc[a,'classe'] = '1'

print("saiu for")

data_set.to_csv( "../KDDCUP99/kddcup99_binary_class.csv", sep=',', index=False)




