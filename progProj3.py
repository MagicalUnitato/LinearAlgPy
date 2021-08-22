#Programming Project Number 3
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)
print("X Size of Matrix :")
x = int(input())
print("Y Size of Matrix :")
y = int(input())


matrix  = np.zeros((x,y), dtype="int")
for j in range(len(matrix)):
    for k in range(len(matrix[j])):
        print('Add Values for ' + str(j) + ' row')
        matrix[j][k] = int(input())

#Get Determinant of Matrix
print("Determinant Of Matrix: ")
det = np.linalg.det(matrix)
print(det)
#Get Inverse of Matrix
print("Inverse Of Matrix: ")
inv = np.linalg.inv(matrix)
print(inv)
#Adjoint of Matrix Solving
print("Adjoint of Matrix:")
print(inv * det)
