from numpy import asarray
from numpy import arange
from numpy.random import rand
import matplotlib.pyplot as plt

#objective function
def objective(x):
    return x**2.0

#derivative function
def derivative(x):
    return x * 2.0

#gradient descent algorithm
def gradient_descent(objective, derivative, bounds, n_iter, step_size):
  #track alll solutions
  solutions, scores = list(), list()
  #generate an initial position
  solution = bounds[:,0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0]) #generate a random between -1 and 1
  #run gradient descent
  for i in range(n_iter):
    #calculate gradient
    gradient = derivative(solution)
    #take a step
    solution = solution - step_size * gradient
    #evaluate the candidate point
    solution_eval = objective(solution)
    #store solution
    solutions.append(solution)
    scores.append(solution_eval)

#define a range for input
bounds = asarray([[-1, 1]])
#total iterations
n_iter = 30
#define step size
step_size = 0.1         

   