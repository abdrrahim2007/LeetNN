### Chapitre 2 : Polynômes à une indéterminée

Université Cadi Ayyad Faculté des Sciences Semlalia Filière TC-INFO - S1 Année Universitaire 2025 − 2026

![](_page_0_Picture_2.jpeg)

14 octobre 2025

![](_page_0_Picture_4.jpeg)

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_1_Picture_11.jpeg)

### Polynômes à une indéterminée

Dans tout ce chapitre on note K l'ensemble des nombres réels ou l'ensembe des nombres complexes.

#### Définition

Un polynôme à coefficients dans  $\mathbb{K}$  est une suite  $(a_n)$  d'éléments de  $\mathbb{K}$ nulle à partir d'un certain rang.

$$(a_n) = (a_0, a_1, \ldots, a_k, 0, 0, \ldots)$$

Le scalaire  $a_i$  est dit le coefficient d'indice i du polynôme  $(a_n)$ .

#### Notations

On note

- 1 le polynôme (1, 0, 0, . . . ).
- X le polynôme (0, 1, 0, 0, ...).
- $\bigcirc$   $X^k$  le polynôme  $(0,\ldots,0,1,0,0,\ldots)$  où 1 est placé dans la position d'indice k.

Avec ces notations, si  $P=(a_0,a_1,\ldots,a_n,\ldots)$  est un polynôme on a

$$P = a_0(1,0,0,\ldots) + a_1(0,1,0,0,\ldots) + \cdots + a_n(0,\ldots,0,1,0,0,\ldots)$$
  
=  $a_0.1 + a_1.X + \cdots + a_n.X^n$ 

### Polynômes à une indéterminée

Dans la suite on note  $\mathbb{K}[X]$  l'ensemble des polynômes à coefficients dans  $\mathbb{K}$ .

#### Remarques

- **1** Un polynôme  $P = a_0 + a_1 X + \cdots + a_n X^n \in \mathbb{K}[X]$  est nul si, et seulement si, tous les coefficients  $a_i$  sont nuls.
- Plus généralement, deux polynômes  $P=a_0+a_1X+\cdots+a_nX^n\in\mathbb{K}[X]$  et  $Q=b_0+b_1X+\cdots+b_mX^m\in\mathbb{K}[X]$  sont égaux si, et seulement si, pour tout  $i\geq 0, a_i=b_i.$

#### Définition

Soit  $P = a_0 + a_1 X + \cdots + a_n X^n \in \mathbb{K}[X]$ , avec  $a_n \neq 0$ .

On appelle degré de P, que l'on note  $\deg(P)$ , l'entier naturel n. Le coefficient  $a_n$  sera dit le coefficient dominant de P. Lorsque  $a_n=1$  on dit que P est unitaire.

Par convention, le degré du polynôme nul est  $-\infty$ .

![](_page_3_Picture_9.jpeg)

#### Remarque

Soit P = a<sup>0</sup> + a1X + · · · + anX <sup>n</sup> ∈ K[X], n = deg(P). Alors pour tout m ≥ n le polynôme P est aussi égal à

$$a_0 + a_1 X + \cdots + a_n X^n + 0 X^{n+1} + \cdots + 0 X^m$$

On définit dans K[X] les opérations d'addition, de multiplication par un scalaire et de multiplication comme suit : Soit P = a<sup>0</sup> + a1X + · · · + anX n et Q = b<sup>0</sup> + b1X + · · · + bmX <sup>m</sup> deux polynômes de K[X].

<sup>1</sup> Somme :

Si m ≥ n on pose

$$P+Q=(a_0+b_0)+(a_1+b_1)X+\cdots+(a_n+b_n)X^n+b_{n+1}X^{n+1}+\cdots+b_mX^m.$$

Si n ≥ m on pose

$$P+Q=(a_0+b_0)+(a_1+b_1)X+\cdots+(a_m+b_m)X^m+b_{m+1}X^{m+1}+\cdots+b_nX^n.$$

