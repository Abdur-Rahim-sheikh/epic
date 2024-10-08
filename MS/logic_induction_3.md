## Chapter 3 - logic induction

1. Determine whether the following implications are true or false:
(a) If 2 is an even integer, then 5 > 0.
(b) If 2 is an even integer, then 5 < 0.
(c) If 2 is an odd integer, then 5 > 0.
(d) If 2 is an odd integer, then 5 < 0.

Answer:
(a) True (b) False (c) True (d) False

2. Let x = 1, y = 1, z = 0. Determine the logical values of the following expressions:
    - $x \land y \land z;$
        - False
    - $x \lor y \lor z;$
        - True
    - $x \longrightarrow (y \longrightarrow z);$
        - 1 → (1 → 0) = 1 → 0 = 0
    - $x \longrightarrow y \longrightarrow z;$
        - 1 → 1 → 0 = 1 → 0 = 0
    - $(x \lor y) \longrightarrow z;$
        - (1 ∨ 1) → 0 = 1 → 0 = 0

3. Determine which of the following formulas are identically true and which are identically false:
    - $x \longrightarrow (x \longrightarrow y)$
        - 1 → (1 → 1) and 0 → (0 → 1) 
        - True
    - $x \longrightarrow (y \longrightarrow x)$
        - 1 → (1 → 1) and 0 → (1 → 0)
        - 1 and 1
        - True
    - $y \longrightarrow x \longrightarrow (x \longrightarrow y)$ 
        - 1 → 1 → (1 → 1), 0 → 0 → (0 → 0), 0 → 1 → (1 → 0), 1 → 0 → (0 → 1)
        - True , True, False, True
        - This is not identically true or false. So `not a tautology`.
    - $(x \longrightarrow y) \land (y \longrightarrow z) \longrightarrow (x \longrightarrow z)$
        - 

        | x | y | z | $(x \longrightarrow y) = P$ | $y \longrightarrow z = Q$ | $P \land Q = R$ | $x \longrightarrow z = T$ | $R \longrightarrow T$ |
        |-------|-------|-------|--------------|--------------|---------------|----------------|--------------|
        | T     | T     | T     | T            | T            | T             | T              |T             |
        | T     | T     | F     | T            | F            | F             | F              |T             |
        | T     | F     | T     | F            | T            | F             | T              |T             |
        | T     | F     | F     | F            | T            | F             | F              |T             |
        | F     | T     | T     | T            | T            | T             | T              |T             |
        | F     | T     | F     | T            | F            | F             | T              |T             |
        | F     | F     | T     | T            | T            | T             | T              |T             |
        | F     | F     | F     | T            | T            | T             | T              |T             |


        - True
    - $(x \longrightarrow z) \longrightarrow (y \longrightarrow z \longrightarrow (x \lor y \longrightarrow z))$
        - 
        | x | y | z | $(x \longrightarrow z) = P$ | $y \longrightarrow z = Q$ | $(x \lor y \longrightarrow z) = R$ | $Q \longrightarrow R = S$ | $P \longrightarrow S$ |
        |-------|-------|-------|--------------|--------------|---------------|----------------|--------------|
        | T     | T     | T     | T            | T            | T             | T              |T             |
        | T     | T     | F     | F            | F            | T             | T              |T             |
        | T     | F     | T     | T            | T            | T             | T              |T             |
        | T     | F     | F     | F            | T            | T             | T              |T             |
        | F     | T     | T     | T            | T            | T             | T              |T             |
        | F     | T     | F     | T            | F            | T             | T              |T             |
        | F     | F     | T     | T            | T            | T             | T              |T             |
        | F     | F     | F     | T            | T            | T             | T              |T             |

        - True

    - $(x \longrightarrow (y \longrightarrow z) \longrightarrow (x \longrightarrow y \longrightarrow (x \longrightarrow z)))$
        - 
        Here is the final truth table in markdown format:


        | x    | y    | z    | P = (y → z) | Q = (x → y) | R = (x → z) | S = (Q → R) | T = (P → S) | x → T |
        |------|------|------|-------------|-------------|-------------|-------------|-------------|-------|
        | T    | T    | T    | T           | T           | T           | T           | T           | T     |
        | T    | T    | F    | F           | T           | F           | F           | T           | T     |
        | T    | F    | T    | T           | F           | T           | T           | T           | T     |
        | T    | F    | F    | T           | F           | F           | T           | T           | T     |
        | F    | T    | T    | T           | T           | T           | T           | T           | T     |
        | F    | T    | F    | F           | T           | T           | T           | T           | T     |
        | F    | F    | T    | T           | T           | T           | T           | T           | T     |
        | F    | F    | F    | T           | T           | T           | T           | T           | T     |
        
        - True

4. Truth table construction easy.

