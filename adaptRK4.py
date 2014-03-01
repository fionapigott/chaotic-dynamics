# Fiona Pigott
# CSCI 4446

# Time step adaptive implementation of the numerical method 
# Runga-Kutta 4 for solving differential equations.

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

# Find the difference between taking a RK4 step with size h
# and a step with size h/2
# Input: (same as input to 'step')
# Output: 'xs': new position vector, calculated using h/2
#               (because that will have less error)
#         'ts': new time
#         'diff': the euclidean distance between the positon
#                 calculated with h/2 vs calculated with h
def vary_step(diffeq, h, x, t):

	# take one full size step
	(xl,tl) = step(diffeq, h, x, t)
	# take two half size steps
	(xs,ts) = step(diffeq, h/2, x, t)
	(xs,ts) = step(diffeq, h/2, xs, ts)
	# compute the Euclidean distance between xl and xs
	diff = np.linalg.norm(xl-xs)
	# return the values with the least error on them
	return (xs, ts, diff)

# Use adaptive step sizes to calculate a trajectory, for
# a tolerance of 10^(-6). That is, choose steps sizes
# such that the difference is position between a step calculated 
# for step size h is within 10^(-6) of that calculated with 
# step size h/2, but not so small that we are wasting time
# getting very small errors (<10^(-6))
# Input: 'steps': number of time steps to take
#                 total time calculated = steps*h (input h)
#        'diffeq': function which outputs the derivative of a system
#        'h': oiginal step size (adaptive RK4, so this will change)
#        'init': vector of initial position
# Output: 'points': vector of all of the points in the trajectory
def adaptRK4(steps, diffeq, h, init):

	# h = step size
	# steps*h = amount of time calculated
	# init = the initial position of the attractor

	# tolerance
	TOL = 10**(-6) 
	# initialize
	t = 0 
	x = init
	xlist = []
	xlist.append(x)

	# take a first step
	(x, t, diff) = vary_step(equation, h, x, t)

	for it in xrange(0,steps): # stoping condition

		# decide what to do with h

		# h is perfect (the error is just slightly less than TOL)
		if (diff >= TOL - .05*TOL) and (diff <= TOL):
			# take a step and record the point
			(x, t, diff) = vary_step(equation, h, x, t)
			xlist.append(x)
			# print 'perfect'


		# h is too small (the error is much less than TOL)
		while (diff < TOL - .05*TOL):
			h = h*2
			(x, t, diff) = vary_step(equation, h, x, t)
			# but still take a step and record the point
			xlist.append(x)
			# print 'too slow!'

		# h is too big (the error is much greater than TOL)
		while (diff > TOL) and (h > 10**(-10)):
			h = h/2
			# take a step to check if h is small enough
			# but don't record the point
			(xgarbage, tgarbage, diff) = vary_step(equation, h, x, t)
			# print 'too fast!'

	# convert the list to an array for matplotlib
	points = np.array(xlist)
	return points


# Define initial conditions
init = np.array([-13.0,-12.0,52.0])
# Calculate the trajectory
adapttraj = adaptRK4(5000, equation, .005, init)
# Plot the attractor
plt.plot(adapttraj[:,0], adapttraj[:,2],'k.', markersize = 2)
plt.title('Lorenz Attractor')
plt.xlabel('x')
plt.ylabel('z')
plt.show()









