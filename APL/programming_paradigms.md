1. Types of programming
    - Imperative Programming
    - object-oriented programming
    - Concurrent Programming
    - Event-Driven Programming
    - Functional Programming
    - Scripting
    - constraint-based programming

2. Imperative Programming
    - The programmer tells the computer what to do by giving it a sequence of commands to perform. The computer performs the commands in the order they are given.
    - Key concepts:
        - variables
        - commands
        - procedures
        - data abstraction (recent addition)
3. Object-Oriented Programming
    - The programmer defines objects that interact with each other to solve a problem. Objects have attributes and methods that define their behavior.
    - Key concepts:
        - objects
        - classes and subclasses
        - inheritance
        - polymorphism
        
3. Concurrent Programming
    - The programmer writes programs that run multiple tasks at the same time. This can be done by using multiple threads or processes.
    - Key concepts:
        - threads
        - processes
        - synchronization
        - communication
        - mutual exclusion
            - Deadlock, livelock, and starvation
        - concurrent control abstractions (recent addition support reliability)

4. Event-Driven Programming
    - The programmer writes programs that respond to events. Events can be user actions, such as clicking a button, or system events, such as a timer expiring.
    - Key concepts:
        - events
        - event listeners

5. Functional Programming
    - The model of computation is the application of functions to arguments.
    - key concepts
        - Expressions
        - Functions
        - parametric polymorphism
        - data abstraction
        - lazy evaluation

        - Church-Rosser property,
            - If a term `t` can be reduced to terms `u` and `v`, then there exists a term `w` that `u` and `v` can be reduced to.
            - So the order of evaluation does not matter.
            - This property is also known as the diamond property.
            - Then the term holds "confluence" / "church-rosser property"
            - Church-rosser property is not possessed by any programming language that allows side effects. 


<img src="paradigm_comparison.png" alt="paradigm_comparison" width="500" height="450" style="filter: brightness(90%);">

6. Scripting
    - The programmer writes scripts that automate tasks. Scripts are usually interpreted rather than compiled.
    - Key concepts:
        - scripts
        - interpreted languages
        - automation
7. Constraint-Based Programming
    - The programmer defines constraints that must be satisfied to solve a problem. The computer uses constraint satisfaction algorithms to find a solution.
    - Key concepts:
        - assertions
        - horn clauses
        - relations

8. Multi-paradigm programming
    - The programmer uses multiple programming paradigms in the same program. This can be done to take advantage of the strengths of different paradigms.
    - Python
        - object-oriented, scripting, and functional programming, async, parallel, and distributed programming.
    - Scala
        - object-oriented and functional programming