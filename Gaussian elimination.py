#Gaussian elimination

def get_result_gaussian_elimination(n, A):
  # n is the number of unknowns
  # A is the Augmented n x n+1 matrix. (numpy array)
  # Making numpy array of n size and initializing
  # to zero for storing solution vector
  x = np.zeros(n)
  for i in range(n):
    if A[i][i] ==0:
      return
    else:
      for j in range(i+1,n):
        m = (A[j][i]) / (A[i][i]) # divier
        for k in range(n+1):
          A[j][k] = A[j][k] - m * A[i][k]
  x[n-1] = A[n-1][n] / A[n-1][n-1]
  for i in range(n-2,-1,-1):
    x[i] = A[i][n]
    for j in range(i+1,n):
      x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]
  return x

# Test case for the get_result_gaussian_elimination(n, A) function.

data_n = 3
data_A = np.array([[1, 2, 1, 0], [1, -2, 2, 4], [2, 12, -2, 4]])

test = get_result_gaussian_elimination(data_n, data_A)
results = [11, -2.5, -6]

np.testing.assert_array_equal(test, results)
