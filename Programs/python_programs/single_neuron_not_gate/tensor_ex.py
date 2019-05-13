"""
Tensor is a generalisation of vectors and matrices.
They are understood as a multi dimensional array.

vector:- One-dimensional or first-order tensor
matrix:- Two-dimensional, or 2nd order tensor.
"""

# Create a tensor
from numpy import array

T = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ])

print(T.shape)
print(T)
