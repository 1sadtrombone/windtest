import numpy as np
import matplotlib.pyplot as plt
import tools

# get data from an arbitrary day
data = tools.readDate("20200219")

data = data[data[:,0] < 1582127040] # cut off when anemometers swapped

time = data[:,0]
inds = np.argsort(data[:,2])
anemom1 = data[:,2][inds]
anemom2 = data[:,5][inds]

p = np.polyfit(anemom1, anemom2, 1)

plt.plot(anemom1, anemom2, 'k.')
plt.plot(anemom1, p[0]*anemom1+p[1], 'r--')
plt.xlabel("anemom1")
plt.ylabel("anemom2")
plt.title(f"$a_2 = {p[0]}*a_1+{p[1]}$")
plt.savefig("plots/fit_with_no_errors.png")