<sup>2</sup> Multiplication par un scalaire : Pour tout λ ∈ K on définit λP = λa<sup>0</sup> + λa1X + · · · + λanX n .

![](_page_4_Picture_10.jpeg)

3. Produit : P × Q = c<sup>0</sup> + c1X + · · · + ckX <sup>k</sup> + · · · + cn+mX <sup>n</sup>+<sup>m</sup>. avec

$$c_k = a_0 b_k + a_1 b_{k-1} + \dots + a_k b_0 = \sum_{\ell=0}^k a_\ell b_{k-\ell}, \ \ 0 \le k \le n+m.$$

#### Proposition

Soient P et Q deux polynômes de K[X]. On a :

- <sup>1</sup> deg(P + Q) ≤ max{deg(P), deg(Q)},
- <sup>2</sup> deg(PQ) = deg(P) + deg(Q).

#### Remarques

- <sup>1</sup> Soit P = 1 + X − X 2 et Q = 1 + X + X 2 . On a P + Q = 2 + 2X et donc deg(P + Q) = 1. Ceci montre que le degré de la somme de deux polynômes peut être strictement inférieur au maximum de leurs degrés.
- <sup>2</sup> Si deg(P) 6= deg(Q) alors deg(P + Q) = max{deg(P), deg(Q)}.

#### Exercice

Soient P, Q ∈ K[X] tels que PQ = 0. Montrer que P = 0 ou Q = 0.

### Solution :

L'égalité PQ = 0 implique deg(PQ) = −∞ et donc deg(P) + deg(Q) = −∞. Alors deg(P) = −∞ ou deg(Q) = −∞. Ceci montre que P = 0 ou Q = 0.

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_7_Picture_11.jpeg)

La division euclidienne dans l'ensemble des entiers relatifs Z s'étend naturellement à l'anneau K[X].

### Définition

Soit A, B ∈ K[X]. On dit que A divise B s'il existe un polynôme Q ∈ K[X] tel que B = QA. On note A|B.

### Exemples

- <sup>1</sup> Dans R[X] on a X <sup>3</sup> − 1 = (X − 1)(X <sup>2</sup> + X + 1). Donc X <sup>2</sup> + X + 1 divise X <sup>3</sup> − 1.
- <sup>2</sup> Dans C[X] on a X <sup>4</sup> − 1 = (X <sup>2</sup> − 1)(X <sup>2</sup> + 1) = (X <sup>2</sup> − 1)(X − i)(X + i). Donc X + i divise X <sup>4</sup> − 1.

### Théorème

Soit A, B ∈ K[X] deux polynômes, avec B 6= 0. Alors il existe un unique couple de polynômes (Q, R) vérifiant

$$A = BQ + R$$
 et  $deg(R) < deg(B)$ .

Le polynôme Q (respectivement R) s'appelle le quotient (respectivement le reste) de la division euclidienne de A par B.

#### Remarque

Dans le dernier théorème la relation A = BQ + R montre que B divise A si, et seulement si R = 0.

#### Exemple 1

Effectuons la division euclidienne du polynôme A = X <sup>3</sup> + X <sup>2</sup> − 1 par le polynôme B = X − 1.

$$\begin{array}{c|ccccc}
X^3 & +X^2 & -1 & X & -1 \\
-X^3 & +X^2 & & & \\
\hline
2X^2 & & -1 & & \\
& & & & \\
\hline
-2X^2 & +2X & -1 & & \\
\hline
2X & -1 & & & \\
\hline
-2X & +2 & & & \\
\hline
+1 & & & & \\
\end{array}$$

On obtient alors Q = X <sup>2</sup> + 2X + 2 et R = 1.

$$X^3 + X^2 - 1 = (X - 1)(X^2 + 2X + 2) + 1.$$

![](_page_10_Picture_6.jpeg)

### Exemples

Effectuons la division euclidienne du polynôme A = X <sup>5</sup> − 1 par le polynôme B = X <sup>2</sup> − 1.

