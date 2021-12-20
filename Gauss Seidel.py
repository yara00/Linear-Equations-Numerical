
import numpy as np
from numpy import linalg as LA

def normCalc(xnew, xold):
  ea = np.subtract(xnew,xold)
  for i in range(len(xnew)):
    ea[i] = ea[i]/xnew[i]
  return LA.norm(ea)

def gaussSeidel(intialGuess, A, b, maxIterations, Es):
   old = [0 for i in range(len(intialGuess))]
   k=1
   while k < maxIterations:

       for z in range(len(intialGuess)):
           old[z] = intialGuess[z]


       for i in range (0,len(A)):                 # calculate the 3 new guesses
           value = b[i]
           for j in range (0,len(A)):
               if(j!=i):
                    value=value-A[i][j]*intialGuess[j]
           value = value / A[i][i]
           intialGuess[i]=value


       if (k != 1):

                   Ea = normCalc(intialGuess,old)
                   if (Ea <= Es ):
                       return intialGuess
       k=k+1
   return intialGuess

intialGuess = [1,1,1]
A = [[4,2,1],
     [-1,2,0],
     [2,1,4]]
b = [11, 3,16]
maxIterations = 3
Es = 0.0001
print(gaussSeidel(intialGuess,A,b,maxIterations,Es))