## Math and Statistics

1. [What is set?](#what-is-set)
2. [Set notations](#set-notations)
3. [Cardinality of a set](#cardinality-of-a-set)
4. [Venn Diagram](#venn-diagram)
5. [Power set](#power-set)
6. [Operations on sets](#operations-on-sets)
7. [Laws of set theory](#laws-of-set-theory)

### What is set?
A collection of distinct objects

### set notations
1. **Roster or Tabular form**: List of elements within curly braces.
    * Example: A = {1, 2, 3, 4, 5}
2. **Semantic notation**: A rule or condition that describes the elements of a set.
    * Example: Let A be the set of all even numbers less than 10. 
                or Let B be the set of things on my table.
3. **Set builder notation**: A rule or condition that describes the elements of a set.
    * Example: A = {x | x is an even number less than 10}
4. **Membership**: If an element belongs to a set, it is denoted by ∈.
    * Example: If _x_ is an element of set A, then x ∈ A.
5. **Subset**: If all the elements of set A are also elements of set B, then A is a subset of B. It is denoted by ⊆.
    * Example: If A = {1, 2, 3} and B = {1, 2, 3, 4, 5}, then A ⊆ B.
    * Proper subset: If A is a subset of B and A is not equal to B, then A is a proper subset of B. It is denoted by ⊂.
    * Universal set: The set of all possible elements under consideration is called the universal set. It is denoted by U.

### Cardinality of a set
The number of elements in a finite set is called the cardinality of the set. It is denoted by |A| or #A.
* Example: If A = {1, 2, 3, 4, 5}, then |A| = 5.
    tricky question:
    * | ∅ | = 0
    * | {∅} | = 1
    * | 1, {1, 3}, ∅, x | = 4
    In one word, ∅ != {∅} => First one is empty set and second one is a set with one element which is empty set.

### Venn Diagram
A Venn diagram is a diagram that shows all possible logical relations between a finite collection of different sets. 
 - The universal set is represented by a rectangle.

### Power set
The power set of a set is the set of all possible subsets of a set. It is denoted by P(A).
* Example: If A = {1, 2}, then P(A) = {∅, {1}, {2}, {1, 2}}.
* Cardinality, |P(A)| = 2^n, where n is the number of elements in set A. 

### Operations on sets
1. **Union**: The union of two sets A and B is the set of elements that are in A, in B, or in both. It is denoted by A ∪ B.
    * Example: If A = {1, 2, 3} and B = {3, 4, 5}, then A ∪ B = {1, 2, 3, 4, 5}.
2. **Intersection**: The intersection of two sets A and B is the set of elements that are in both A and B. It is denoted by A ∩ B.
    * Example: If A = {1, 2, 3} and B = {3, 4, 5}, then A ∩ B = {3}.
3. **Difference**: The difference of two sets A and B is the set of elements that are in A but not in B. It is denoted by A - B.
    * Example: If A = {1, 2, 3} and B = {3, 4, 5}, then A - B = {1, 2}.
4. **Complement**: The complement of a set A with respect to the universal set U is the set of elements in U that are not in A. It is denoted by A'.
    * Example: If U = {1, 2, 3, 4, 5} and A = {1, 2, 3}, then A' = {4, 5}.
5. **Disjoint sets**: Two sets are said to be disjoint if they have no elements in common.
    * Example: If A = {1, 2, 3} and B = {4, 5}, then A and B are disjoint sets.
6. **Pairwise disjoint sets**: A collection of sets is said to be pairwise disjoint if every pair of sets in the collection is disjoint.
    * Example: If A = {1, 2}, B = {3, 4}, and C = {5, 6}, then A, B, and C are pairwise disjoint sets.

### Laws of set theory
1. **Commutative laws**: A ∪ B = B ∪ A and A ∩ B = B ∩ A
2. **Associative laws**: A ∪ (B ∪ C) = (A ∪ B) ∪ C and A ∩ (B ∩ C) = (A ∩ B) ∩ C
3. **Distributive laws**: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
4. **Identity laws**: A ∪ ∅ = A and A ∩ U = A