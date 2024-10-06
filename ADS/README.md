## Important Topics
1. [What is asymtotics (strict)?](#what-is-asymtotics-strict)
2. [Stable vs Unstable Sort](#stable-vs-unstable-sort)
3. [Finite, Countable, continuum sets](#finite-countable-continuum-sets)
4. [What is task](#what-is-task)

### What is asymtotics (strict)?
Asymptotic notation is a way to represent the time complexity of an algorithm. It is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. The most common asymptotic notations are Big O, Big Omega, and Big Theta. <br>
`f(x) =~ O(g(x)) <=> all(x) > C1: f(x)/g(x) < C2`

### Stable vs Unstable Sort
Stable sort algorithms maintain the relative order of equal elements. Unstable sort algorithms do not maintain the relative order of equal elements.
``` 
Example:
Unsorted: 3, 2, 3', 1, 2'
Stable Sort: 1, 2, 2', 3, 3' 
Unstable Sort: 1, 2', 2, 3, 3'
```


### Finite, Countable, continuum sets
* **Finite Set:** A set of finite size is a set consisting of a finite number of elements.  
    - {1, 2, 3, 4, 5}
* **Countable Set:** Countable set is a set of infinite length, but which can be enumerated with natural numbers. 
    - `natural numbers`, `integers`, `rational numbers` are countable sets.
* **Continuum Set:** A set of infinite length, which cannot be enumerated.
    - `real numbers` are continuum sets. 


### What is task
A binary word of arbitrary length to possibly another binary word of arbitrary length. 
    - f: {0, 1}* -> {0, 1}*
        - f(00) = f(01) = 10
        - f(10) = f(11) = 01
    - If there exists an algorithm that calculates `f(x)` from x, then it's called a **computable task**.
    
