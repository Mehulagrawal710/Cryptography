import numpy
import math
from numpy import matrix
from numpy import linalg

def modMatInv(A,p):
    n=len(A)
    A=matrix(A)
    adj=numpy.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
    return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):
    for i in range(1,p):
        if (i*a)%p==1:
            return i
    raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):
    A=numpy.array(A)
    minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
    p=0
    for s in range(0,len(minor)):
        if p==i:
            p=p+1
        q=0
        for t in range(0,len(minor)):
            if q==j:
                q=q+1
            minor[s][t]=A[p][q]
            q=q+1
        p=p+1
    return minor