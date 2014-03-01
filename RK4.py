# Fiona Pigott
# CSCI 4446

# Runga-Kutta 4 impplementation for solving differential equations.

# Solves the system of equations defined in 'equation'
# for initial conditions 'init'
# Solves the Lorentz system:
# x' = a*(y-x)
# y' = r*x-y-x*z
# z' = x*y-b*z
# For parameters a = 16, r = 45, b = 4
# and initial conditions: [x y z] = [-13, -12, 52]

# OUTPUT: Plot of the Lorentz attractor

# Libraries:
import math
import numpy as np 
import matplotlib.pyplot as plt 

# Lorentz equation
# Input: 'pos': current position of the attractor, vector [x y z]
#		 'time': current time 
# Output: 'dfdx': derivative of the system at 'pos', vector [x' y' z']

def equation(pos, time):

	# Parameters:
	a = 16.0
	r = 45.0
	b = 4.0

	x = pos[0]
	y = pos[1]
	z = pos[2]

	dfdx = np.array([a*(y-x), r*x-y-x*z, x*y-b*z])
	return dfdx

# Take one RK4 step
# Input: 'diffeq': function defining the differential equation
#				   with inputs: (position vector, time)
#        'h': length of the time step
#        'x': current position vector
#        't': current time
# Output: '(x,t)': tuple of 'x' (new position vector) 
#				   and 't' (new time)
def step(diffeq, h, x, t):
	
	k1 = h*diffeq(x, t)
	k2 = h*diffeq(x+(k1/2), t+(h/2))
	k3 = h*diffeq(x+(k2/2), t+(h/2))
	k4 = h*diffeq(x+k3, t+h)

	x = x + (k1+2*k2+2*k3+k4)/6
	t = t + h

	return (x,t)

# Take RK4 steps to solve the differential equation
# Input: 'steps': number of time steps to take
#                 total time calculated = steps*h (input h)
#        'diffeq': function which outputs the derivative of a system
#        'h': step size 
#        'init': vector of initial position
# Output: 'points': vector of all of the points in the trajectory
def myRK4(steps, diffeq, h, init):

	# initialize
	x = init 
	t = 0
	xlist = []
	xlist.append(x)

	# take RK4 steps
	for iter in xrange(0, steps):
		(x,t) = step(diffeq, h, x, t)
		xlist.append(x)

	# convert the list to an array
	points = np.array(xlist)
	return points

# Define initial conditions
init = np.array([-13.0,-12.0,52.0])
# Calculate the trajectory
traj = myRK4(10000, equation, .001, init)

# save the output
with open('LorenzTraj10000', 'w+') as f:
	np.savetxt(f, traj)
# plot the output
plt.plot(traj[:,0], traj[:,2],'k.', markersize = 2)
plt.show()









