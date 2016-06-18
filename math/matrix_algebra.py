# Matrix Algebra
import numpy as np
A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])
############################# 1. MATRIX DIMENSIONS #############################
# dimensions ==> (# of rows, # columns)
print 'A', A.shape      # 1.1) (2x3)
print 'B', B.shape      # 1.2) (2x2)
print 'C', C.shape      # 1.3) (3x2)
print 'D', D.shape      # 1.4) (2x3)
print 'u', u.shape      # 1.5) (1x4)
print 'w', w.shape      # 1.6) (4x1)
############################# 2. VECTOR OPERATIONS #############################
alpha = 6
print u + v             # 2.1) [9 7 -4 9]
print u - v             # 2.2) [3 -3 -2 1]
print alpha*u           # 2.3) [36 12 -18 30]
print np.dot(u,v)       # 2.4) (6*3)+(2*5)+(-3*-1)+(5*4) = 51
print np.linalg.norm(u) # 2.5) sqrt(6**2 + 2**2 + (-3)**2 + 5**2) = 8.60
############################# 3. MATRIX OPERATIONS #############################
# multiplation: A*B where n col in matrix A MUST EQUAL n row in matrix B
#print A+C               # 3.1) not defined
print A - C.transpose()  # 3.2) [[-4 -7 -3]
#                               [ 3  6  4]]
#
print C.transpose()+3*D  # 3.3) [[14  3  3]
#                               [ 2  7  9]]
#
print B*A                # 3.4) [[-1 -5 -1]
#                               [ 2  7  4]]
#
#print B*A.transpose()   # 3.5) not defined
##################### 3. MATRIX OPERATIONS (OPTIONAL) ##########################
# If matrix is set as a np.matrix(), then you can use A*B
# If matrix is set as a np.array(),  then you have to use np.dot(A,B)
#print B*C               # 3.6) not defined
print C*B                # 3.7) [[ 5 -6]
#                                [ 9 -8]
#                                [ 6 -6]]
#
print B**4               # 3.8) [[ 1 -4]
#                                [ 0  1]]
#
print A*D.transpose()    # 3.9) [[14 28]
#                                [28 69]]
#
print D.transpose()*D    # 3.10) [[10 -4  0]
#                                 [-4  8  8]
#                                 [ 0  8 10]]
