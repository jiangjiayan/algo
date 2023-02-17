import numpy as np
import matplotlib.pyplot as plt


# Génération de points de données aléatoires
np.random.seed(0)
n = 99
x = np.linspace(0, 10, n)
y = 3* x + np.random.normal(0, 2, n)#fonction y = 3x+b,b est random par numpy

# Calcul de la régression linéaire
a, b = np.polyfit(x, y, 1)
z = a * x + b

# Calcul de la différence en norme 1
inter1 = np.max(np.abs(z - y))

# Calcul de la différence en norme infi
interf = np.min(inter1)

# Tracé des points de données et des lignes de régression
plt.scatter(x, y, label='Données originales')#scatter les points
plt.plot(x, z, color='red', label='interpolation linéaire en norme 1')
#plt.plot(x,inter1,color='blue')
plt.plot([x[0], x[-1]], [z[0] - interf, z[-1] - interf], color='green', label='interpolation linéaire en norme infini')

# Ajout d'une légende et d'un titre
plt.legend()
plt.title('interpolation en normes 1 et infini')

# Affichage du résultat
plt.show()


