import numpy as np
import matplotlib.pyplot as plt

# Génération de points de données aléatoires
np.random.seed(0)
n = 99
x = np.linspace(0, 10, n)
y = 1 * x + np.random.normal(0, 2, n)

# Calcul de l'interpolation en norme infinie
z_inf = np.poly1d(np.polyfit(x, y, 1, w=np.ones_like(x)))


# Tracé des points de données et de la droite d'interpolation en norme infinie
plt.scatter(x, y, label='Données originales')
plt.plot(x, z_inf(x), color='red', label='Interpolation en norme infinie')

# Ajout d'une légende et d'un titre
plt.legend()
plt.title('Interpolation en norme infinie')

# Affichage du résultat
plt.show()
