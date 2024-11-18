## Homework 4

- **Question 1**: Choose one true proposition:
    - [ ] A. All terms of a sequence must be distinct.
    - [ ] B. Every sequence can be explicitly defined.
    - [ ] C. A sequence cannot have both an explicit and a recursive definition.
    - [ ] D. A sequence can have at most one recursive relation.
    - [x] E. A recursively defined sequence must have initial values.

        - Answer: E, A recursively defined sequence must have initial value which we call base case.

- **Question 2**: Choose a closed-form expression for the $n_{th}$ term of the sequence {$a_n$}, where $n\in \mathbb{N}$, whose first four terms are $7, 19, 55, 163, \ldots$:
    - [ ] A. $a_n = 7n$
    - [x] B. $a_n = 2\cdot3^n + 1$
    - [ ] C. $a_n = 4n^2 + 3$
    - [ ] D. $a_n = 6\cdot3^n + 1$
    - [ ] E. $a_n = 2n^3 + 5$

        - Answer: B, Cause $a_1 = 2\cdot3^1 + 1 = 7$, $a_2 = 2\cdot3^2 + 1 = 19$, $a_3 = 2\cdot3^3 + 1 = 55$, $a_4 = 2\cdot3^4 + 1 = 163$. So, $a_n = 2\cdot3^n + 1$.

- **Question 3**: Let $s_n$ be the number of n-digit numbers such that every digit is 0, 1, or 2 and the sequence "00" never appears (note that a number cannot start with 0). Choose one true proposition.
    - [ ] A. $s_n = 2s_{n-1} + 2$ for all n>2.
    - [ ] B. $s_n = 2s_{n-1} + 2s_{n-2}$ for all n>2.
    - [ ] C. $s_n = 3s_{n-1} + s_{n-2}$ for all n>2
    - [ ] D. $s_n = s_{n-1} + 3s_{n-2}$ for all n>2.
    - [ ] E. All the previous relations are false.

        - Answer: B, here, $s_1 = 2, s_2 = 6, s_3 = 16, s_4 = 44, s_5 = 120$
        - So we see that if n>2, it follows, $s_n = 2s_{n-1} + 2s_{n-2}$

- **Question 4**: Consider the following recurraence relation:
    - $a_n = 10a_{n-2} - 3a_{n-1}$ with $a_1 = 1$ and $a_2 = 3$.
    - We know that $a_n = \alpha \cdot r_1^n + \beta \cdot r_2^n$ where $r_1>r_2$. Find the value of the expression $\alpha/\beta + r_1 - r_2$.