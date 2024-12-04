#LU Decomposition

def lu(A):

  #Get the number of rows
  n = A.shape[0]

  U = A.copy()
  L = np.eye(n, dtype=np.double)


   # YOUR CODE HERE
  for i in range(n):
    if A[i][i] ==0:
      break
    else:
      for j in range(i+1,n):
        m = (A[j][i]) / (A[i][i])
        L[j][i] = m
        for k in range(n):
          A[j][k] = A[j][k] - m * A[i][k]
  U = A
  #Loop over rows
  # for i in range(n):
    #Eliminate entries below i with row operations
    #on U and reverse the row operations to
    #manipulate L

  return L, U

def forward_substitution(L, b):

  #Get number of rows
  n = L.shape[0]

  #Allocating space for the solution vector
  y = np.zeros_like(b, dtype=np.double);


  L_inverse = np.linalg.inv(L)
  y = np.dot(L_inverse,b)

  #Perform the forward-substitution.
  #Initialize  with the first row.
  #Loop over rows in reverse (from the bottom  up),
  #Start with the second to last row, because  the
  #last row solve was completed in the last step.

  return y



def back_substitution(U, y):

  #Number of rows
  n = U.shape[0]

  #Allocating space for the solution vector
  x = np.zeros_like(y, dtype=np.double);


  # YOUR CODE HERE
  u_inverse = np.linalg.inv(U)
  x = np.dot(u_inverse,y)

  #Perform the back-substitution.
  #Initialize with the last row.
  #Loop over rows in reverse (from the bottom up),
  #Start with the second to last row, because the
  #last row solve was completed in the last step.

  return x



def lu_solve(A, b):

  L, U = lu(A)

  y = forward_substitution(L, b)

  return back_substitution(U, y)

# Test case for the lu_solve(A, b) function.

data_A = np.array([[1., 2., 1.], [1., -2., 2.], [2., 12., -2.]])
data_b = np.array([0., 4., 4.])

test = lu_solve(data_A, data_b)
results = [11, -2.5, -6]

np.testing.assert_array_equal(test, results)
