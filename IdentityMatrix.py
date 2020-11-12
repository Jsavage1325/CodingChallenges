# Create a program to create an identity matrix
# The matrix is of size n, and is created using only n
# if n is negative a mirror of the identity matrix should be returned
# https://edabit.com/challenge/QN4RMpAnktNvMCWwg
# would be very similar without using numpy, the only reason numpy was used was for fast array filling with 0's
import numpy as np


def create_identity_matrix(n):
    if n is 0:
        return "Error"
    elif n is 1 or n is -1:
        im = [1]
    elif n > 1:
        im = np.zeros((n, n))
        for i in range(n):
            im[i, i] = 1
    elif n < -1:
        im = np.zeros((abs(n), abs(n)))
        for i in range(abs(n)):
            im[i, (abs(n)-i-1)] = 1
    return im


if __name__ == "__main__":
    print(create_identity_matrix(-4))
    print(create_identity_matrix(7))
    print(create_identity_matrix(1))
    print(create_identity_matrix(-1))
    print(create_identity_matrix(0))