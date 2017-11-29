import sys, os, pandas

data_set = pandas.read_csv("bases/NSL_KDD-master/KDDTrain+binary_class.csv")
print(data_set)
a = data_set.drop(['protocol_type', 'dst_host_srv_rerror_rate', 'rerror_rate','dst_host_rerror_rate','srv_rerror_rate','duration','hot','wrong_fragment','num_compromised','num_root'],axis=1)
print(a)
a.to_csv( "KDDTrain+binary_class_20_attribute.csv", sep=',', index=False)




