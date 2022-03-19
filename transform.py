#!/bin/python3
import numpy as np 
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Renders an animation representing a 2D linear transformation')

parser.add_argument("-c1", "--column1", nargs=2, type=int, required=True, help="the first column vector in the transformation matrix, input as two ints \"x0 x1\"")
parser.add_argument("-c2", "--column2", nargs=2, type=int, required=True, help="the second column vector in the transformation matrix, input as two ints \"x0 x1\"")
parser.add_argument("-v", "--vector", nargs=2, type=int, required=True, help="The vector to be transformed, will also include unit vectors as well by default")

args = parser.parse_args()

col_vector_1 = args.column1
col_vector_2 = args.column2
vector = args.vector

matrix = np.array([[col_vector_1[0], col_vector_2[0]], 
                    [col_vector_1[1], col_vector_2[1]]])

start_vector = np.array([[vector[0]], 
                          [vector[1]]])

print(start_vector[0][0])


#final_vector = np.matmul(matrix, start_vector)


ax = plt.axes()
ax.arrow(0, 0, start_vector[0][0], start_vector[1][0] , head_width=0.5, head_length=0.5)
plt.ylim(-10,10)
plt.xlim(-10,10)
plt.show()