$$\begin{array}{c|ccccc}
X^5 & -1 & X^2 & -1 \\
-X^5 & +X^3 & -1 & X^3 & +X \\
\hline
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & \\
& & & & & & \\
\hline
& & & & & & \\
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & & & \\
\hline
& & & &$$

On obtient alors Q = X <sup>3</sup> + X et R = X − 1.

$$X^5 - 1 = (X^2 - 1)(X^3 + X) + X - 1.$$

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- 3 Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_12_Picture_11.jpeg)

#### Définition

Soit A, B ∈ K[X], avec A 6= 0 ou B 6= 0. On appelle le plus grand diviseur commun de A et B, que l'on note pgcd(A, B), l'unique polynôme unitaire de plus grand degré qui divise à la fois A et B.

L'algorithme d'Euclide pour les entiers s'étend aux polynômes et permet de déterminer le  $\operatorname{pgcd}$  de deux polynômes.

#### Algortihme d'Euclide.

Soit A, B des polynômes, avec  $B \neq 0$ . On effectue les divisions euclidiennes successives,

$$egin{array}{lcl} A & = & BQ_1 + R_1 & \deg(R_1) < \deg(B) \\ B & = & R_1Q_2 + R_2 & \deg(R_2) < \deg(R_1) \\ R_1 & = & R_2Q_3 + R_3 & \deg(R_3) < \deg(R_2) \\ & dots & & & & & & & & & & & & & & & & & & &$$

Le pgcd est le dernier reste non nul  $R_k$  (rendu unitaire).

![](_page_14_Picture_6.jpeg)

#### Exemple 1

Calculer pgcd(X <sup>5</sup> − 1, X <sup>3</sup> − 1). Appliquons l'algorithme d'Euclide :

$$X^5 - 1 = (X^3 - 1) \times X^2 + X^2 - 1$$
  
 $X^3 - 1 = (X^2 - 1) \times X + X - 1$   
 $X^2 - 1 = (X - 1) \times (X + 1) + 0$ 

Le pgcd est le dernier reste non nul, donc pgcd(X <sup>5</sup> − 1, X <sup>3</sup> − 1) = X − 1.

#### Exemple 2

• Calculer  $\operatorname{pgcd}(X^5 + X^4 + 2X^3 + X^2 + X + 2, X^4 + 2X^3 + X^2 - 4)$ . Appliquons l'algorithme d'Euclide :

Apprint and the definition of Euclide . 
$$X^5 + X^4 + 2X^3 + X^2 + X + 2 = (X^4 + 2X^3 + X^2 - 4)(X - 1) + 3X^3 + 2X^2 + 5X - 2$$
 
$$X^4 + 2X^3 + X^2 - 4 = (3X^3 + 2X^2 + 5X - 2) \times \frac{1}{9}(3X + 4) - \frac{14}{9}(X^2 + X + 2)$$
 
$$3X^3 + 2X^2 + 5X - 2 = (X^2 + X + 2)(3X - 1) + 0$$
 Ainsi 
$$\operatorname{pgcd}(X^5 + X^4 + 2X^3 + X^2 + X + 2, X^4 + 2X^3 + X^2 - 4) = X^2 + X + 2.$$

#### Exemple 3

Calculer pgcd(2X − 2X − X + 1, 2X + 2X + 3X + 2X + 1). Appliquons l'algorithme d'Euclide : X − 2X − X + 1 = (2X + 2X + 3X + 2X + 1) × 1 + (−4X − 4X − 2X) X + 2X + 3X + 2X + 1 = (−4X − 4X − 2X) × (− X) + 2X + 2X + 1 −4X − 4X − 2X = (2X + 2X + 1)(−2X) + 0 Ainsi Le dernier reste non nul est 2X + 2X + 1 et donc pgcd(2X −2X −X +1, 2X +2X +3X +2X +1) = X +X + .

### Polynômes premiers entre eux

#### Définition

On dit que deux polynômes A et B sont premiers entre eux lorsque pgcd(A, B) = 1.

### Exemple 1

Montrons que les polynômes X <sup>3</sup> − 1 et X <sup>2</sup> + 1 sont premiers entre eux.

