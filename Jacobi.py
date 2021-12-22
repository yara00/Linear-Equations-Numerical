import numpy
import numpy as np
from numpy import linalg as LA
def jacobi(x, A, b ,tol ,maxIteraions, precision):
  """
    function for approximating the solution of system of linear equations using Jacobi iterative method.
    :param x: array or list representingintial guess.
    :param A: array or list coeffecient.
    :param b: array or list b values.
    :param tol: tolerance float number
    :param maxIteration: integer representing maximun number of iterations 
    :param prescion: integer representing number of decimal digits reqired
    :return: array list representing approximated solution for the equations
           : integer 0 for no error, 1 if error found
  """ 
  for k in range(0, maxIteraions):
    x_new = np.empty(len(A))
    for i in range(0, len(A)):
      sum = 0
      for j in range(0, len(A)):
        if i == j:
          sum = round(sum + b[i], precision)
        if i != j:
          sum = round(sum - round(x[j]*A[i][j], precision), precision)
      if A[i][i] == 0:
        return x, 1
      x_new[i] = round(sum/round(A[i][i], precision), precision)
    #check if tolerance was achieved.
    ea = normCalc(x_new, x)
    if(ea < tol):
      return x_new, 0
      break;
    x = x_new
  return x, 0

      
def normCalc(xnew, xold):
  """
    :function for calculating relative error using norm.
    :param xnew: array or list of the new X values.
    :param xold: array or list of the old X values.
    :return: relative error Ea.
  """ 
  #suntract new x values from old ones
  ea = np.subtract(xnew,xold)
  # divide by x new values.
  for i in range(len(xnew)):
    ea[i] = ea[i]/xnew[i]
  return LA.norm(ea)
