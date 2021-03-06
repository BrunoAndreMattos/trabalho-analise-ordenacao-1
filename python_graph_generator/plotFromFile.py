import matplotlib.pyplot as plt
import numpy as np
from math import log, exp, factorial, sqrt

# Plot lendo dados de arquivo

data = np.genfromtxt("data.txt", delimiter=' ',names=True)

columns = data.dtype.names
print(columns)
print(data)

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_title("Insertion Shell Sort (tokuda)")    
ax.set_xlabel('Quantidade de Items')
ax.set_ylabel('Trocas')

for m in range(1,len(columns)):
    ax.plot(data[columns[0]],data[columns[m]],label=columns[m])
ax.legend()

fig.savefig('graph.png')

plt.show()

