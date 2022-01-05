import numpy as np
import matplotlib.pyplot as plt

def secant(eq, x1, x2, n, tol):
  for i in range(1,n):
    x = x2
    fnx2 = eval(eq)
    x = x1
    fnx1 = eval(eq)
    x3 = x2 - ((fnx2 * (x1-x2)) / (fnx1 - fnx2))
    print("Value of iteration", i , " is ", x3)

    if(((x3 - x2)/ x3) < tol):
      return x3
    x1 = x2
    x2 = x3

  return x3

def draw(fun, root):
  #step size
  h = 0.1
  x = np.arange(root-1, root+1, h) 
  y = eval(fun)
  # compute vector of forward differences
  forward_diff = np.diff(y)/h 
  yy = y[:-1:] 
  x_diff = x[:-1:] 

  plt.figure(figsize = (12, 8))
  plt.plot(x_diff, forward_diff, '--', \
          label = 'Finite difference approximation of f''(x)')

  plt.legend()
  plt.show()