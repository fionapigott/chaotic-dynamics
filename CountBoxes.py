# Fiona Pigott
# CSCI 4446
# Hw 10

# Box Counting dimension:
# To compute N(e) for a given e, calculate the number of m dimensional 
# boxes with side length e that it takes to cover the attractor.

# Output: Plot of N(e), capacity dimension (slope of the scaling region
# 		  of the plot), D_cap.

# Compute the box counting dim for the Lorentz attractor.
# Note: this trajectory has 300,000 points, and this code plots N(e) as a 
# function of epsilon, so that calculation is repeated for each e.
# It will take a few minutes

import numpy
import matplotlib.pyplot as plt
import math

def find_N(epsilon):
	# load the trajectory
	arraytraj = numpy.loadtxt('LorenzTraj300000')
	arraytraj.tolist()
	traj = [ ar.tolist() for ar in arraytraj ]

	# decide the origin
	# same number of points as the embedding dimension m
	x0 = tuple([0,0,0,0,0,0,0])

	# discretize the points of the trajectory such that each point is within 
	# some integer number of epsilon units from some (arbitrary) origin. 
	# Discretized x = (x - origin)/e. 
	# Only store the number of unique discretized points which  = N(e)
	# Count the number of unique points by adding each point to a set, 
	# then the cardinality of the set is N (e).
	boxes = set([tuple([int((x - x0[i])/epsilon) 
		for i,x in enumerate(xpoint)]) for xpoint in traj])
	N = len(boxes)
	return N

# Calculate the box dimension for a set of e values
N = []
logep = []
eps = list(numpy.logspace(-3, 2, num = 50))

for ep in eps:
	N.append(math.log(find_N(ep),10))
	logep.append(math.log(1.0/(ep),10))

# Find the slope of the straight part of the trajectory
# to find the capacity dimension
slope = (N[50-14]-N[50-8])/(logep[50-14]-logep[50-8])
print slope

# Plot N(e) as a function of e
plt.plot(numpy.array(logep),numpy.array(N),'k.')
plt.ylabel('log(N(epsilon))')
plt.xlabel('log(1/epsilon)')
plt.show()