Appliquons l'algorithme d'Euclide pour calculer pgcd(X <sup>3</sup> − 1, X <sup>2</sup> + 1).

$$X^{3} - 1 = (X^{2} + 1)(X) - X - 1$$

$$X^{2} + 1 = (-X - 1)(-X + 1) + 2$$

$$-X - 1 = (-\frac{1}{2}X - \frac{1}{2}) \times 2 + 0$$

Ainsi pgcd(X <sup>3</sup> − 1, X <sup>2</sup> + 1) = 1.

![](_page_18_Picture_8.jpeg)

## Polynômes premiers entre eux

### Exemple 2

Montrons que les polynômes X <sup>3</sup> + 1 et X <sup>2</sup> + X + 1 sont premiers entre eux.

Appliquons l'algorithme d'Euclide pour calculer pgcd(X <sup>3</sup> + 1, X <sup>2</sup> + X + 1).

$$X^3 + 1 = (X^2 + X + 1)(X - 1) + 2$$
  
 $X^2 + X + 1 = (\frac{1}{2}X^2 + \frac{1}{2}X + \frac{1}{2}) \times 2 + 0$ 

Ainsi pgcd(X <sup>3</sup> + 1, X <sup>2</sup> + X + 1) = 1.

![](_page_19_Picture_6.jpeg)

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_20_Picture_11.jpeg)

### Racines d'un polynôme

#### Notation

Soit  $P=a_0+a_1X+\cdots+a_nX^n\in\mathbb{K}[X].$  On note  $\tilde{P}$  la fonction polynomiale associée à P:

$$\tilde{P}: \mathbb{K} \to \mathbb{K}$$
  
 $x \mapsto a_0 + a_1 x + \dots + a_n x^n.$ 

Pour un scalaire  $x \in \mathbb{K}$  on note P(x) l'évaluation de  $\tilde{P}$  en x :  $P(x) = \tilde{P}(x)$ .

#### **Définition**

Soit  $P \in \mathbb{K}[X]$  et  $\alpha \in \mathbb{K}$ . On dit que  $\alpha$  est une racine de P si  $P(\alpha) = 0$ .

#### **Exemples**

- 1 est une racine de  $X^4 1$ .
- ② Pour tout entier naturel n et tout entier  $0 \le k \le n-1$ , le complexe  $e^{\frac{2ik\pi}{n}}$  est une racine du polynôme  $X^n-1$ .
- **3** 0 est une racine du polynôme de la forme  $P = a_1 X + \cdots + a_n X^n$ .

## Racines d'un polynôme

### Proposition

Soit P ∈ K[X] et α ∈ K. Alors α est une racine de P si, et seulement si X − α divise P.

#### Preuve :

Montrons l'implication directe. On sait qu'il existe un couple unique de polynômes (Q, R) vérifiant P = (X − α)Q + R et deg(R) < deg(X − α). Puisque deg(X − α) = 1 il vient deg(R) = 0 ou deg(R) = −∞ ; autrement dit, R est une constante non nulle ou R = 0. Mais P(α) = R(α) = 0 ce qui montre que R = 0. La réciproque est évidente.

## Racines d'un polynôme

#### Définition

Soit P ∈ K[X], α ∈ K et m ∈ N ? . On dit que α est une racine de P, de multiplicité m, si (X − α) <sup>m</sup> divise P et (X − α) <sup>m</sup>+<sup>1</sup> ne divise pas P. Si m = 1 (respectivement m = 2) on parle de racine simple (respectivement double) et lorsque m > 2 on dit que α est une racine multiple de P.

#### Proposition

Soit P ∈ K[X] et α ∈ K. Alors α est une racine de P de multiplicité m si, et seulement si, il existe un polynôme Q ∈ K[X] tel que P = (X − α) <sup>m</sup>Q et Q(α) 6= 0.

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- 6 Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_24_Picture_11.jpeg)

#### Définition

Soit P = a<sup>0</sup> + a1X + · · · + anX <sup>n</sup> ∈ K[X]. Le polynôme dérivé de P est le polynôme, que l'on note P 0 , défini par

