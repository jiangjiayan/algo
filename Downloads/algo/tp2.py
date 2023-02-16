"""
Le problème de production peut être formalisé comme un problème d'optimisation linéaire en utilisant la fonction objective suivante :

Minimize : c[s] * s + Σ(c[i] * x[i] + c[δ] * (x[i] - x[i-1])) pour i = 1 à n

Subject to :
x[i] <= p pour i = 1 à n (capacité de production maximale par jour)
x[i] >= 0 pour i = 1 à n (production minimale)
s >= x[i] - d[i] pour i = 1 à n (stockage minimale)
s <= p pour i = 1 à n (capacité de stockage maximale)

Où :
x[i] = production du jour i
s = stock
d[i] = demande prévue du jour i
p = capacité de production maximale par jour
c[s] = coût de stockage par unité de produit
c[i] = coût de production par unité de produit le jour i
c[δ] = coût de variation de production entre deux jours consécutifs par unité de produit
"""
"""
Pour résoudre ce problème en utilisant Python avec PULP, nous pouvons suivre les étapes suivantes:

Importer la bibliothèque PULP

Définir les variables: Nous définissons les variables de décision pour chaque jour i, qui représentent la quantité produite ce jour-là. Nous appellerons ces variables "x".

Définir les contraintes: Nous définissons les contraintes pour la capacité de production, la capacité de stockage et la variation de production.

Définir l'objectif: Nous définissons l'objectif en minimisant le coût total de production et de stockage.

Résoudre le problème en utilisant la fonction solve() de PULP.

Afficher les résultats.

"""
from pulp import *

# Define the problem and decision variables
prob = LpProblem("Production Planning", LpMinimize)
n = 5
d = [100, 120, 150, 110, 90]
p = 200
s = 1000
c_s = 2
c = [3, 4, 5, 6, 7]
c_d = 1
x = [LpVariable("x_%d" % i, lowBound=0) for i in range(n)]

# Define the objective function
prob += lpSum([c[i] * x[i] + c_s * (x[i] - d[i]) for i in range(n)]) + c_d * lpSum([x[i+1] - x[i] for i in range(n-1)])

# Define the constraints
for i in range(n):
    prob += x[i] <= p
    prob += x[i] >= d[i]
    prob += x[i] <= s

# Solve the problem
prob.solve()

# Print the results
for i in range(n):
    print("Production on day %d: %f" % (i+1, x[i].value()))

