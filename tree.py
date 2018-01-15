from math import sin, cos
from matplotlib import pyplot as plt

# Constants
a = 5
b = 0.2
c = 0.6
s = 1


d = [[0, 1, 0]]
plt.plot([0, 0], [0, 1])

for i in range(a):
    n = []
    for j in range(len(d)):
        n.append([d[j][0]+s*sin(d[j][2]-b),
                  d[j][1]+s*cos(d[j][2]-b),
                  d[j][2]-b])
        n.append([d[j][0]+s*sin(d[j][2]+b),
                  d[j][1]+s*cos(d[j][2]+b),
                  d[j][2]+b])

        plt.plot([d[j][0], n[-2][0]], [d[j][1], n[-2][1]])
        plt.plot([d[j][0], n[-1][0]], [d[j][1], n[-1][1]])
    d = n
    s *= c
plt.savefig('tree.png')