import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    #Using my same code from a previous pi assignment in this course
    #these values are from the wiki link
    a = 1
    b = 1 / (2 ** (1 / 2))
    t = 1 / 4
    p = 1
    #using a for loop to run through a specific range to estimate the value of pi
    for iterations in range(1, 20):  # Loop is being told to go through 10 times
        """
        Step 2: Update each variable based upon the algorithm. Take care to ensure
        the order of operations and dependencies among calculations is respected. You
        may wish to create new "temporary" variables to hold intermediate results
        """
        ### YOUR CODE HERE ###

        # These are from the wiki link equations in the readme file
        a_new = (a + b) / 2
        b_new = (a * b) ** (1 / 2)
        p_new = 2 * p
        t_new = t - p * (a_new - a) ** 2

        # storing the new variables in the place of old so they continue to update throughout the loop
        a = a_new
        b = b_new
        p = p_new
        t = t_new
        pi_estimate = ((a_new + b_new) ** 2) / (4 * t_new)

    # change this so an actual value is returned
    return pi_estimate

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
