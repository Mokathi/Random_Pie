import matplotlib.pyplot as plt
import numpy as np

data = [18, 17, 19, 13, 23, 18, 14, 18, 22, 21, 22, 17, 17, 20, 20, 
        16, 24, 16, 17, 20, 21, 20, 22, 16, 26, 21, 17, 21, 25, 24, 25, 20]

k = 7

width = (max(data) - min(data)) / k

hist_data, bins = np.histogram(data, bins=k, range=(min(data), max(data)), density=True)

plt.bar(bins[:-1], hist_data, width=width)
plt.xlabel('Direction values')
plt.ylabel('Relative Frequency')
plt.title('Histogram with Relative Frequencies')

plt.show()

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

if abs(mean - median) < std_dev:
    print("The data appears to be reasonable.")
else:
    print("The data may not be reasonable.")