$$P' = a_1 + 2a_2X + \dots + na_nX^{n-1} = \sum_{k=1}^n ka_kX^{k-1}.$$

#### Exemples

- <sup>1</sup> Soit P = X <sup>4</sup> + X <sup>3</sup> + 2X + 3. Alors P <sup>0</sup> = 4X <sup>3</sup> + 3X <sup>2</sup> + 2.
- <sup>2</sup> Soit P = X <sup>n</sup> − 1. Alors P <sup>0</sup> = nX<sup>n</sup>−<sup>1</sup> .

#### Remarques

Soit P ∈ K[X].

- <sup>1</sup> Si deg(P) > 0 on a deg(P 0 ) = deg(P) − 1.
- <sup>2</sup> P est constante si, et seulement si, P <sup>0</sup> = 0.

![](_page_25_Picture_11.jpeg)

#### Proposition

Soient P, Q ∈ K[X] et α, β ∈ K. Alors

- <sup>1</sup> (αP + βQ) <sup>0</sup> = αP <sup>0</sup> + βQ<sup>0</sup> .
- <sup>2</sup> (PQ) <sup>0</sup> = P <sup>0</sup>Q + PQ<sup>0</sup> .

### Définition

Soit P ∈ K[X] et n ∈ N. La dérivée n-ième (ou d'ordre n) de P, que l'on note P (n) , est le polynôme défini par récurrence :

- P (0) = P,
- P (k+1) = (P (k) ) <sup>0</sup> ∀k ∈ N.

### Proposition (Formule de Taylor )

Soit P ∈ K[X], a ∈ K. On suppose que deg(P) ≤ n. Alors

$$P = \sum_{k=0}^{n} \frac{P^{(k)}(a)}{k!} (X - a)^{k}.$$

![](_page_26_Picture_12.jpeg)

#### Exercice

Pour un entier naturel  $n \ge 3$  déterminer le reste R de la division euclidienne de  $X^n$  par  $(X - a)^3$ .

La formule de Taylor utilisée lorsque  $P = X^n$  montre que

$$X^{n} = P(a) + P'(a)(X - a) + \frac{P''(a)}{2}(X - a)^{2} + \sum_{k=3}^{n} \frac{P^{(k)}(a)}{k!}(X - a)^{k}.$$

Donc

$$X^{n} = a^{n} + na^{n-1}(X - a) + \frac{n(n-1)a^{n-2}}{2}(X - a)^{2} +$$
$$(X - a)^{3} \left( \sum_{k=3}^{n} \frac{P^{(k)}(a)}{k!} (X - a)^{k-3} \right).$$

Alors l'unicité du quotient et du reste de la division euclidienne permet de conclure que

 $C = a^n + na^{n-1}(X - a) + \frac{n(n-1)a^{n-2}}{\text{Cours d'Algèbre 1, S}_1}(X - a)$ 

La formule de Taylor permet d'avoir un critère simple pour déterminer la multiplicité d'une racine d'un polynôme.

#### Proposition

Soit P ∈ K[X], a ∈ K et m ∈ N ? . Alors α est une racine de P de multiplicité m si, et seulement si P(a) = P 0 (a) = · · · = P (m−1) (a) = 0 et P (m) (a) 6= 0.

#### Exemples

- <sup>1</sup> 0 est une racine de multiplicité 3 du polynôme P = X <sup>3</sup> + 2X <sup>5</sup> − X 7 . En effet on a P(0) = P 0 (0) = P <sup>00</sup>(0) = 0 et P (3) (0) 6= 0.
- <sup>2</sup> Une racine n-ième de l'unité α, qui est racine du polynôme P = X <sup>n</sup> − 1, est simple puisque P(α) = α <sup>n</sup> − 1 = 0 et P 0 (α) = nα <sup>n</sup>−<sup>1</sup> 6= 0.

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- 6 Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_29_Picture_11.jpeg)

### Polynôme conjugué

Soit P = a<sup>0</sup> + a1X + · · · + anX <sup>n</sup> ∈ C[X]. Le conjugué de P est le polynôme P ∈ C[X] défini par

$$\overline{P} = \overline{a_0} + \overline{a_1}X + \cdots + \overline{a_n}X^n.$$

On a le résultat important :

#### Proposition

Soit P ∈ C[X] et α ∈ C une racine de P. Alors : α est une racine de P de multiplicité m si, et seulement si, α est une racine de P de multiplicité m.

En remarquant q'un polynôme P de R[X] coincide avec son conjugué (P = P), on obtient :

#### Corollaire

Soit P ∈ R[X] et α ∈ C une racine de P. Alors : α est une racine de P de multiplicité m si, et seulement si, α est une racine de P de multiplicité m.

![](_page_30_Picture_9.jpeg)

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- Exercices

![](_page_31_Picture_11.jpeg)

# Factorisation dans C[X]

Le théorème suivant est connu sous le nom de théorème de d'Alembert-Gauss ou théorème fondamental d'algèbre :

### Theorème

Tout polynôme à coefficients complexes de degré n ≥ 1 admet au moins une racine dans C.

En utilisant le théorème de d'Alembert-Gauss on obtient le théorème de factorisation de polynômes de C[X] :

#### Theorème

Soit P un polynôme de C[X] de degré n ≥ 1. Alors P s'écrit sous la forme suivante :

$$P = \lambda (X - \alpha_1)^{m_1} (X - \alpha_2)^{m_2} \cdots (X - \alpha_r)^{m_r},$$

où λ est le coefficient dominant de P et α1, α2, . . . , α<sup>r</sup> sont les racines distinctes de P de multiplicités respectives m1, m2, . . . , m<sup>r</sup> . Cette écriture de P s'appelle la décomposition de P en produit de facteurs irréductibles dans C[X].

## Factorisation dans $\mathbb{C}[X]$

#### Remarques

Décomposer un polynôme en produit de facteurs irréductible revient à déterminer ses racines complexes avec leurs multiplicités.

#### **Exemples**

- $2 X^2 + 1 = (X i)(X + i).$
- $2X^2 + X + 1 = (X j)(X \bar{j}) \text{ où } j = e^{\frac{2i\pi}{3}} = \frac{-1}{2} + \frac{i\sqrt{3}}{2}.$
- $X^3 + 1 = (X+1)(X e^{\frac{i\pi}{3}})(X e^{\frac{-i\pi}{3}}) = (X+1)(X \frac{1}{2} \frac{\sqrt{3}}{2}i)(X \frac{1}{2} + \frac{\sqrt{3}}{2}i).$

## Factorisation dans $\mathbb{R}[X]$

Le théorème de d'Alembert-Gauss n'est pas vrai sur  $\mathbb R$  dans le sens où il existe des polynômes à coefficients dans  $\mathbb R$  qui n'ont pas de racines dans  $\mathbb R$ . Un exemple simple est donné par le polynôme  $X^2+1$ . Ceci implique que dans  $\mathbb R[X]$  on aura une autre forme de factorisation de polynômes :

#### Définition

On appelle discriminant d'un polynôme  $aX^2 + bX + c \in \mathbb{R}[X]$ , le réel  $b^2 - 4ac$ . Le polynôme  $aX^2 + bX + c \in \mathbb{R}[X]$  est de discriminant strictement négatif si  $b^2 - 4ac < 0$ .

#### Theorème

Soit P un polynôme de  $\mathbb{R}[X]$  de degré  $n \ge 1$ . Alors P s'écrit sous la forme suivante :

$$P = \lambda (X - \alpha_1)^{m_1} (X - \alpha_2)^{m_2} \cdots (X - \alpha_r)^{m_r} Q_1^{\ell_1} \cdots Q_s^{\ell_s},$$

où les  $\alpha_i$  sont les racines réelles distinctes de P, de multiplicités respectives  $m_i$ , et les  $Q_i \in \mathbb{R}[X]$  sont des polynômes de degré 2 de discriminant strictement négatif.

# Factorisation dans R[X]

### Exemples

- X − 1 = (X − 1)(X + X + 1).
- X + 1 = X + 2X + 1 − 2X = (X + 1) − 2X = (X − √ X + 1)(X + √ X + 1).
- X + 1 = (X + 1)(X − X + 1).

### Remarque

Soit α ∈ C\R c'est à dire Im(α) 6= 0. Alors le polynôme (X − α)(X − α) = X − 2Re(α)X + |α| est un polynôme de R[X] de degré 2 de discriminant 4Re(α) − 4|α| = −4Im(α) qui est strictement négatif.

## Factorisation dans $\mathbb{R}[X]$

Rappelons que si  $\alpha \in \mathbb{C} \backslash \mathbb{R}$  est une racine complexe d'un polynôme  $P \in \mathbb{R}[X]$ , de multiplicité m, alors  $\overline{\alpha}$  est une racine de P de même multiplicité m. Ceci nous permet de passer de la factorisation du polynôme P dans  $\mathbb{C}[X]$  à sa factorisation dans  $\mathbb{R}[X]$ .

#### Exemples

• Factorisons le polynôme  $X^5-1$  dans  $\mathbb{R}[X]$ . On sait que dans  $\mathbb{C}[X]$  on a :

$$X^{5}-1=(X-1)(X-e^{\frac{2i\pi}{5}})(X-e^{\frac{4i\pi}{5}})(X-e^{\frac{6i\pi}{5}})(X-e^{\frac{8i\pi}{5}}).$$

Puisque  $e^{\frac{6i\pi}{5}}=\overline{e^{\frac{4i\pi}{5}}}$  et  $e^{\frac{8i\pi}{5}}=\overline{e^{\frac{2i\pi}{5}}}$  il vient dans  $\mathbb{R}[X]$  :

$$X^{5}-1=(X-1)(X^{2}-2\operatorname{Re}(e^{\frac{2i\pi}{5}})X+1)(X^{2}-2\operatorname{Re}(e^{\frac{4i\pi}{5}})X+1).$$

Factorisons le polynôme  $X^4+1$  dans  $\mathbb{R}[X]$ . On a  $X^4+1=(X^2+i)(X^2-i)$ . Or les racines carrées de i sont  $\frac{1+i}{\sqrt{2}}$  et  $-\frac{1+i}{\sqrt{2}}$  et les racines carrées de -i sont  $\frac{1-i}{\sqrt{2}}$  et  $-\frac{1-i}{\sqrt{2}}$ . Donc

### Plan

- Polynômes à une indéterminée
- Division euclidienne
- Plus grand commun diviseur (pgcd)
- Racines d'un polynôme
- Polynômes dérivés
- Polynôme conjugué
- Factorisation de polynômes
  - Factorisation dans  $\mathbb{C}[X]$
  - Factorisation dans  $\mathbb{R}[X]$
- 8 Exercices

![](_page_37_Picture_11.jpeg)

### Exercices

#### Exercice

Soit P = X − 15X − 10X + 60X + 72.

- Montrer que −2 est une racine de P et déterminer sa multiplicité.
- En déduire la factorisation de P dans R[X].

#### Exercice

Soit P = 2X − 11X + 21X − 22X + 28X − 24.

- Montrer que 2 est une racine de P et déterminer sa multiplicité.
- En déduire la factorisation de P dans R[X] puis dans C[X].

#### Exercice

Soit 
$$P = X^6 - 6X^5 + 11X^4 - 12X^3 + 19X^2 - 6X + 9$$
.

- Montrer que 3 est une racine de P et déterminer sa multiplicité.
- En déduire la factorisation de P dans R[X] puis dans C[X].

#### Exercice

Soit 
$$P = X^6 - 2X^5 + 3X^4 - 4X^3 + 3X^2 - 2X + 1$$
.

- Montrer que 1 est une racine de P et déterminer sa multiplicité.
- En déduire la factorisation de P dans R[X] puis dans C[X].

Fin du chapitre 2