import numpy as np
import math

def forward_substitution(L, b):
  n = len(L)
  x = np.zeros(n)
  x[0] = b[0] / L[0,0]
  for i in range(n):
    temp = b[i]
    for j in range(i):
      temp = temp - (L[i,j] * x[j])
    x[i] = temp / L[i,i]
    #print(x)
  return x 

def backward_substitution(U, b):
  n = len(U)
  x = np.zeros(n)
  for i in range(n-1, -1, -1):
      temp = b[i]
      for j in range(i+1, n):
          temp -= U[i,j] * x[j]
      x[i] = round(temp / U[i,i],3)
    #print(x)
  return x
  
  #seperation of L
def extractL(compressed):
  n = len(compressed)
  L = np.identity(n) #identity --> diagonals = 1
  for i in range(1,n):
    for j in range(0,i):
      #print(compressed[i,j])
      L[i,j] = float(compressed[i,j])
  return L

  #separation of U
def extractU(compressed):
  n = len(compressed)
  U = np.zeros((n, n))
  for i in range(0,n-1):
    for j in range(i+1,n):
      U[i,j] = compressed[i,j]
    #set diagonal elements
  for i in range(0,n):
    U[i,i] = compressed[i,i]
  return U

 #doolittle method
def doolittle(A, b):
  n = len(A)
  U = np.zeros((n, n)) #set U to zeros
  L = np.identity(n) #set L to identity matrix of same length as A

  for i in range(n-1):
    #partial pivoting
    maxelement=max(A[:,i],key=abs)  #max element in col#i
    if (A[i,i])!=maxelement: #max element of col #i is not the one in the diagonal,pivoting is needed
      for k in range(i+1,n):
        if np.abs(A[k,i])>np.abs(A[i,i]):
          A[[i,k]]=A[[k,i]]             # Swaps ith and kth rows to each other
          b[[i,k]]=b[[k,i]] 

      #decomposing A to copmact representaion
    for k in range(i+1,n):          
      A[k,i] = A[k,i]/A[i,i]      
      for j in range(i+1,n):      
        A[k,j] -= A[k,i]*A[i,j] 
    #extract A to L,U and solve by forward then backward substition
  L = extractL(A)
  U = extractU(A)
  #Ld=b
  d = forward_substitution(L, b)
  #Ux=d
  x = backward_substitution(U, d)
  return L, U, x

def crout(A, b):
  n = len(A)
  L = np.zeros((n, n)) #set L to zeros
  U = np.identity(n) #set U to indentity matrix of same length as A

  for i in range(0, n):
    #setting L matrix
      for j in range(i, n):
        summationL = 0
        for s in range(0,j):
          summationL += L[j, s] * U[s, i]
        L[j, i] = A[j, i] - summationL
    #setting U matrix
      for j in range(i+1, 3):
        summationU = 0
        for s in range(0,i):
          summationU += L[i, s] * U[s, j]
        U[i, j] = (A[i, j] - summationU) / L[i, i]

  d = forward_substitution(L,b)
  x = backward_substitution(U,d) #final solution
  return L, U, x

def chelosky(A, b):
  n = len(A)
  L = np.zeros((n, n)) #set L to zeros of same length as A
  for j in range(n): #cols
    for i in range(j,n): #rows
      if(i==j): #diagonal
        summation = 0
        for k in range(j):
          summation+= L[i,k]**2
        L[i,j] = np.sqrt(A[i,j]-summation)
      else: #others
        summation = 0
        for k in range(j):
          summation += L[i,k]*L[j,k]
        L[i,j] = (A[i,j] - summation) / L[j,j]
  U = L.transpose() #set U to L transpose
  d = forward_substitution(L, b)
  x = round(backward_substitution(U, d),3) #final solution
  return L, U, x;