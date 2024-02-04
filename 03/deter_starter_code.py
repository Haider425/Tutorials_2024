# Recursive computation of the determinant starter code. Tutorial 3 of MATH/CSCI2072 CSI, Ontario Tech U, 2024.
import numpy as np

def deter(A):
    # Recursive computation of the determinant. Input: n X n array A. Out: determinant of A (float).
    n = len(A)                                          # Size of matrix.
    if n == 2:                                          # For 2x2 matrix, use definition.
        detA = None  # Compute the determinant.
    else:                                               # For larger matrices, compute recursively.
        detA = 0                                        # Initialize the determinant.
        for i in range(0, n):                            # Cofactor expansion.
            B = [row[:i] + row[i+1:] for row in A[1:]]   # Delete i-th row.
            detA += (-1) ** i * A[0][i] * deter(B)       # Recursive call.
    return detA

