## Logic and Induction

### Which of the following statements are false?
- If "Harry Potter" was written by J. Rowling then 576 is a perfect square.
- **If 576 is a perfect square then a cat can fly.**
    - This one is False, Because $True \longrightarrow False$ is False.
- If a cat can fly then Isaac Newton was an ancient Greek.
- If Isaac Newton was an ancient Greek then "Harry Potter" was written by J. Rowling.

### Let x and y be integers. Which of the following statements are true?
- $\forall x \exists y (x^2 + y^2$ is a perfect square)
    - **True**, let if $y = 0$ then $x^2 + y^2 = x^2$ which is a perfect square.
- $\forall x \exists y (3xy$ is a perfect square)
    - **True**, let if $y = 3x$ then $3xy = 3x.3x = (3x)^2$ which is a perfect square.
- $\exists x \forall y (xy$ is a multiple of 3)
    - **True**, let if $x = 3$ then $xy = 3y$ which is a multiple of 3.
- $\forall x \exists y (\cfrac{x}{y}$ is a prime)
    - False, let if $x = 1$ then $\cfrac{x}{y} = \cfrac{1}{y}$ which is not a prime.
- $\forall x (x^2 + x + 41$ is a prime)
    - False, **it's very interesting** cause till $x = 39$ it's a prime but at $x = 40, x^2 + x + 41 = 40^2 + 40 + 41 = 1681 = 41^2$ which is not a prime.

Summary, 1, 2, 3 are True and 4, 5 are False.

### Construct the truth tables for the logical expressions below.
- $(\overline{A} \Longrightarrow B) \lor (A \land \overline{B})$
    - | A | B | $\overline{ A}$ | $\overline{ A} \Rightarrow B = x$ | $A \land \overline{ B} = y$ | $x \lor y$ |
      |---|---|---------|---------------------------|------------------|-------------------------------------------------|
      | T | T | F       | T                         | F                | T                                               |
      | T | F | F       | T                         | T                | T                                               |
      | F | T | T       | T                         | F                | T                                               |
      | F | F | T       | F                         | F                | F                                               |
- $(A \lor B) \Longrightarrow (\overline{ A} \land B)$
    - | A | B | $\overline{ A}$ | $A \lor B = x$ | $\overline{ A} \land B = y$ | $x \Rightarrow y$ |
      |---|---|---------|-----------------|---------------------------|------------------|
      | T | T | F       | T               | F                         | F                |
      | T | F | F       | T               | F                         | F                |
      | F | T | T       | T               | T                         | T                |
      | F | F | T       | F               | F                         | T                |

### What is the greatest number of parts that 100 circles can cut a plane into?
- The greatest number of parts that 100 circles can cut a plane into is 100*99/2 + 1 = 4951.
- Be

### Prove that for any natural number `n` there exists a number which is written with only the digits 3 and 6 and is divisible by $2^n$.
- Let's prove this by pigeonhole principle.
- Let's think of binary tree each node having value 3 or 6. So the tree is infinite.
- But as we know the modulo $2^n$ has finite 0 to $2^n - 1$ values. 
- So, by pigeonhole principle, reminder of the tree will be repeated after some level and at some point it will cycle back to the same value.
- So, there exists a number which is written with only the digits 3 and 6 and is divisible by $2^n$.


### What is the greatest value of `k` such that the number $1+1 \cdot 1!+2 \cdot 2!+ \ldots + 99 \cdot 99!$ is divisible by $7^k$?
- Let's find the pattern of the number.
