## Important Topics
1. [What is asymtotics (strict)?](#what-is-asymtotics-strict)


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