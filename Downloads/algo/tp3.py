"""
1.Il n'est pas toujours possible de tracer
une ligne séparant les points rouges et verts sur le plan réel. 
Cela dépend de la répartition des points. 
Si la distribution des points rouges et verts est t
elle qu'ils sont mélangés et ne peuvent être séparés par une ligne droite, 
on parle de données non séparables. Dans ce cas, 
il n'y a pas de ligne droite qui puisse les séparer correctement.

Cependant, si la distribution des points rouges et verts est telle qu'ils peuvent être séparés par une ligne droite, 
on dit que les données sont séparables. 
Dans ce cas, on peut tracer une ligne droite pour séparer les points rouge et vert, en les plaçant du même côté de la ligne.
"""


"""
2.
Oui, c'est possible de choisir une droite qui passe par le point milieu entre le point rouge et le point vert les plus proches.

Cela peut être fait en trouvant le point rouge et le point vert les plus proches, 
en calculant leur milieu et en dessinant une droite qui passe par ce point milieu. 
Cette droite sera à mi-chemin entre ces deux points les plus proches.

Cependant, il est important de noter que cette méthode ne garantit pas qu'il y aura une telle droite qui 
passe par le point milieu pour tous les ensembles de points rouges et verts.
 Il peut y avoir des cas où aucune droite ne peut être trouvée qui soit à mi-chemin entre les deux points les plus proches.

"""
"""
3.
Oui, il est possible de trouver un polynôme de degré 2, 3, ... qui peut séparer 
les points s'ils sont séparables et qu'une droite ne peut pas les séparer. 
Les polynômes de degré plus élevé peuvent capturer des relations plus complexes 
entre les données et peuvent mieux séparer les points en conséquence. 

Cela dépend de la distribution des points rouges et verts dans le plan. 
Si les points rouges et verts sont distincts et séparés, 
il est possible de trouver un polynôme de degré 2 ou supérieur pour les séparer.
Cependant, si les points rouges et verts sont mélangés et qu'il n'y a pas de tendance claire à les séparer, 
il peut être impossible de trouver un polynôme de degré 2 ou supérieur qui les sépare.

"""

"""
import matplotlib.pyplot as plt
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
plt.show()#c'est le code de problem 1,dans ce cas,on peut pas séparer les point
"""

"""
import matplotlib.pyplot as plt
import numpy as np
import random


x = np.linspace(-10, 10, num=100)

# on fait y=x
y = x
plt.plot(x, y, label='y = x')

# point aléatoire par random
rouge_x = [random.uniform(-10, 10) for i in range(10)]
rouge_y = [random.uniform(-10, 10) for i in range(10)]
vert_x = [random.uniform(-10, 10) for i in range(10)]
vert_y = [random.uniform(-10, 10) for i in range(10)]

# séparé les points rouge et vert
rouge_points = [(x, y) for x, y in zip(rouge_x, rouge_y) if y > x]
vert_points = [(x, y) for x, y in zip(vert_x, vert_y) if y < x]


plt.scatter([x for x, y in rouge_points], [y for x, y in rouge_points], c='red', label='red points')
plt.scatter([x for x, y in vert_points], [y for x, y in vert_points], c='green', label='green points')

plt.legend()
plt.show()
#dans ce cas ,les point rouge et vert peut etre séparé par y=x
"""

"""
import numpy as np
import matplotlib.pyplot as plt

# y=x^2
x = np.linspace(-5, 5, 100)
y = x ** 2

# les points rouges et verts aléatoire
red_x = np.random.rand(20) * 10 - 5
red_y = red_x ** 2 + np.random.rand(20) * 2
green_x = np.random.rand(20) * 10 - 5
green_y = green_x ** 2 - np.random.rand(20) * 2

# plt.
plt.plot(x, y, 'g-', label='y = x^2')
plt.scatter(red_x, red_y, c='r', label='red points above')
plt.scatter(green_x, green_y, c='g', label='green points below')
plt.legend()
plt.show()

"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

rouge_x = np.array([1.7,2.6,3.4,4.9,4,5.3,6.9])
rouge_y = np.array([5,6.9,12,10,11,12.6,14.7])
vert_x = np.array([1.0,1.4,3.5,4.1,5.2,6.0,6.7])
vert_y = np.array([1.4,1.6,2.0,3.0,9.9,4.0,11.0])

# 构造特征矩阵和标签向量
X = np.concatenate((np.vstack((rouge_x, rouge_y)).T, np.vstack((vert_x, vert_y)).T))
y = np.concatenate((np.zeros(rouge_x.shape), np.ones(vert_x.shape)))

# 使用感知机算法分类
clf = Perceptron()
clf.fit(X, y)

# 绘制分类结果
plt.scatter(rouge_x, rouge_y, c='red')
plt.scatter(vert_x, vert_y, c='green')
x_min, x_max = plt.xlim()
w = clf.coef_[0]
b = clf.intercept_[0]
y_min, y_max = (-b - w[0] * x_min) / w[1], (-b - w[0] * x_max) / w[1]
plt.plot([x_min, x_max], [y_min, y_max], 'k-')
plt.show()

