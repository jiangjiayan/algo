import numpy as np
import matplotlib.pyplot as plt
"""1.5.1

minimize c = max | ax[i]+ b - y[i]|
subject to:
-b <= ax[i]+ b - y[i] <= b

-b <= -ax[i]- b + y[i] <= b
"""

"""
1.5.2
Cette équation calcule en réalité la valeur minimale du maximum de la valeur absolue de la différence entre les éléments correspondants de la liste ax et y.

Il peut être transformé en un problème d'optimisation linéaire en ajoutant des variables et des contraintes supplémentaires :

1.Ajouter une variable diff[i] pour représenter la valeur de ax[i] + b - y[i].

2.Pour tous les i, ajouter une contrainte -diff[i] <= ax[i] + b - y[i] <= diff[i].

3.La fonction objectif est min (max (diff[i])).

"""

"""
1.5.3 code en norme 1 et norme infini
Ce code tracera deux graphiques, 
un avec des points représentant la différence 
entre les éléments de ax et y dans une norme 1 
et un autre avec des points représentant la même différence dans une norme ∞. 
Les points seront tracés en utilisant la fonction plot de matplotlib 
et les deux graphiques seront affichés ensemble en utilisant la fonction show.
 Les labels des graphiques seront Norme 1 et Norme ∞, respectivement.
"""
# Définir les vecteurs ax, y et b
ax = np.array([3, 8, 1, 0, 10, 6, 4, 7, 1])
y = np.array([2, 4, 9, 1, 0, 15, 1, 0, 1])
b = 14

# Calculer les différences entre les éléments de ax et y

diff = np.abs(ax + b - y)

# Tracer les points en norme 1 et en norme ∞
plt.plot(diff, np.ones_like(diff), 'o', label='Norme 1')
plt.plot(diff, np.inf * np.ones_like(diff), 'o', label='Norme ∞')

# Afficher le graphique
plt.legend()
plt.show()
