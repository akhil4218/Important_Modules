import numpy as np

#   Reasones why we use numpy already we are having lists
#                        1.consumes less memory 2.fast 3 easy to use


#  sys.getsizeof(list)*len(list)  prints list size
#  b.size*b.itemsize   if b is numpy list


#a=np.array([(1,2,3),(5,6,7)])
#    b=np.array([(11,22,33),(55,566,777),(505,506,707)])

#  a+b will print each elemnt addition with its respective
#similarly -,*,/ does
# np.sqrt(array) will print each  sqrt element
#  np.std(array)  for standard deviation
#print(np.exp(a))  #exponential values
#print(np.log10(a)) #  prints log to  base (10)  u can change this num    
#np.size(element) will print total array size
#  a.shape will give shape
#  a.reshape((b,a)) if u r having a-rows b-coloums it  will swap  b-rows and a-coloumns

#print(a.ravel())   #  will print(1,2,3,5,6,7)
#  print(a[0]) will print (1,2,3)

#  a.max() a.min()  a.sum()
#print(a.sum(axis=0))   #  wil print 6,8,10   1+5,2+6,3+7
#print(a.sum(axis=1))   # will print  6,18  3+2+1,5+6+7
#print(np.vstack((a,b)))

# above will print [[  1   2   3]
 #                  [  5   6   7] it will ad  all lists vertically
 #                  [ 11  22  33]
 #                  [ 55 566 777]
 #                  [505 506 707]]
# print(np.hstack((a,b)))  #[[  1   2   3  11  22  33] if u erase 3 rd list inb
 #                         [  5   6   7  55 566 777]] horizontal concatination
#print(a[0:2])  #will print (1,2,3),(5,6,7)

#print(a[0:1])  # will print (1,2,3)

#print(a[0:,2])  #  will print (3,7)  beacause it is in 0,1 th row 2 nd elements

#print(a[0,2])   #will print  0 th row 2 nd elemnet

#print(b[0:2,2])   #it will print  33,777  it includes only 2 rows of having 2nd position

#print(np.linspace(2,6,10))  #it will print all numbers between 2,6  10 numbers

#print(a.reshape(3,2))

#print(a.shape)

#print(np.sqrt(a))


#print(np.size(b))


#print(a+b)
#size=10000000

#l1=range(size)
#l2=range(size)

#a1=np.arange(size)
#a2=np.arange(size)

# a.ndim to know which dimwnsional it is
# a.dtype to know which type it is
# a.itemssize to find size of each element

#start=time.time()

#result=[(x,y) for x,y in zip(l1,l2)]

#print((time.time()-start)*1000)

#start1=time.time()

#result1=a1+a2

#print((time.time()-start1)*1000)

#print(np.zeros(2))   #will print 2 zeros
#print(np.zeros((2,4))) # will print 2 sets of four zero sets
#print(np.ones(2))  # similarly
#print(np.logspace(2,10,10))   # returns similarly linspace way but returns log values

#print(a.flatten())   # same as ravel()

"""
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[11,12,13],[14,15,16],[17,18,19]])
#print(np.dot(a,b))    #for multiplication of matrices
A=np.matrix(a)
#print(a*b) #just to multilpy only values 1*11   2*12  ...
#print("===============")
#print(a)
#print(np.multiply(a,a))   #to print squares of matrix

#print(np.r_[:11])   # top print a row matrix of 0-10
#print(np.r_["c",:12])   #to print coloumn matrix 0-11  to print row change it to "r"
#print(np.eye(6))
""" """
[[1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]]
 """  """  """
#print(np.diag([3,4,5]))   # prints 3 rows and 3 columns with diagonal elemnts 3,4,5

#print(np.random.randint(2,9,(3,3)))   # prints random numbers

"""
import numpy.linalg as linalg
a=np.array([[1,2,33],[3,55,4]])
#print(a)
#print(linalg.pinv(a))   #  print   ssomething
#print(linalg.inv(a))
data=np.random.randn(2,2000)
np.save("save.java",data)     ## save an array into binary file in .npy format


da=np.load("save.npy")
#print(da)
import scipy.io
scipy.io.savemat("pop.txt",{"data":data})   # saves in microst office file
ss=scipy.io.loadmat("pop.txt")
print(ss)

#to transpose     -->  a.T
"""


#to resize the shape
#np.resize(a,(4,4))
"""
a=np.arange(10)**2
b=np.array([[1,2],[3,4]])
print(a[b])   #  prints   [[1,4],[9,16]]

"""
"""
palette = np.array( [ [0,0,0],                # black
                       [255,5,0],              # red
                       [0,255,0],              # green
                       [0,0,255],              # blue
                       [255,255,255] ] )       # white
image = np.array( [ [ 0, 4, 2, 4 ],           # each value corresponds to a color in the palette
                     [ 0, 3, 4, 0 ]  ] )
print(palette[image])

"""













