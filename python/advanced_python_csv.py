import numpy as np
import csv
data = np.genfromtxt('faculty.csv',delimiter=',',dtype='S20,S20,S20,S20')
emails  = [data[i][3] for i in range(1,len(data))]
with open('emails.csv','wb') as f:
    w = csv.writer(f)
    for email in emails:
        w.writerow([email])
