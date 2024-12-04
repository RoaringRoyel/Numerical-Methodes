# Solving a linear system using inverse matrix

import matplotlib.pyplot as plt
import numpy as np
import sys

def get_result_by_inverse_matrix(A, b):
  # A and b are numpy arrays
  # first check if the A is non-singular matrix. We know that the determinant of
  # a non-singular matrix will be non-zero
  # YOUR CODE HERE
  detA = np.linalg.det(A)
  if detA == 0:
    return "Not Possible"
  A_inverse = np.linalg.inv(A)
  return np.dot(A_inverse,b)

# Test case for the get_result_by_inverse_matrix(A, b) function.

data_A = np.array([[1, 2, 1], [1, -2, 2], [2, 12, -2]])
data_b = np.array([0,4,4])

test = get_result_by_inverse_matrix(data_A, data_b)
results = [11, -2.5, -6]

np.testing.assert_array_equal(test, results)
