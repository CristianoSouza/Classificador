import sys, os, pandas

data_set = pandas.read_csv("bases/NSL_KDD-master/KDDTrain+binary_class_30_attribute.csv")
#data_set = pandas.read._csv("bases/NSL_KDD-master/KDDTrain+binary_class.csv")
print(data_set)


a = data_set.drop(['duration', 'hot','su_attempted', 'num_compromised', 'protocol_type','num_access_files','dst_host_same_src_port_rate','rerror_rate','num_root','srv_rerror_rate'],axis=1)
#a = data_set.drop(['is_host_login', 'num_outbound_cmds', 'urgent','land','is_guest_login','num_shells','root_shell','srv_count','num_failed_logins','num_file_creations', 'dst_host_rerror_rate'],axis=1)
a.to_csv( "bases/NSL_KDD-master/KDDTrain+binary_class_20_attribute.csv", sep=',', index=False)




