import numpy as np
import math

def forward_substitution(L, b, sigFigs):
  n = len(L)
  x = np.zeros(n)
  x[0] = b[0] / L[0,0]
  for i in range(n):
    temp = b[i]
    for j in range(i):
      temp = temp - (L[i,j] * x[j])
    x[i] = round(temp / L[i,i], sigFigs)
    #print(x)
  return x 

def backward_substitution(U, d, sigFigs):
  n = len(U)
  x = np.zeros(n)
  for i in range(n-1, -1, -1):
      temp = d[i]
      for j in range(i+1, n):
          temp -= U[i,j] * x[j]
      x[i] = round(temp / U[i,i], sigFigs)
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
def doolittle(A, b,sigFigs, unknownsNumber):
  startTime=time.time()
  n = len(A)
  U = np.zeros((n, n)) #set U to zeros
  L = np.identity(n) #set L to identity matrix of same length as A
  #consistency attributes
  augB = b.reshape(-1,1)
  Aug = np.append(A,augB, axis=1)
  rankA = np.linalg.matrix_rank(A) 
  rankAug=np.linalg.matrix_rank(Aug) 
  #consistency check
  if(rankA!=rankAug):
    end = time.time()    
    runTime = end - startTime
    return 1,0,0,"System is inconsistent and there is no solution",runTime
  elif(rankA==rankAug<unknownsNumber):
    end = time.time()    
    runTime = end - startTime
    return 1,0,0,"System has infinite number of solutions",runTime
  else: #unique consistent system
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
        A[k,i] = round(A[k,i]/A[i,i], sigFigs)      
        for j in range(i+1,n):      
          A[k,j] -= round(A[k,i]*A[i,j], sigFigs) 
    #extract A to L,U and solve by forward then backward substition
    L = extractL(A)
    U = extractU(A)
    
    #Ld=b
    d = forward_substitution(L, b,sigFigs)
    #Ux=d
    x = backward_substitution(U, d,sigFigs)
    end = time.time()    
    runTime = end - startTime
    return 0, L, U, x, runTime

def crout(A, b, sigFigs, unknownsNumber):
  startTime=time.time()
  n = len(A)
  L = np.zeros((n, n)) #set L to zeros
  U = np.identity(n) #set U to indentity matrix of same length as A
  #consistency attributes
  augB = b.reshape(-1,1)
  Aug = np.append(A,augB, axis=1)
  rankA = np.linalg.matrix_rank(A) 
  rankAug=np.linalg.matrix_rank(Aug) 
  #consistency check
  if(rankA!=rankAug):
    end = time.time()    
    runTime = end - startTime
    return 1,0,0,"System is inconsistent and there is no solution",runTime
  elif(rankA==rankAug<unknownsNumber):
    end = time.time()    
    runTime = end - startTime
    return 1,0,0,"System has infinite number of solutions",runTime
  else: #unique consistent system
    for i in range(0, n):
      #setting L matrix
        for j in range(i,n):
          summationL = 0
          for k in range(0,j):
            summationL += L[j,k] * U[k,i]
          L[j,i] = A[j,i] - summationL
          L[j,i] = round(L[j,i], sigFigs)
      #setting U matrix
        for j in range(i+1,n):
          summationU = 0
          for k in range(0,i):
            summationU += L[i,k] * U[k,j]
          U[i,j] = (A[i,j] - summationU) / L[i, i] 
          U[i,j] = round(U[i,j], sigFigs)
    #Ld = b
    d = forward_substitution(L,b,sigFigs)
    #Ux = d
    x = backward_substitution(U,d,sigFigs) #final solution
    end = time.time()    
    runTime = end - startTime
    return 0, L, U, x, runTime

def chelosky(A, b, sigFigs, unknownsNumber):
  startTime=time.time()
  #consistency attributes
  augB = b.reshape(-1,1)
  Aug = np.append(A,augB, axis=1)
  rankA = np.linalg.matrix_rank(A) 
  rankAug=np.linalg.matrix_rank(Aug) 
  #consistency check
  if(rankA!=rankAug):
    return 1,0,0,"System is inconsistent and there is no solution"
  elif(rankA==rankAug<unknownsNumber):
    return 1,0,0,"System has infinite number of solutions"
  #unique consistent system
  elif(np.all(np.abs(A-A.T) < 1e-8)):  #check symmetry with transpose by tolerance:
    n = len(A)
    L = np.zeros((n, n)) #set L to zeros of same length as A
    for j in range(n): #cols
      for i in range(j,n): #rows
        if(i==j): #diagonal elements formula
          summation = 0
          for k in range(j):
            summation+= math.pow(L[i,k],2)
          L[i,j] = np.sqrt(A[i,j]-summation) #set L matrix
          L[i,j] = round(L[i,j], sigFigs) #round to sig figs no.
        else: 
          summation = 0
          for k in range(j):
            summation += L[i,k]*L[j,k]
          L[i,j] = (A[i,j] - summation) / L[j,j] #set L matrix
          L[i,j] = round(L[i,j], sigFigs) #round to sig figs no.
    U = L.transpose() #set U to L transpose
    #Ld = b
    d = forward_substitution(L, b, sigFigs)
    #Ux = d
    x = round(backward_substitution(U, d), sigFigs) #final solution
    end = time.time()    
    runTime = end - startTime
    return 0,L,U,x,runTime;
  else: #nonsymmetric system
    end = time.time()    
    runTime = end - startTime
    return 1,0,0,"System is not symmetric",runTime