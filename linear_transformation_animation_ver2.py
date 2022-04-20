#!/bin/python3

import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Take inputs via argparse
parser = argparse.ArgumentParser(description=('Renders an animation representing a 2D linear tranformation'))

parser.add_argument("-c1", "--column1", nargs=2, type=int, required=True, help=("The first column vector in the transformation matrix. This should be inputted as two ints, \"x0 x1\""))
parser.add_argument("-c2", "--column2", nargs=2, type=int, required=True, help=("The second column vector in the transformation matrix. This should be inputted as two ints, \"x0 x1\""))
parser.add_argument("-v", "--vector", nargs=2, type=int, required=True, help=("The vector that will be transformed. Defaults to the unit vectors."))

args = parser.parse_args()

# Assigns data from the inputs to variables
col_vector_1 = args.column1
col_vector_2 = args.column2
vector = args.vector

# Creates starting vector
start_vector = np.array([[vector[0]], 
                          [vector[1]]])

# Creates the plot
fig, ax = plt.subplots()

# Limits the size of the x and y axis
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Creates the arrow of the vector and places it on the plot
quiver = ax.quiver(vector[0], vector[1], color=['b'], angles='xy', scale_units='xy', scale=0.5)

# Smoothing function that returns how complete the transformation is
def sigmoid(num_frames):
    return max(1.01799 / (1 + math.exp(-10 / 60 * num_frames + 4)) - 0.01799, 0)

# Renders the frames of the animation
def animate(num_frames):

    sig = sigmoid(num_frames)
    x1 = col_vector_1[0]
    x2 = col_vector_2[0]
    y1 = col_vector_1[1]
    y2 = col_vector_2[1]

    #adjusted matrix for this part of the animation
    dx1 = 1 + x1 * sig
    dy1 = 0 + y1 * sig
    dx2 = 0 + x2 * sig
    dy2 = 1 + y2 * sig

    transform = np.matrix([[dx1, dx2],[dy1, dy2]])
    
    matrix = np.matmul(transform, start_vector)

    quiver.set_UVC(matrix[0][0], matrix[1][0])

# Makes a gif of the animation
gif_creator = animation.FuncAnimation(fig, animate, frames=60, interval=20, repeat=False, blit=False)

# Saves gif in whichever directory this code is running in
gif_creator.save('miniproject.gif', fps=30, bitrate=5000, dpi=250)