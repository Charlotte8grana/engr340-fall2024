
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
LT=np.loadtxt(path, delimiter=',', skiprows=2)

# save each vector as own variable
time = LT[:,0]
MLII = LT[:,1]
V1 = LT[:,2]

# use matplot lib to generate a single
#Plot for MLII and Time
plt.title('MLII vs Time')
plt.xlabel('Time (sec)')
plt.ylabel('MLII (mV)')
plt.plot(time, MLII)
#plt.show()

#Plot for V1 and Time
plt.title('V1 vs Time')
plt.xlabel('Time (sec)')
plt.ylabel('V1 (mV)')
plt.plot(time, V1)
plt.show()
