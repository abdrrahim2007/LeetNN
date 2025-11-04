# <span id="page-0-0"></span>Module d'algèbre 1

### Contenu du programme

- Chapitre 1 : Corps des nombres complexes
- Chapitre 2 : Polynômes à une indéterminée
- Chapitre 3 : Fractions rationnelles
- Chapitre 4 : L'espace euclidien R n
- Chapitre 5 : Espace affine de dimension finie
- Chapitre 6 : Géométrie dans le plan R
- Chapitre 7 : Géométrie dans l'espace R
- Chapitre 8 : Applications affines dans R et dans R

![](_page_0_Picture_10.jpeg)

![](_page_0_Picture_11.jpeg)

## Chapitre 1 : Nombres Complexes

Université Cadi Ayyad Faculté des Sciences Semlalia Filière TC-INFO - S1 Année Universitaire 2025 − 2026

![](_page_1_Picture_2.jpeg)

17 septembre 2025

![](_page_1_Picture_4.jpeg)

![](_page_1_Picture_5.jpeg)

## <span id="page-2-0"></span>Plan

- <sup>2</sup> [Corps des nombres complexes](#page-2-0)

- - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_2_Picture_11.jpeg)

![](_page_2_Picture_12.jpeg)

Soit  $\mathbb{R}$  le corps des nombres réels. On note  $\mathbb{R}^2$  l'ensemble des couples de nombres réels :  $\mathbb{R}^2 = \{(a,b) : a,b \in \mathbb{R}\}.$ 

#### Définition

On appelle corps des nombres complexes, que l'on note  $\mathbb{C}$ , l'ensemble  $\mathbb{R}^2$  muni des opérations + et  $\times$ , définies de la manière suivante :

$$\forall (a,b), (a',b') \in \mathbb{R}^2,$$

- Opération d'addition + : (a, b) + (a', b') = (a + a', b + b'),
- Opération de multiplication  $\times$  :  $(a,b) \times (a',b') = (aa'-bb',ab'+a'b)$ .

![](_page_3_Picture_7.jpeg)

![](_page_3_Picture_8.jpeg)

### Notation :

- <sup>1</sup> On veut que le corps des nombres complexes C contienne le corps des nombres réels. Pour cela, pour tout réel a ∈ R, on identifie a avec le nombre complexe (a, 0). On note alors a le nombre complexe (a, 0).
- <sup>2</sup> On note i le nombre complexe (0, 1).

Avec les notations précédentes, on obtient :

#### Proposition

Soit a, b ∈ R. Alors :

- <sup>1</sup> (0, b) = i × b = b × i.
- <sup>2</sup> (a, b) = a + i × b et i × i = −1.

![](_page_4_Picture_9.jpeg)

![](_page_4_Picture_10.jpeg)

### <span id="page-5-0"></span>Preuve

- <sup>1</sup> On a (0, b) = (b, 0) × (0, 1) = (0, 1) × (b, 0). Donc (0, b) = i × b = b × i.
- <sup>2</sup> On a (a, b) = (a, 0) + (0, b) = a + i × b.
- <sup>3</sup> On a (0, 1) × (0, 1) = (1, 0). Donc i × i = −1.

### Remarque

Dans la suite, on convient de noter zz<sup>0</sup> le nombre complexe obtenu par la multiplication des deux nombres complexes z et z 0 .

### Notation

On note a + ib ou a + bi le nombre complexe z = (a, b). Cette écriture s'appelle la forme algébrique de z. Lorsque a = 0 on dit que z est un imaginaire pur et on écrit z ∈ iR.

![](_page_5_Picture_9.jpeg)

![](_page_5_Picture_10.jpeg)

Notation Avec les conventions précédentes, l'addition et la multiplication deviennent pour les nombres complexes :

$$\forall z = a + ib, z' = a' + ib' \in \mathbb{C},$$

- Opération d'addition + : z + z <sup>0</sup> = (a + a 0 ) + i(b + b 0 ),
- Opération de multiplication × : zz<sup>0</sup> = (aa<sup>0</sup> − bb<sup>0</sup> ) + i(ab<sup>0</sup> + a <sup>0</sup>b).

### Remarques

