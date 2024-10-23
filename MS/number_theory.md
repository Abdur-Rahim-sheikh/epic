## Number Theory

1. [Division with reminder and Congruence](#division-with-reminder-and-congruence)
2. [Fermat's Little Theorem](#fermats-little-theorem)
3. [Chinese Remainder Theorem (CRT)](#chinese-remainder-theorem-crt)

### Division with reminder and Congruence
Congruence properties:
- If $a \equiv b \pmod{m}$ and $c \equiv d \pmod{m}$, then $a+c \equiv b+d \pmod{m}$
- If $a \equiv b \pmod{m}$ and $c \equiv d \pmod{m}$, then $a-c \equiv b-d \pmod{m}$
- If $a \equiv b \pmod{m}$ then $a^n \equiv b^n \pmod{m}$
- If $ka \equiv kb \pmod{m}$ and gcd($k$, $m$) = 1, then $a \equiv b \pmod{m}$

### Fermat's Little Theorem
Let a be an integer and p be a prime number. such that gcd(a, p) = 1.
- Then $a^{p-1} \equiv 1 \pmod{p}$
- $a^p \equiv a \pmod{p}$
Proof:
- $a, 2a, 3a, ..., (p-1)a$ are all distinct modulo p.
- So, $a*2a*3a*...*(p-1)a \equiv 1*2*3*...*(p-1) \pmod{p}$
- $a^{p-1}*(p-1)! \equiv (p-1)! \pmod{p}$
- $a^{p-1} \equiv 1 \pmod{p}$

### Chinese Remainder Theorem (CRT)
Let $m_1, m_2, ..., m_k$ be pairwise coprime integers and $M = m_1*m_2*...*m_k$.
- Then for any integers $a_1, a_2, ..., a_k$, there exists an integer x such that:
  - $x \equiv a_1 \pmod{m_1}$
  - $x \equiv a_2 \pmod{m_2}$
  - ...
  - $x \equiv a_k \pmod{m_k}$
Then $x \equiv a_1*M_1*M_1^{-1} + a_2*M_2*M_2^{-1} + ... + a_k*M_k*M_k^{-1} \pmod{M}$
Also, $M_i * M_i^{-1} \equiv 1 \pmod{m_i}$

Let's solve $2^102 \pmod{303}$ using CRT:
- $303 = 3*101$
- since $2 \equiv -1 \pmod{3}$
    - $2^{102} \equiv (-1)^{102} \equiv 1 \pmod{3}$
- Fermat's Little Theorem: $2^{101-1} \equiv 1 \pmod{101}$
    - $2^{100} * 2^2 \pmod{101}$
    - $2^2 \equiv 4 \pmod{101}$

We now have a congruence system:
- $x \equiv 1 \pmod{3}$
- $x \equiv 4 \pmod{101}$

| $a_i$ | $m_i$ | $M_i$ | $M_i^{-1}$ |
|-------|-------|-------|-------|
| 1     | 3     | 303/3 = 101 | 101^-1%3 = 2 |
| 4     | 101   | 303/101 = 3 | 3^-1%101 = 34 |

- $x = 1*101*2 + 4*3*34 \pmod{303}$
- $x = 202 + 408 \pmod{303}$
- $x = 610 \pmod{303}$
- $x = 4 \pmod{303}$

