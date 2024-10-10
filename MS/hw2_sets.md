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



