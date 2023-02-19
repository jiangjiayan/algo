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

## TP1.5.2 Un problème de séparation /classification  
### On a n points rouges et n points verts dans le plan reél $R^2$
### 1.Est-il possible de tracer une droite qui sépare les points au sens où tous les points de la même couleur sont du même côté de la droite?  
  
  Il n'est pas toujours possible de tracer une ligne séparant les points rouges et verts sur le plan réel. Cela dépend de la répartition des points.Les exemples suivants illustrent les cas de séparabilité et de non-séparabilité à l'aide de Python.   
    
   Dans ce cas, nous générons aléatoirement quelques points rouges et verts, répartis uniformément et de manière chaotique sur un graphique en nuage, ils sont non-séparables:  
     
```python
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
plt.show()
```

<img width="752" alt="passéparé" src="https://user-images.githubusercontent.com/106167157/219867876-1a45ed54-c083-481d-b651-603f858434ca.png">  

Lorsque nous pouvons voir à l'œil nu qu'ils sont répartis de manière régulière de part et d'autre d'une ligne droite, alors ils sont séparables.  

```python
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
```  

<img width="752" alt="séparé" src="https://user-images.githubusercontent.com/106167157/219867975-f42023ca-a80b-4585-923d-66af88548450.png">  

### 2.S'il une telle droitisations existe ,est-il possible d'en choisir une qui est à mi-chemin entre le point rouge et le point vert les plus proches ?  
Oui, c'est possible de choisir une droite qui passe par le point milieu entre le point rouge et le point vert les plus proches.Cependant, cette méthode ne garantit pas qu'il y aura une telle droite qui passe par le point milieu pour tous les ensembles de points rouges et verts.Donc,on ne considère que le cas séparable.  
  
  La condition de contrainte est qu'on assure les points rouge sont au-dessus de cette lignes et les verts sont au-dessous(Comme l'image précédente). C’est à dire si on fait cette ligne est f(x)= ax +b,les points rouges $\geq$ f(x), et les points verts $\leq$ f(x).
  
  À l'aide votre exemple,pour résoudre cette problème ,on va ajouter deux valeurs aussi,y et c,y représente la distance de chaque point à cette ligne.On a  ajouté C pour m'assurer que la distance entre chaque point et la ligne est égale(c’est à dire mi-chemin).  
    
    Donc on résout le problème comme suivant :  
    
```math
\begin{align*}
&max :c \\
&a x_i + b - y_i \geq c  (i: point rouge)\\ 
&a x_i + b - y_i \leq -c (i:point verts)\\
&y_i \geq 0
\end{align*}
```
    
### 3.Il peut être impossible de séparer les points avec une droite .Dans ce cas,est-il possible de trouver un polynôme de degré 2,3....qui sépare les points ?
Si les points rouges et verts sont mélangés et qu'il n'y a pas de tendance claire à les séparer, il peut être impossible de trouver un polynôme de degré 2 ou supérieur qui les sépare.Si leur distribution est régulière， il est possible de trouver un polynôme de degré 2, 3, ... qui peut séparer les points s'ils sont séparables et qu'une droite ne peut pas les séparer. On fait un exemple suivant en degré 2(même si on peut le trouver ,il est non-linéaire ):  
1.On assure les points rouge sont au-dessus de cette lignes et les verts sont au-dessous.Et la fonction de la parabole est f(x) = $ax^2$ +bx+c,pour tout $f(x)\geq y$ (les points rouges),et pour tout $f(x)\leq y$ (les points verts)  
2.Avec la façon de 'quadratic programming',son norme est :  
```math
\begin{align*}
&min x 
&\frac{1}{2} x^T Gx+ x^Tc
\end{align*}
```  
3.On ajouter deux variables aussi,y:il représente la carré de la distance ,et d est une valeur limite.  
4.La fonction objectif est :
```math
\begin{align*}
&max :d \\
&a x_i^2 + bx_i +c- y_i \geq d  (i: point rouge)\\ 
&a x_i^2 + bx_i +c- y_i \leq -d (i:point verts)\\
&y_i \geq 0
\end{align*}
```



### 4.En $R^n$,peut-on chercher un hyperplan affine plutôt qu'une droite(à savoir {x| $a^T$ x=b})?
/solution/
