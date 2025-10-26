# Matrices

<section id="introduction-matrices" style="padding:20px; background-color:#f0f8ff; border-radius:8px; margin-bottom:15px;">
## Part 1: Introduction to Matrices

A matrix is a rectangular array of numbers arranged in rows and columns:

<mathblock>
A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ 
                    a_{21} & a_{22} & \dots & a_{2n} \\ 
                    \vdots & \vdots & \ddots & \vdots \\ 
                    a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}
</mathblock>

- <math>m</math>: number of rows  
- <math>n</math>: number of columns  
- <math>a_{ij}</math>: element in row <math>i</math> and column <math>j</math>
</section>

<section id="operations-matrices" style="padding:20px; background-color:#fff0f5; border-radius:8px; margin-bottom:15px;">
## Part 2: Basic Operations

### Addition & Subtraction
<mathblock>
A + B = [a_{ij} + b_{ij}], \quad A - B = [a_{ij} - b_{ij}]
</mathblock>

### Scalar Multiplication
<mathblock>
kA = [k \cdot a_{ij}]
</mathblock>

### Matrix Multiplication
<mathblock>
C = A \cdot B, \quad c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
</mathblock>

### Transpose
<mathblock>
A^T = [a_{ji}]
</mathblock>
</section>

<section id="special-matrices" style="padding:20px; background-color:#f5fff0; border-radius:8px; margin-bottom:15px;">
## Part 3: Special Matrices

- **Zero matrix**: all elements 0, denoted <math>0_{m \times n}</math>  
- **Identity matrix**: square matrix with 1's on the diagonal, denoted <math>I_n</math>  
- **Diagonal matrix**: only diagonal elements non-zero  
- **Symmetric matrix**: <math>A = A^T</math>  
- **Skew-symmetric**: <math>A^T = -A</math>
</section>

<section id="determinant-inverse" style="padding:20px; background-color:#fffaf0; border-radius:8px; margin-bottom:15px;">
## Part 4: Determinant & Inverse

### Determinant
For a 2x2 matrix:

<mathblock>
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \quad \det(A) = ad - bc
</mathblock>

### Inverse
A matrix <math>A</math> is invertible if <math>\det(A) \neq 0</math>. Its inverse satisfies:

<mathblock>
A^{-1} \cdot A = I
</mathblock>
</section>

<section id="applications-matrices" style="padding:20px; background-color:#f0fff5; border-radius:8px;">
## Part 5: Applications

- Solving systems of linear equations  
- Computer graphics transformations  
- Machine learning (linear regression, neural networks)  
- Markov chains and probability  
- Engineering simulations
</section>
