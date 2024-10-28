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

Solution:
We need at most `log n` questions to find the number `m`.
Running a binary search on the range [1, n] will help us to find the number `m` in `log n` questions.
Though I could not find better time complexity combining both types of questions.

### Task 3
Let quicksort select median of the first, second, middle, penultimate and last element as pivot. Show a test on which such an algorithm will work for $O(n^2)$ time.

Solution: Let us consider an array of size 2n, in this pattern [$n_0, n_1, ... n_{n-1}, n_n, n_{n-1}, ... n_1,n_0$]
So either increasing than decreasing or decreasing than increasing. Then the pivot will be near maximum or minimum and the split will be very unbalanced, keeping all elements in one side and almost none in the other side. This will lead to $O(n^2)$ time complexity.

### Task 4
You are given a set of forbidden decimal digits. It is necessary to find the number of numbers between $10^b$ and $10^{b+1}$ that are divisible by `x` and do not contain forbidden digits. The complexity is $O(x^3 log b)$.

Solution: Could not found any, please help me to solve this.

### Task 5
In lecture we talked about Euler's theorem, If $a$ and $m$ are coprime, then $a^{\phi(m)} \equiv 1 \pmod m$. Here $\phi(m)$ is euler totient function. Prove this theorem.

Proof: We can generalize the fermat's little theorem to Euler's theorem.
Let $a$ and $m$ are coprime, then $a^{\phi(m)} \equiv 1 \pmod m$.
According to fermat's little theorem, $a^{m-1} \equiv 1 \pmod m$. Where $m$ is prime number.
We also know that $\phi(m) = m-1$ for prime numbers.
So, $a^{\phi(m)} \equiv 1 \pmod m$.


### Task 6
Prove that there is no data structure such that,
1. Get and remove the minimum element in $O(1)$ time
2. We can insert an element in $O(1)$ time

Proof: Let us consider a data structure which can get and remove the minimum element in $O(1)$ time. It means that the minimum element is always at the top of the data structure. Now, if we insert an element in $O(1)$ time, then we need to check if the inserted element is the minimum element or not. If it is the minimum element, then we need to update the top element. This will take at least $O(log n)$ time. On the other hand, if we do not update the top element, then we can not get and remove the minimum element in $O(1)$ time. Hence, there is no data structure which can satisfy both conditions.

### Task 7
You are given an array of length n and k queries for searching k-th statistics.You need to create an algorithm that answers all queries in O(n log k) time.

Solution: K'th statistics refers to the k'th smallest/largest element in the array. We can use min or max heap to find the k'th statistics in O(n log k) time. We can insert elements to the array in O(n) time and if array size is greater than k, then we can remove the top element from the heap keeping min or max k elements in the heap. This will take O(log k) time. Hence, we can answer all queries in O(n log k) time.

Below is the algorithm to find k'th maximum element in the array.
```algorithm
1. Create a min heap
2. Insert elements to the heap
3. If heap size is greater than k
    - check if the top element is greater than the current element
    - if yes, then remove the top element and insert the current element
4. Return the top element
```