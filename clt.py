import random
import numpy as np
import matplotlib.pyplot as plt


random_ints = []
means = []

low_bound = 54
high_bound = 100000

for _iterations in range(1000):
    for _sample_size in range(100):
        random_ints.append(random.randint(low_bound, high_bound))
    
    means.append(np.mean(random_ints))
    del random_ints[:]



sorted_means = sorted(means)

print("Mean of data: " + str(np.mean(sorted_means)))

print("Mean of range boundarys: " + str(np.mean([low_bound, high_bound])))

plt.hist(sorted_means, bins = high_bound - low_bound)

plt.show()