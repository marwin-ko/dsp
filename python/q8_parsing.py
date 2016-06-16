# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import numpy as np
data = np.genfromtxt('football.csv',delimiter=',',dtype='S15,int,int,int,int,int,int,int')
temp = []
for i,x in enumerate(data):
    info = (x[0],x[5]-x[6])
    temp.append(info)
temp = sorted(temp,key=lambda x:x[1])
print 'The team with the smallest point differential is',temp[0][0]
