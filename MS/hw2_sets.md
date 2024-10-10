## Homework 2. Relations and functions

1. Determine which of the following functions is a bijection from R to R.
- $f(x) = sin(x)$
- $f(x) = -2x + 3$
- $f(x) = x(x-2) + 1$
- $f(x) = x^3 - x$
- $f(x) = 2^x$
    - $f(x) = sin(x)$ is not a bijection because it is not `injective`.
        - $sin(0) = sin(2\pi) = 0$
    - $f(x) = -2x + 3$ `is a bijection` because it is injective and surjective.
    - $f(x) = x(x-2) + 1$ is not a bijection because it is `not surjective`.
        - $f(x) = 1$ has no solution. Because if $f(x) = 1$ then, $b^2 - 4ac$ becomes negative
         and which is not true $x \in R$

    - $f(x) = x^3 - x$ is not a bijection because it is `not injective`.
        - $f(1) = f(-1) = 0$
    - $f(x) = 2^x$ is not a bijection because it is `not surjective`.
        - $f(x) = 0$ has no solution. Because $2^x$ is always positive.

2. Choose one true proposition.
- There is no function $f: z \longrightarrow z$ that is injective and surjective.
    - False because the identity function $f(x) = x$ is both injective and surjective.
- There is no function $f: z \longrightarrow z$ that is injective but not surjective.
    - True
- There is no function $f: z \longrightarrow z$ that is surjective but not injective.
    - False, $f(x) = \lfloor x \rfloor/2$ is surjective but not injective. 
- There is no function $f: z \longrightarrow z$ that is neither injective nor surjective.
    - False, $f(x) = 0$  or $f(x) = n^2$ is neither injective nor surjective.
- All the four previous propositions are false.


3. The set $\mathbb{N} \cup \mathbb{Q}$ has the same cardinality as:
- $\mathbb{R}$
- $\mathbb{N} \times \mathbb{Q}$
    - True,
- $\mathbb{N}^\mathbb{Q}$
- $\mathbb{Z} \cup \mathbb{R}$
- $\mathbb{N} \setminus \mathbb{Q}$

4. A relation $\mathbb{R}$ is defined on $\mathbb{N}$ by a R if 5a - b is even. How many equivalence classes are there.

- 5a - b is even means
    - $5a - b \equiv 0 \pmod{2}$
    - $5a \equiv b \pmod{2}$
    - $a \equiv b \pmod{2}$

    - So one set is: {2, 4, 6, 8, 10, ...}
    - Another set is: {1, 3, 5, 7, 9, ...}
    - So there are `two equivalence classes`.

5. Find the real number `a` such that the function $ f: \mathbb{R} - {3} \longrightarrow \mathbb{R} - {a}$ defined by $f(x) = \frac{x}{x-3}$ is a bijection.

- Let f(x) = y = $\frac{x}{x-3}$
    - $y(x-3) = x$
    - $yx - 3y = x$
    - $yx - x = 3y$
    - $x(y-1) = 3y$
    - $x = \frac{3y}{y-1}$

    So y can be anything except 1. So `a = 1`

    
