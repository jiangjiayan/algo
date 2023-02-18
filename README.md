# Algorithmique Avancée TP1
## TP1.5.1 Interpolation en norme infini  
### 1. Formalisez ce problème comme un problème d'optimisation linéaire.  
On introduit les variables $z_0, ..., z_{n-1},  i=0, ..., n-1$ telles que
```math
z_i = \| \alpha x_i + b - y_i \|_{\infty} = max |\alpha x_i + b - y_i | \geq |\alpha x_i + b - y_i | \, , \quad i=0, ..., n-1.
```
En cherchant à minimiser la plus grande difference, on cherche, en effet, à minimiser leur somme, et donc notre problème devient comme suivant
```math
\begin{align*}
&min\sum_{i=0}^{n-1} z_i \\
&z_i \geq \alpha x_i + b - y_i \\
&z_i \geq -(\alpha x_i + b - y_i)
\end{align*}
```
### 2. Démontrez que votre formule capture exactement le problème.  
On va montrer maintenant que $(\alpha, b)$ est une solution optimale du problème sous la forme initiale si et seulement si $(\alpha, b, \bar{z})$ est une solution optimale du problème sous la forme de l'optimisation linéaire.
Supposons $(\alpha, b)$ optimale.
On a bien $(\alpha, b, \bar{z})$ est une solution avec $z_i = max | \alpha x_i + b |$. On va montrer que elle est aussi optimale.
Soit $(\alpha^{'}, b^{'}, \bar{z^{'}})$ une autre solution.
```math
\sum_{i=0}^{n-1} z_i^{'}\geq \sum_{i=0}^{n-1} max | a^{'} x_i + b^{'} - y_i | \overset{ (\alpha, b) \text{ opt} }{\geq} \sum_{i=0}^{n-1} max | \alpha x_i + b - y_i | = \sum z_i
```
D'autre part on suppose $(\alpha, b, \bar{z})$ est optimale.
Soit $(\alpha^{'}, b^{'})$ une autre solution, supposons optimale.
Or $(\alpha, b, \bar{z})$ est optimale, on obtient
```math
\sum_{i=0}^{n-1} max | \alpha x_i + b - y_i | \leq \sum_{i=0}^{n-1} max | \alpha^{'} x_i + b^{'} - y_i |, \quad \forall (\alpha, b)
```
qui est une contradiction, alors $(\alpha, b)$ est bien optimale.

### 3. Visualisez le résultat de l’interpolation en norme 1 et en norme infini en utilisant le module matplotlib.  
Norme1: L'interpolation en norme 1 est une méthode d'approximation de fonctions qui consiste à trouver une fonction simple qui approche au mieux une fonction donnée, en minimisant la somme des valeurs absolues des différences entre les deux fonctions. Donc on choisi la même façon dans le cours:moindres carrés pour obtenir son interpolation ,et en python,on choisi la fonction 'np.polyfit(x,y,deg)' dans module numpy.  
  
  
Norme infini:L'interpolation en norme infinie est une méthode d'approximation de fonctions qui consiste à trouver une fonction simple qui approche au mieux une fonction donnée, en minimisant l'erreur maximale entre les deux fonctions.  
  
  
#### Les code suivant :  

```python
iimport numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n = 99
x = np.linspace(0, 10, n)
y = 3* x + np.random.normal(0, 2, n)

#Pour assurer le succès de l'interpolation, nous n'utilisons pas "np.random" ici.
#On générons plutôt quelques points qui ont une relation linéaire, en supposant que leur relation linéaire est y = 3x + b.
# Calcul de la régression linéaire

a, b = np.polyfit(x, y, 1)#moindre carré ,deg = 1
z = a * x + b
inter1 = np.max(np.abs(z - y))

# Calcul de la différence en norme infi
interf = np.min(inter1)

# Tracé des points de données et des lignes de régression

plt.scatter(x, y, label='Données originales')#scatter les points
plt.plot(x, z, color='red', label='interpolation linéaire en norme 1')

#plt.plot(x,inter1,color='blue')

plt.plot([x[0], x[-1]], [z[0] - interf, z[-1] - interf], color='green', label='interpolation linéaire en norme infini')

#[x[0], x[-1]], [z[0] - interf, z[-1] - interf c'est le proint on veut trouver qui a la distance max
# avec cette point on peut déterminer l'interpolation infini 

plt.legend()
plt.title('interpolation en normes 1 et infini')
plt.show()
```  

#### L’image du résultats  

<img width="752" alt="image 1" src="https://user-images.githubusercontent.com/106167157/219715975-d04f9d90-2ab0-463b-91f0-2dadb51c406b.png">

