import numpy as np
data = np.genfromtxt('faculty.csv',delimiter=',',dtype='S20,S20,S20,S20')
#####################################  Q1  #####################################
degrees = [data[i][1] for i in range(1,len(data))]
degrees = ','.join(degrees)
degrees = degrees.replace(',',' ')
degrees = degrees.replace('  ',' ')
degrees = degrees.strip()
degrees = degrees.replace('.','')
degrees = degrees.split(' ')
num_deg = len(set(degrees))
key_deg = list(set(degrees))
val_deg = [0]*num_deg
dic_deg = dict(zip(key_deg,val_deg))
for deg in degrees:
    dic_deg[deg] += 1
print '# of different degrees: {}'.format(num_deg)
print dic_deg
print
#####################################  Q2  #####################################
titles = [data[i][2].strip() for i in range(1,len(data))]
num_tit = len(set(titles))
key_tit = list(set(titles))
val_tit = [0]*num_tit
dic_tit = dict(zip(key_tit,val_tit))
for tit in titles:
    dic_tit[tit] += 1
print '# of different titles: {}'.format(num_tit)
print dic_tit
print
#####################################  Q3  #####################################
emails  = [data[i][3] for i in range(1,len(data))]
print emails
print
#####################################  Q4  #####################################
domains = []
for email in emails:
    indx = email.find('@')
    domains.append(email[indx:])
num_domain = len(set(domains))
key_domain = list(set(domains))
print '# of different e-mail domains: {}'.format(num_domain)
print key_domain
