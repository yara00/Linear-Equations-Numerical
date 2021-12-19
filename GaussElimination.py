import numpy as np
def gauss_pivot(D,g,Aug,numberofunknowns):
    A=np.array((D),dtype=float)
    f=np.array((g),dtype=float)
    rankA = np.linalg.matrix_rank(A) 
    rankAug=np.linalg.matrix_rank(Aug) 
    n = len(f)
    
    if(rankA!=rankAug):
        print("System is inconsistent and there is no solution")
    elif(rankA==rankAug<numberofunknowns):
        print("system has infinite number of solution")
    else:
        for i in range(int(0),int(n-1)):     # Loop through the columns of the matrix
            maxelement=max(A[:,i],key=abs)  #max element in col#i
            if (A[i,i])!=maxelement: #max element of col #i is not the one in the diagonal,pivoting is needed
                for k in range(i+1,n):
                    if np.abs(A[k,i])>np.abs(A[i,i]):
                        A[[i,k]]=A[[k,i]]             # Swaps ith and kth rows to each other
                        f[[i,k]]=f[[k,i]] 
                    
             #now elimination    
            for j in range(i+1,n):     # Loop through rows below diagonal for each column
                m = A[j,i]/A[i,i]      #get the multiply
                roundm=round(m,4)
                A[j,:] = A[j,:] - roundm*A[i,:]
                f[j] = f[j] - roundm*f[i] 
           
        Back_Subs(A,f)

def Back_Subs(A,f):
    n = f.size
    x = np.zeros(n)             # Initialize the solution vector, x, to zero
    x[n-1] = round(f[n-1]/A[n-1,n-1],3)    # Solve for last entry first
    
    for i in range(n-2,-1,-1):      # Loop from the end to the beginning
        sum_ = 0
        for j in range(i+1,n):         
            sum_ = sum_ + A[i,j]*x[j]
        x[i] = round((f[i] - sum_)/A[i,i],3) 
    print(x) 

A = np.array([[10,-7,0],[-3,2.099,6],[5,-1,5]])    #has solution[0,-1,1]
f = np.array([7,3.901,6])
Aug=np.array([[10,-7,0,7],[-3,2.099,6,3.901],[5,-1,5,6]])
numberofunknowns=3 #number of unknowns
gauss_pivot(A,f,Aug,numberofunknowns)              