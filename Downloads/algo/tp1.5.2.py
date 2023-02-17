"""import matplotlib.pyplot as plt
import random

def aléatoire(n, label):
    points = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        points.append((x, y, label))
    return points

rouge = aléatoire(100, "red")
vert = aléatoire(100, "green")

x = [p[0] for p in rouge + vert]
y = [p[1] for p in rouge + vert]
labels = [p[2] for p in rouge + vert]

plt.scatter(x, y, c=labels)
plt.show()
#c'est le code de problem 1,dans ce cas,on peut pas séparer les point
"""

import matplotlib.pylab as plt
import numpy as np

rouge_x = np.array([1.7,2.6,3.4,4.9,4,5.3,6.9])
rouge_y = np.array([5,6.9,12,10,11,12.6,14.7])
vert_x = np.array([1.0,1.4,3.5,4.1,5.2,6.0,6.7])
vert_y = np.array([1.4,1.6,2.0,3.0,9.9,4.0,11.0])

fig, ax = plt.subplots()
ax.plot(rouge_x, rouge_y, "or",
        color = "red",
        markersize = 7)
ax.plot(vert_x, vert_y, "oy",
        color = "green",
        markersize = 7)

point_en_linge = (5, 9.9)
X = np.arange(0,10)
m = point_en_linge[1]/point_en_linge[0]
ax.plot(X, m * X, "black", linewidth = 3)
plt.show()