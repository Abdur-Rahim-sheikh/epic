## First Home work

### Task 1: Prove that any number `n` has at most `log n` different prime factors.
Proof: 
We know that, $n = p_1^{e_1} \cdot p_2^{e_2} \cdot p_3^{e_3} \cdot \ldots \cdot p_k^{e_k}$

so $n \geq p_1 \cdot p_2 \cdot p_3 \cdot \ldots \cdot p_k$ 
i.e. 

- $360 = 2^3 \cdot 3^2 \cdot 5^1$
- $360 \geq 2 \cdot 3 \cdot 5$
- $360 \geq 2 \cdot 2 \cdot 2$ as 3 and 5 are greater than 2
- $360 \geq 2^3 \equiv 2^k$

So,
- $n \geq 2^k$ 
- $log_2 (n) \geq log_2 (2^k)$
- $log_2 (n) \geq k$

Hence, any number `n` has at most `log n` different prime factors.


### Task 2
We have secretly picked a number `m` from range [1, n], your task is to find it using the following two types of questions:
1. Find out if the number is divisible by x
2. Check if the number is greater than x
How many questions do you need to definitely know the number? You do not need to provide an exact answer, asymptotic is enough.