import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = 0
## YOUR CODE HERE ##
signal = np.loadtxt(signal_filepath, delimiter=',', skiprows=2)
time = signal[:,0]
MLII = signal[:,1]
V1 = signal[:,2]
plt.title('Graph of raw signal for ' + database_name)
plt.xlabel('Time (sec)')
plt.ylabel('V1 and MLII (mV)')
plt.plot(signal)
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
diff = np.diff(V1)
plt.plot(diff)
plt.title('Graph of Derivative for ' + database_name)
plt.xlabel('Time (sec)')
plt.ylabel('V1 (mV)')
plt.show()
"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
square = np.square(diff)
plt.plot(square)
plt.title('Graph of square for ' + database_name)
plt.xlabel('Time (sec)')
plt.ylabel('V1 (mV)')
plt.show()
"""
Step 5: Pass a moving filter over your data
"""
## YOUR CODE HERE ##
v = [1, 1, 1, 1, 1,]
thing = np.convolve(square, v)


# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(thing)
plt.xlabel('Time (sec)')
plt.ylabel('V1 (mV)')
plt.show()