import numpy
import numpy as np
from numpy import linalg as LA
def jacobi(x, A, b ,tol ,maxIteraions, precision):
  for k in range(0, maxIteraions):
    x_new = np.empty(len(A))
    for i in range(0, len(A)):
      sum = 0
      for j in range(0, len(A)):
        if i == j:
          sum = round(sum + b[i], precision)
        if i != j:
          sum = round(sum - round(x[j]*A[i][j], precision), precision) 
      x_new[i] = round(sum/round(A[i][i], precision), precision)
    #Ea calculations
    ea = normCalc(x_new, x)
    print("ea", ea)
    if(ea < tol):
      return x_new
      break;
    x = x_new
    print(x_new)
  return x

      
def normCalc(xnew, xold):
  ea = np.subtract(xnew,xold)
  for i in range(len(xnew)):
    ea[i] = ea[i]/xnew[i]
  return LA.norm(ea)