- <sup>1</sup> Un nombre complexe z = a + ib est nul (z = 0) si, et seulement si a = b = 0.
- <sup>2</sup> Pour tout nombre complexe z, on a z + 0 = 0 + z = z et z1 = 1z = z.
- <sup>3</sup> Tout nombre complexe z = a + ib admet un opposé noté −z = −a − ib.
- <sup>4</sup> Tout nombre complexe non nul z = a + ib admet un inverse noté

$$\frac{1}{z} = \frac{a}{a^2 + b^2} - i \frac{b}{a^2 + b^2}.$$

![](_page_6_Picture_11.jpeg)

![](_page_6_Picture_12.jpeg)

### Proposition

On a les proporiétés suivantes :

- <sup>1</sup> Les deux opérations définies sur C sont associatives et commutatives.
- <sup>2</sup> L'opération × est distributive par rapport à l'opération + :

$$\forall z, z', z'' \in \mathbb{C}$$
 :  $z(z' + z'') = zz' + zz''$ .

![](_page_7_Picture_6.jpeg)

![](_page_7_Picture_7.jpeg)

Les formules suivantes sont d'une importance majeure dans la suite. Soit z1, z<sup>2</sup> ∈ C et soit n ∈ N.

<sup>1</sup> Formule du binôme :

$$(z_1+z_2)^n=\sum_{k=0}^n C_n^k z_1^k z_2^{n-k} \qquad (C_n^k=\frac{n!}{k!(n-k)!}).$$

<sup>2</sup> Formule de factorisation :

$$z_1^n - z_2^n = (z_1 - z_2) \left( \sum_{k=0}^{n-1} z_1^{n-1-k} z_2^k \right).$$

<sup>3</sup> Si z<sup>1</sup> 6= 1 alors P<sup>n</sup> k=0 z k <sup>1</sup> = 1−z n+1 1 1−z<sup>1</sup> .

![](_page_8_Picture_6.jpeg)

![](_page_8_Picture_7.jpeg)

## <span id="page-9-0"></span>Plan

- <sup>3</sup> [Partie réelle, partie imaginaire et conjugaison](#page-9-0)

- - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_9_Picture_11.jpeg)

![](_page_9_Picture_12.jpeg)

# Partie réelle, partie imaginaire et conjugaison

### Définition

Soit z = a + ib un nombre complexe.

- <sup>1</sup> On appelle partie réelle de z, que l'on note Re(z), le nombre réel a.
- <sup>2</sup> On appelle partie imaginaire de z, que l'on note Im(z), le nombre réel b.
- <sup>3</sup> On appelle conjugué de z, que l'on note z, le nombre complexe défini par z = a − ib.

#### Remarques

Soit z, z <sup>0</sup> deux nombres complexes. Alors on a :

- <sup>1</sup> z = z 0 si, et seulement si, Re(z) = Re(z 0 )et Im(z) = Im(z 0 ).
- <sup>2</sup> z ∈ R si, et seulement si, Im(z) = 0.
- <sup>3</sup> z ∈ iR si, et seulement si, Re(z) = 0.

![](_page_10_Picture_11.jpeg)

![](_page_10_Picture_12.jpeg)

# <span id="page-11-0"></span>Partie réelle, partie imaginaire et conjugaison

### Proposition

Soit z, z <sup>0</sup> deux nombres complexes. On a les propriétés suivantes :

<sup>1</sup> Re(z) = <sup>z</sup>+<sup>z</sup> 2 et Im(z) = <sup>z</sup>−<sup>z</sup> 2i ,

<sup>2</sup> z = z si, et seulement si, z ∈ R.

<sup>3</sup> z = −z si, et seulement si, z ∈ iR.

$$\overline{z+z'} = \overline{z} + \overline{z'} \text{ et } \overline{zz'} = \overline{z}\overline{z'} .$$

<sup>5</sup> Si z <sup>0</sup> 6= 0 on a

$$\overline{\left(\frac{z}{z'}\right)} = \frac{\overline{z}}{\overline{z'}}.$$

![](_page_11_Picture_9.jpeg)

![](_page_11_Picture_10.jpeg)

# Partie réelle, partie imaginaire et conjugaison

#### Exercice

- <sup>1</sup> Soit z = a + ib un nombre complexe non nul. Donner la forme algébrique de <sup>1</sup> z .
- <sup>2</sup> Donner les formes algébriques des nombres complexes suivants :

$$z_1 = \frac{3+4i}{1+3i}, \quad z_2 = \frac{1+i}{1-i}.$$

#### Solution :

<sup>1</sup> On a zz = a <sup>2</sup> + b 2 . Donc

$$\frac{1}{z} = \frac{\overline{z}}{a^2 + b^2} = \frac{a}{a^2 + b^2} - i\frac{b}{a^2 + b^2}.$$

<sup>2</sup> On a :

$$z_1 = \frac{3+4i}{1+3i} = \frac{(3+4i)(1-3i)}{(1+3i)(1-3i)} = \frac{15-5i}{10} = \frac{3}{2} - \frac{1}{2}i.$$

$$z_2 = \frac{1+i}{1-i} = \frac{(1+i)^2}{(1-i)(1+i)} = \frac{2i}{2} = i.$$

![](_page_12_Picture_11.jpeg)

## <span id="page-13-0"></span>Plan

- <sup>4</sup> [Module d'un nombre complexe](#page-13-0)

- - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_13_Picture_11.jpeg)

![](_page_13_Picture_12.jpeg)

### Définition

Soit z = a + ib un nombre complexe. On appelle module de z, que l'on note |z|, le nombre réel positif, défini par :

$$|z|=\sqrt{a^2+b^2}.$$

### Remarque

Soit z = a + ib un nombre complexe. Si M est le point du plan R <sup>2</sup> de coordonnées (a, b) dans un repère orthonormé de centre O alors le module de z correspond à la distance entre O et M.

![](_page_14_Picture_6.jpeg)

![](_page_14_Picture_7.jpeg)

### Proposition

Soit z = a + ib un nombre complexe. Alors on a :

- $|z| = 0 \Longleftrightarrow z = 0 \text{ et } |z| = 1 \Longleftrightarrow z\overline{z} = 1.$
- $|z| = |\overline{z}|.$
- $|\operatorname{Re}(z)| \le |z| \text{ et } |\operatorname{Im}(z)| \le |z|.$

#### Preuve

0

$$|z| = 0 \iff a^2 + b^2 = 0 \iff a = b = 0 \iff z = 0.$$
  
 $|z| = 1 \iff a^2 + b^2 = 1 \iff z\overline{z} = 1.$ 

- ② On a  $|z| = \sqrt{a^2 + b^2} = |\overline{z}|$ .
- Ces inégalités découlent du fait que  $|a| \le \sqrt{a^2 + b^2}$  et  $|b| \le \sqrt{a^2 + b^2}$ .

![](_page_15_Picture_11.jpeg)

![](_page_15_Picture_12.jpeg)

### Proposition

Soit z, z <sup>0</sup> des nombres complexes. Alors on a :

- <sup>1</sup> |zz<sup>0</sup> | = |z||z 0 |.
- <sup>2</sup> Si z <sup>0</sup> 6= 0 alors | z z 0 | = |z| |z 0 .

Preuve On montre le premier point et le deuxième en découle aisément. Soit z = a +ib et z <sup>0</sup> = a <sup>0</sup> +ib<sup>0</sup> . On a zz<sup>0</sup> = (aa<sup>0</sup> −bb<sup>0</sup> ) +i(ab<sup>0</sup> +a <sup>0</sup>b) donc

$$|zz'| = \sqrt{(aa' - bb')^2 + (ab' + a'b)^2}$$

$$= \sqrt{a^2a'^2 - 2aa'bb' + b^2b'^2 + a^2b'^2 + 2aa'bb' + a'^2b^2}$$

$$= \sqrt{a^2a'^2 + b^2b'^2 + a^2b'^2 + a'^2b^2}$$

$$= \sqrt{(a^2 + b^2)(a'^2 + b'^2)}$$

$$= \sqrt{a^2 + b^2}\sqrt{a'^2 + b'^2}$$

$$= |z||z'|.$$

![](_page_16_Picture_7.jpeg)

![](_page_16_Picture_8.jpeg)

### Remarque

Pour deux nombres complexes z et z 0 , on a l'inégalité |z + z 0 | ≤ |z| + |z 0 |, appelée l'inégalité triangulaire.

![](_page_17_Picture_3.jpeg)

![](_page_17_Picture_4.jpeg)

## <span id="page-18-0"></span>Plan

- <sup>5</sup> [Exponentielle imaginaire](#page-18-0)

- - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_18_Picture_11.jpeg)

![](_page_18_Picture_12.jpeg)

### Définition

Soit θ ∈ R. On appelle exponentielle imaginaire de θ, que l'on note e iθ , le nombre complexe défini par :

$$e^{i\theta} = \cos(\theta) + i\sin(\theta).$$

### Proposition

On a les propriétés suivantes :

- <sup>1</sup> Soit z = e iθ , avec θ ∈ R. Alors |e iθ | = 1.
- <sup>2</sup> Soit z ∈ C, avec |z| = 1, alors il existe un réel θ tel que z = e iθ .

![](_page_19_Picture_8.jpeg)

![](_page_19_Picture_9.jpeg)

### Preuve

- <sup>1</sup> On a |e iθ <sup>2</sup> = cos(θ) <sup>2</sup> + sin(θ) <sup>2</sup> = 1.
- <sup>2</sup> Soit z = a + ib. L'identité |z| = 1 implique que a <sup>2</sup> + b <sup>2</sup> = 1 et par suite −1 ≤ a ≤ 1 et −1 ≤ b ≤ 1. Soit θ ∈ R tel que cos(θ) = a donc b <sup>2</sup> = 1 − a <sup>2</sup> = sin(θ) 2 . Il s'ensuit que (a = cos(θ), b = sin(θ)) ou (a = cos(θ), b = sin(θ)). Ceci montre que z = e <sup>i</sup><sup>θ</sup> ou z = e −iθ .

Le résultat suivant est très important :

### Proposition

Soit θ, θ<sup>0</sup> ∈ R. Alors

1

$$e^{i(\theta+\theta')}=e^{i\theta}e^{i\theta'}.$$

2

$$e^{i\theta} = e^{i\theta'} \iff \exists k \in \mathbb{Z} : \theta' = \theta + 2k\pi.$$

### Exemples

Soit θ ∈ R.

<sup>1</sup> e <sup>i</sup><sup>θ</sup> = 1 ⇐⇒ e <sup>i</sup><sup>θ</sup> = e <sup>i</sup><sup>0</sup> ⇐⇒ ∃k ∈ Z : θ = 2kπ.

<sup>2</sup> e <sup>i</sup><sup>θ</sup> = −1 ⇐⇒ e <sup>i</sup><sup>θ</sup> = e <sup>i</sup><sup>π</sup> ⇐⇒ ∃k ∈ Z : θ = π + 2kπ.

<sup>3</sup> e <sup>i</sup><sup>θ</sup> = i ⇐⇒ e <sup>i</sup><sup>θ</sup> = e i <sup>2</sup> ⇐⇒ ∃k ∈ Z : θ = π <sup>2</sup> + 2kπ.

Les formules suivantes sont importantes en analyse. L'une de leurs applications est la linéarisation des expressions trigonométriques.

### Proposition

Soit θ ∈ R et n ∈ Z.

<sup>1</sup> Formules d'Euler :

$$\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$$
  $\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$ 

<sup>2</sup> Formule de Moivre :

$$(e^{i\theta})^n = e^{in\theta}.$$

Linéariser une expression sin(x) <sup>k</sup> ou cos(x) k 0 , avec k et k <sup>0</sup> des entiers naturels, revient à les écrire comme combinaisons linéaires d'expressions de la forme sin(ax) ou cos(bx) où a et b sont des entiers.

### Exemple 1

Linéarisons l'expression sin(x) 3 . On utilise les formules d'Euler, la formule du binôme puis la formule de Moivre.

On a 
$$\sin(x) = \frac{e^{ix} - e^{-ix}}{2i}$$
. Donc

$$\sin(x)^{3} = \left(\frac{e^{ix} - e^{-ix}}{2i}\right)^{3}$$

$$= \frac{1}{8i^{3}}((e^{ix})^{3} - 3(e^{ix})^{2}e^{-ix} + 3e^{ix}(e^{-ix})^{2} - (e^{-ix})^{3})$$

$$= \frac{i}{8}(e^{3ix} - 3e^{ix} + 3e^{-ix} - e^{-3ix})$$

$$= \frac{i}{8}(2i\sin(3x) - 6i\sin(x))$$

$$= \frac{1}{4}(3\sin(x) - \sin(3x))$$

![](_page_22_Picture_6.jpeg)

![](_page_22_Picture_7.jpeg)

### <span id="page-23-0"></span>Exemple 2

Nous allons linéariser l'expression cos(x) 4 . On utilise les formules d'Euler, la formule du binôme puis la formule de Moivre.

$$\cos(x)^4 = \left(\frac{e^{ix} + e^{-ix}}{2}\right)^4$$

$$= \frac{1}{16}((e^{ix})^4 + 4(e^{ix})^3 e^{-ix} + 6(e^{ix})^2 (e^{-ix})^2 + 4e^{ix}(e^{-ix})^3 + (e^{-ix})^4)$$

$$= \frac{1}{16}(e^{4ix} + 4e^{2ix} + 6 + 4e^{-2ix} + e^{-4ix})$$

$$= \frac{1}{16}(2\cos(4x) + 8\cos(2x) + 6)$$

$$= \frac{1}{8}(\cos(4x) + 4\cos(2x) + 3)$$

![](_page_23_Picture_4.jpeg)

![](_page_23_Picture_5.jpeg)

## <span id="page-24-0"></span>Plan

- <sup>6</sup> [Argument d'un nombre complexe](#page-24-0)
- - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_24_Picture_11.jpeg)

![](_page_24_Picture_12.jpeg)

### <span id="page-25-0"></span>Argument d'un nombre complexe

La notion d'arguments de nombres complexes joue un rôle important en géométrie plane et en physique. Nous allons voir dans cette section quelques propriétés essentielles de nombres complexes.

### Proposition

Soit z un nombre complexe non nul. Alors il existe  $\theta \in \mathbb{R}$  :  $z = |z|e^{i\theta}$ .

**Preuve** Puisque 
$$\left|\frac{z}{|z|}\right|=1$$
 il existe  $\theta\in\mathbb{R}$  :  $\frac{z}{|z|}=e^{i\theta}$ . Il s'ensuit que  $z=|z|e^{i\theta}$ .

#### Définition

Soit z un nombre complexe non nul.

- L'écriture  $z = |z|e^{i\theta}$  s'appelle la forme polaire de z.
- 2 Le réel  $\theta$ , noté arg(z), s'appelle un argument de z.

![](_page_25_Picture_9.jpeg)

![](_page_25_Picture_10.jpeg)

### <span id="page-26-0"></span>Argument d'un nombre complexe

#### Remarques

- **3** Soit z un nombre complexe non nul. Si  $\theta$  est un argument de z, alors pour tout entier  $k \in \mathbb{Z}$ ,  $\theta + 2k\pi$  est aussi un argument de z. On écrit  $\arg(z) = \theta$  [ $2\pi$ ].
- ② Sur l'intervalle  $]-\pi,\pi]$ , il existe un unique réel  $\theta$  vérifiant  $\theta=\arg(z)$ . On l'appelle argument principal de z.

#### **Exemples**

- L'argument principal de 1 est 0.
- **2** L'argument principal de -1 est  $\pi$ .
- **②** L'argument principal de i est  $\frac{\pi}{2}$ .

On détermine effectivement l'argument principal  $\theta$  d'un complexe non nul z=a+ib en remarquant que  $\theta$  est l'unique réel appartenant à l'intervalle  $]-\pi,\pi]$  défini par les deux relations :

$$\cos(\theta) = \frac{a}{\sqrt{a^2 + b^2}}$$
  $\sin(\theta) = \frac{b}{\sqrt{a^2 + b^2}}$ 

![](_page_26_Picture_10.jpeg)

# <span id="page-27-0"></span>Argument d'un nombre complexe

### Proposition

Soit z et z <sup>0</sup> deux nombres complexes non nuls. Alors :

1

$$arg(zz') = arg(z) + arg(z')$$
 [2 $\pi$ ].

2

$$\arg(\frac{z}{z'}) = \arg(z) - \arg(z')$$
 [2 $\pi$ ].

3

$$arg(\frac{1}{z}) = arg(\overline{z}) = -arg(z)$$
 [2 $\pi$ ].

<sup>4</sup> Pour tout k ∈ Z on a :

$$arg(z^k) = k arg(z)$$
 [2 $\pi$ ].

![](_page_27_Picture_11.jpeg)

![](_page_27_Picture_12.jpeg)

## <span id="page-28-0"></span>Plan

- <sup>7</sup> Racines n[-èmes d'un nombre complexe](#page-28-0)
- - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_28_Picture_11.jpeg)

![](_page_28_Picture_12.jpeg)

Dans cette section, n désigne un entier naturel non nul.

### Définition

Soit z un nombre complexe non nul. On appelle racine n-ème de z tout nombre complexe w vérifiant w <sup>n</sup> = z.

### Remarque

Lorsque n = 2 (respectivement n = 3) on parle de racine carrée (respectivement racine cubique).

#### Exemples

- <sup>1</sup> 1 est une racine n-ème de 1 pour tout n.
- <sup>2</sup> i est une racine carrée de −1.
- 3 √5 3 est une racine cinquième de 3.

![](_page_29_Picture_11.jpeg)

Notre but est de déterminer toutes les racines n-èmes d'un nombre complexe donné. On commence par déterminer les racines n-èmes du complexes z = 1 et ensuite on montre comment déterminer celles d'un nombre complexe quelconque. Une racine n-ème de 1 s'appelle une racine n-ème de l'unité.

### Remarques

- <sup>1</sup> Si n est pair alors 1 et −1 sont des racines n-èmes de l'unité.
- <sup>2</sup> Si w est une racine n-ème de l'unité alors |w| = 1. En effet w <sup>n</sup> = 1 implique |w| <sup>n</sup> = 1. Donc

$$0 = |w|^n - 1 = (|w| - 1)(\sum_{k=0}^{n-1} |w|^{n-1-k}).$$

Comme ( P<sup>n</sup>−<sup>1</sup> k=0 |w| n−1−k ) 6= 0 il vient |w| − 1 = 0 et par suite |w| = 1.

#### Proposition

Il existe exactement n racines n-èmes de l'unité. Elles sont de la forme

$$w_k = e^{\frac{2ik\pi}{n}}, \quad k = 0, 1, \dots, n-1.$$

**Preuve** Il est clair que pour tout entier  $0 \le k \le n-1$ , le complexe  $e^{\frac{2ik\pi}{n}}$  est une racine n-ème de l'unité.

Réciproquement, soit w une racine n-ème de l'unité. Puisque |w|=1 il existe  $\theta \in [0,2\pi[$  tel que  $w=e^{i\theta}.$  En utilisant la formule de Moivre il vient  $(e^{i\theta})^n=e^{in\theta}=1.$ 

Alors il existe  $k \in \mathbb{Z}$  tel que  $n\theta = 2k\pi$ , soit  $\theta = \frac{2k\pi}{n}$ .

Comme  $\theta \in [0, 2\pi[$  on a nécessairement  $0 \le k \le n-1$ .

![](_page_31_Picture_8.jpeg)

![](_page_31_Picture_9.jpeg)

### Remarques

<sup>1</sup> Soit w une racine n-ème de l'unité. Si w 6= 1 alors

$$1+w+\cdots+w^{n-1}=0.$$

<sup>2</sup> Soit w<sup>k</sup> = e <sup>n</sup> une racine n-ème de l'unité. Alors

$$\overline{w_k} = \frac{1}{w_k} = e^{-\frac{2ik\pi}{n}} = e^{2i\pi - \frac{2ik\pi}{n}} = e^{\frac{2i(n-k)\pi}{n}} = w_{n-k}.$$

<sup>3</sup> Les racines n-èmes de l'unité sont situées sur le cercle trogonométrique.

![](_page_32_Picture_7.jpeg)

![](_page_32_Picture_8.jpeg)

### Exemples

Déterminons les racines n-èmes de l'unité dans les cas suivants :

n = 3 : On a trois racines troisièmes de l'unité

$$w_0 = 1,$$
  $w_1 = e^{\frac{2i\pi}{3}},$   $w_2 = e^{\frac{4i\pi}{3}} = \overline{w_1}.$ 

n = 4 : On a quatre racines quatrièmes de l'unité

$$w_0 = 1$$
,  $w_1 = e^{\frac{2i\pi}{4}} = i$ ,  $w_2 = e^{\frac{4i\pi}{4}} = -1$ ,  $w_3 = e^{\frac{6i\pi}{4}} = -i$ .

n = 5 : On a cinq racines cinquièmes de l'unité

$$w_0 = 1$$
,  $w_1 = e^{\frac{2i\pi}{5}}$ ,  $w_2 = e^{\frac{4i\pi}{5}}$ ,  $w_3 = e^{\frac{6i\pi}{5}} = \overline{w_2}$ ,  $w_4 = e^{\frac{8i\pi}{5}} = \overline{w_1}$ .

![](_page_33_Picture_9.jpeg)

![](_page_33_Picture_10.jpeg)

On peut maintenant donner la forme des racines n-èmes d'un nombre complexe quelconque.

### Proposition

Soit z un nombre complexe non nul de forme polaire  $z=\rho e^{i\theta}$ . Alors les racines n-èmes de z sont de la forme

$$Z_k = \sqrt[n]{\rho} e^{i\left(\frac{\theta}{n} + \frac{2k\pi}{n}\right)}, \quad k = 0, 1, \dots, n-1.$$

**Preuve** Il suffit de remarquer que si Z est une racine n-ème de z alors

$$\frac{Z}{\sqrt[n]{\rho}e^{\frac{i\theta}{n}}}$$

est une racine n-ème de l'unité. Ceci montre qu'il existe  $0 \le k \le n-1$  tel que

$$\frac{Z}{\sqrt[n]{\rho}\,\mathrm{e}^{\frac{\mathrm{i}\theta}{n}}}=\mathrm{e}^{\frac{2\mathrm{i}k\pi}{n}}.$$

D'où Z est de la forme  $\sqrt[n]{\rho} e^{i\left(\frac{\theta}{n} + \frac{2k\pi}{n}\right)}$ .

![](_page_34_Picture_10.jpeg)

![](_page_34_Picture_11.jpeg)

#### **Exemples**

Déterminons les racines *n*-èmes du nombre complexe *z* dans les cas suivants:

- -1 sont :
  - $z_0 = e^{i\frac{\pi}{4}}, \quad z_1 = e^{i\frac{\pi}{4}}e^{2i\frac{\pi}{4}} = e^{3i\frac{\pi}{4}}, \quad z_2 = e^{i\frac{\pi}{4}}e^{4i\frac{\pi}{4}} = e^{5i\frac{\pi}{4}}, \quad z_3 = e^{i\frac{\pi}{4}}e^{2i\frac{\pi}{4}}$  $e^{i\frac{\pi}{4}}e^{6i\frac{\pi}{4}}=e^{7i\frac{\pi}{4}}$
- 2 z = 1 + i et n = 4: On a  $z = \sqrt{2}e^{i\frac{\pi}{4}}$ . Donc les racines quatrièmes de 1+i sont :  $z_0 = 2^{\frac{1}{8}} e^{i\frac{\pi}{16}}, \quad z_1 = 2^{\frac{1}{8}} e^{9i\frac{\pi}{16}}, \quad z_2 = 2^{\frac{1}{8}} e^{17i\frac{\pi}{16}}, \quad z_3 = 2^{\frac{1}{8}} e^{25i\frac{\pi}{16}}.$

![](_page_35_Picture_6.jpeg)

![](_page_35_Picture_7.jpeg)

## <span id="page-36-0"></span>Plan

- <sup>8</sup> [Equations du second degré](#page-36-0)
  - [Racines carrées d'un nombre complexe](#page-37-0)

![](_page_36_Picture_11.jpeg)

![](_page_36_Picture_12.jpeg)

# <span id="page-37-0"></span>Racines carrées d'un nombre complexe

D'après la section précédente tout nombre complexe non nul z admet deux racines carrées opposées l'une à l'autre. Si z est donné sous sa forme polaire z = ρe iθ alors ces deux racines carrées sont données par

$$z_1 = \sqrt{\rho} e^{\frac{i\theta}{2}}, \qquad z_2 = -z_1.$$

#### Remarques

- <sup>1</sup> Si <sup>x</sup> <sup>∈</sup> <sup>R</sup><sup>+</sup> alors les racines carrées de <sup>x</sup> sont <sup>√</sup> x et − √ x.
- <sup>2</sup> Si x ∈ R<sup>−</sup> alors les racines carrées de x sont i p |x| et −i p |x|.

![](_page_37_Picture_6.jpeg)

![](_page_37_Picture_7.jpeg)

## Racines carrées d'un nombre complexe

Dans le cas où le nombre complexe z = a + ib est donné sous sa forme algébrique on suit la méthode suivante. Soit Z = x + iy une racine carrée de z. Puisque Z <sup>2</sup> = z et |Z| <sup>2</sup> = |z| on a

$$\begin{cases} x^2 + y^2 &= \sqrt{a^2 + b^2} \\ x^2 - y^2 &= a \\ 2xy &= b \end{cases}$$

On obtient alors

$$\begin{cases} x^2 = \frac{\sqrt{a^2 + b^2} + a}{2} \\ y^2 = \frac{\sqrt{a^2 + b^2} - a}{2} \\ 2xy = b \end{cases}$$

On utilise les deux premières équations pour déterminer les valeurs possibles de x et y et on utilise la troisième relation pour choisir les valeurs convenables.

![](_page_38_Picture_6.jpeg)

![](_page_38_Picture_7.jpeg)

# Racines carrées d'un nombre complexe

### Exemple

Déterminons les racines carrées de z = 8 − 6i. Posons Z = x + iy une racine carrée de z. Alors on a

$$\begin{cases} x^2 + y^2 &= 10 \\ x^2 - y^2 &= 8 \\ 2xy &= -6 \end{cases}$$

Donc

$$\begin{cases} x^2 = 9 \\ y^2 = 1 \\ xy = -3 \end{cases}$$

Il vient Z<sup>1</sup> = 3 − i et Z<sup>2</sup> = −3 + i.

![](_page_39_Picture_7.jpeg)

![](_page_39_Picture_8.jpeg)

### <span id="page-40-0"></span>Equation du second degré

Une équation de la forme  $az^2 + bz + c = 0$  d'inconnue z et de coefficients a,b,c dans  $\mathbb C$  s'appelle une équation du second degré à coefficients dans  $\mathbb C$ .

#### théorème

Soit a, b, c des nombres complexes avec  $a \neq 0$  et soit l'équation du second degré

$$(E) \qquad az^2 + bz + c = 0.$$

Notons  $\Delta = b^2 - 4ac$ . Alors

• Si  $\Delta = 0$  l'équation (E) admet une solution double

$$z_0=\frac{-b}{2a}.$$

② Si  $\Delta \neq 0$  l'équation (E) admet deux solutions distinctes :

$$Z_1 = \frac{-b - \delta}{2a} \qquad \qquad Z_2 = \frac{-b + \delta}{2a}$$

où  $\delta$  est une racine carrée de  $\Delta$ .

![](_page_40_Picture_11.jpeg)

![](_page_40_Picture_12.jpeg)

# <span id="page-41-0"></span>Equation du second degré

### Exemples

<sup>1</sup> Résoudre dans C l'équation du second degré :

(E) : 
$$iz^2 - \sqrt{3}z + 1 = 0$$

On a ∆ = 3 − 4i et δ = 2 − i est une racine carrée de ∆. Alors les solutions de (E) sont :

$$Z_1 = \frac{\sqrt{3} - 2 + i}{2i}$$
  $Z_2 = \frac{\sqrt{3} + 2 - i}{2i}$ 

<sup>2</sup> Résoudre dans C l'équation du second degré :

(E) : 
$$z^2 - (1+i)z + i = 0$$
.

On a ∆ = −2i = 2e −iπ <sup>2</sup> et δ = √ 2e −iπ <sup>4</sup> est une racine carrée de ∆. Alors les solutions de (E) sont :

$$Z_1 = \frac{1+i-\sqrt{2}e^{\frac{-i\pi}{4}}}{2}$$
  $Z_2 = \frac{1+i+\sqrt{2}e^{\frac{-i\pi}{4}}}{2}$ 

![](_page_41_Picture_10.jpeg)

### <span id="page-42-0"></span>Fin du chapitre 1

![](_page_42_Picture_1.jpeg)

![](_page_42_Picture_2.jpeg)