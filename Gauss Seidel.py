
import numpy as np
from numpy import linalg as LA
import time

def normCalc(xnew, xold):
  ea = np.subtract(xnew,xold)
  for i in range(len(xnew)):
    ea[i] = ea[i]/xnew[i]
  return LA.norm(ea)

def gaussSeidel(intialGuess, A, b, maxIterations, Es,prec,startTime):
   old = [0 for i in range(len(intialGuess))]
   k=1
   L=0
   runTime=0
   n = len(A)

   # Traverse through all array elements
   for i in range(n):

       # Last i elements are already in place
       for j in range(0, n - i - 1):

           # traverse the array from 0 to n-i-1
           # Swap if the element found is greater
           # than the next element
           if A[j][0] < A[j + 1][0]:
               A[j][0], A[j + 1][0] = A[j + 1][0], A[j][0]
   print(A)
   while k < maxIterations:

       for z in range(len(intialGuess)):
           old[z] = intialGuess[z]


       for i in range (0,len(A)):                 # calculate the 3 new guesses
           value = b[i]
           for j in range (0,len(A)):
               if(j!=i):
                    value=round(value-A[i][j]*intialGuess[j],prec)
           if(A[i][i]==0):
               L=1
               return intialGuess,L
           value =round(value / A[i][i],prec)
           intialGuess[i]=value

       if (k != 1):

                   Ea = normCalc(intialGuess,old)
                   if (Ea <= Es ):
                        end = time.time()
                        runtime=end-startTime
                        return intialGuess,L,runtime
       k=k+1
   end = time.time()
   runtime = end - startTime
   return intialGuess,L,runtime

intialGuess = [1,1,1]
A = [[4,2,1],
     [-1,0,0],
     [2,0,4]]
b = [11, 3,16]
maxIterations = 3
Es = 0.0001
prec =2
print(gaussSeidel(intialGuess,A,b,maxIterations,Es,prec,startTime=4))