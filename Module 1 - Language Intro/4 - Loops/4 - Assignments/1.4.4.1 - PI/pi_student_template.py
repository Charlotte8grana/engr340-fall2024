import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""
a = 1
b = 1 / (2 ** (1 / 2))
t = 1 / 4
p = 1
# modify these lines to correct set the variable values
##These values are coming from the wiki link provided in the readme file

# perform 10 iterations of this loop
for iterations in range(1, 11): #Loop is being told to go through 10 times
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """
    ### YOUR CODE HERE ###

    #These are from the wiki link equations in the readme file
    a_new = (a + b) / 2
    b_new = (a * b)**(1 / 2)
    p_new = 2 * p
    t_new = t - p * (a_new - a)**2

    #storing the new variables in the place of old so they continue to update throughout the loop
    a = a_new
    b = b_new
    p = p_new
    t = t_new
    pi_estimate = ((a_new + b_new) ** 2) / (4 * t_new)

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", iterations)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
#this tells me the estimate of pi after the 10th loop above

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