5. Which of the following statements are true (x and y are real numbers)?
    - $\forall x \exists y (xy = 1);$
        - False Because for x = 0, there is no y such that xy = 1.
    - $\forall x \exists y (xy=0);$
        - True Because for x if we take y = 0, then xy = 0.
    - $\exists x \forall y (xy = 1);$
        - False Because for y = 0, there is no x such that xy = 1.
    - $\forall x \exists y (x^2 + y^2 = 1);$
        - False Because for x = 2, there is no y such that x^2 + y^2 = 1.
    - $\forall x \exists y (x^2 - y^2 = 1);$
        - False Because for x = 0, there is no y such that x^2 - y^2 = 1.

6. Prove that
    - $1+2+3+...+(2n-1) = n^2$
        - Base case: n = 1
            - LHS = 1 = 1^2 = RHS
            - LHS n=2, 1+3 = 4 = 2^2 = RHS
            - LHS n=3, 1+3+5 = 9 = 3^2 = RHS
        - Inductive step: Assume true for n = k
            - $1+2+3+...+(2k-1) = k^2$
        - Prove for n = k+1
            - $1+2+3+...+(2k-1) + (2(k+1)-1) = k^2 + 2k + 1 = (k+1)^2$
    - $1^3 + 2^3 + 3^3 + ... + n^3 = n^2(n+1)^2/4$
        - Base case:
            - LHS n=1, 1 = 1^2(1+1)^2/4 = 1
            - LHS n=2, 1+8 = 2^2(2+1)^2/4 = 9
            - LHS n=3, 1+8+27 = 3^2(3+1)^2/4 = 36
        - Inductive step: Assume true for n = k
            - $1^3 + 2^3 + 3^3 + ... + k^3 = k^2(k+1)^2/4$
        - Prove for n = k+1
            - $1^3 + 2^3 + 3^3 + ... + k^3 + (k+1)^3$ 
            - $k^2(k+1)^2/4 + (k+1)^3$
            -  $(k+1)^2(k^2/4 + k + 1)$ // factor out (k+1)^2
            -  $(k+1)^2(k^2 + 4k + 4)/4$
            -  $(k+1)^2(k+2)^2/4$

7. Simplify the following statement:
    - $1/(1.2) + 1/(2.3) + 1/(3.4) + ... + 1/(n(n+1))$
    - $\sum_{k=1}^{n} \frac{1}{k(k+1)}$
    - let, $1/(k(k+1)) = A/k + B/(k+1)$
    - $1 = A(k+1) + Bk$
    - $1 = Ak + A + Bk$
    - $1 = (A+B)k + A$
    - $A+B = 0$ and $A = 1$
    - $B = -1$

    - $\sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n} \frac{1}{k} - \frac{1}{k+1}$
    - $1 - 1/2 + 1/2 - 1/3 + 1/3 - 1/4 + ... + 1/n - 1/(n+1)$
    - $1 - 1/(n+1)$

8. Find the value of the sum, $1^2 + 3^2 + 5^2 + ..... + 99^2$
    - $\sum_{k=1}^{50} (2k-1)^2$
    - $\sum_{k=1}^{50} 4k^2 - 4k + 1$
    - $4\sum_{k=1}^{50} k^2 - 4\sum_{k=1}^{50} k + \sum_{k=1}^{50} 1$
    - we know, $\sum_{k=1}^{n} k^2 = n(n+1)(2n+1)/6$ , $\sum_{k=1}^{n} k = n(n+1)/2$
    - $4*50*51*101/6 - 4*50*51/2 + 50$
    - $80850$

9. For which `n` that is true?
    - $n^2 > 2n + 1$
        - $n^2 - 2n - 1 > 0$
        - $ n > 1 + \sqrt{2}$
       
    - $2^n > n^2$
        - n = 1, 
            - LHS = 2, RHS = 1 - True
        - n = 2,
            - LHS = 4, RHS = 4 - False
        - n = 3,
            - LHS = 8, RHS = 9 - False
        - n = 4,
            - LHS = 16, RHS = 16 - False
        - n = 5,
            - LHS = 32, RHS = 25 - True
        n>4

    - $n! > 2^n$
        - $n \geq 4$

10. Prove that $\frac{1}{n + 1} + \frac{1}{n + 2}.....\frac{1}{3n + 1} > 1$
    - let n = 1
        - $1/2 + 1/3 + 1/4 = 13/12 > 1$
    So if we increase n, the value adds up and becomes greater, so no chance of becoming less than or equal to 1.
    - Proved

11. prove that 111...111 (243 digits) is divisible by 243.
    - Don't know how to prove this.

12. Prove that a regular triangle can be dissected into `n` smaller regular triangles if `n` is not less than 7.
    - draw and prove

13. How many parts do `n` straight lines in general position divide the plane into? (no two lines are parallel and no three lines pass through the same point)
    - $n(n+1)/2 + 1$