# Fiona Pigott
# CSCI 4446

# Draw a fractal tree.

# modules
import turtle as t
from math import pi, sin, cos

# set the parameters for the tree
trunk = 150; # trunk length
alphaR = 45; # 
alphaL = 45; # 
ratioR = .6; # ratio of a branch to the next on the right
ratioL = .6; # ratio of a branch to the next on the right

runs = 14; # recursion depth

# make sure that the turtle in facing the right direction
# initial heading = north
# positive angles are clockwise
t.mode("logo")
t.speed(0)
t.hideturtle()
t.tracer(10000, 1)

# Recursively draw the tree.
# Inputs: 'length': length of the branch being drawn
# 	(included as an input so they can be aried with recusion depth)
#         'alphaR': angle of turn on right branches
#         'alphaL': angle of turn on left branches 
def drawTree(length, alphaR, alphaL, depth):

	if depth == 0:
		return

	t.forward(length)
	top = t.position()
	upangle = t.heading()

	# Draw the right half of the tree
	t.right(alphaR)
	drawTree((ratioR)*length, alphaR, alphaL, depth-1)

	# Go back to the start
	t.penup()
	t.goto(top)
	t.setheading(upangle)
	t.pendown()

	# Draw the left half of the tree
	t.left(alphaL)
	drawTree((ratioL)*length, alphaR, alphaL, depth-1)

# Call drawTree
t.pencolor(0,0,0)
t.penup()
t.setheading(0)
t.goto(0,-trunk)
t.pendown()
drawTree(trunk, alphaR, alphaL, runs)

t.done()




