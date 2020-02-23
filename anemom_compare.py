import numpy as np
import matplotlib.pyplot as plt

# get data from an arbitrary day
data = np.genfromtxt("wind_test_data/20200218.CSV", delimiter=',', skip_header=1)

time = data[:,0]
anemom1 = data[:,2]
anemom2 = data[:,5]

plt.plot(anemom1, anemom2, 'k.')
plt.xlabel("anemom1")
plt.ylabel("anemom2")
plt.savefig("plots/first_compare.png")
plt.clf()

plt.plot(time, anemom1-anemom2, 'k.')
plt.xlabel("time")
plt.ylabel("absolute difference")
plt.savefig("plots/first_diff.png")
