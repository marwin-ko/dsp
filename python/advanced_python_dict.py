import numpy as np
data = np.genfromtxt('faculty.csv',delimiter=',',dtype='S20,S20,S20,S20')
info = [[data[i][1],data[i][2],data[i][3]] for i in range(1,len(data))]
names = [data[i][0] for i in range(1,len(data))]
#####################################  Q6  #####################################
last_name = [name.split(' ')[-1] for name in names]
faculty_dict = dict(zip(last_name,info))
print 'Question #6', faculty_dict
print
#####################################  Q7  #####################################
full_name = [(name.split(' ')[0],name.split(' ')[-1]) for name in names]
faculty_dict = dict(zip(full_name,info))
print 'Question #7', faculty_dict
print
#####################################  Q8  #####################################
sort_last = sorted(full_name, key=lambda x:x[-1] )
for name in sort_last:
    print name,':',faculty_dict[name]
