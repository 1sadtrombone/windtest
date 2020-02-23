import tools
import matplotlib.pyplot as plt

data = tools.readDates(["20200218"])

abs_diff = data[:,2] - data[:,5] # absolute difference of average windpeeds
pct_diff = abs_diff / data[:,2] # percent difference relative to anemom1

counts = plt.hist(abs_diff)
plt.savefig("plots/20200218_abs_diffs_hist.png")
