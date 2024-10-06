## RAM is the first approximation of computer program similar to assembly language.

- There is an input tape, there is an output tape, and there are registers. 
In the registers, you can store any number. You can only read from the 
input tape and only write to the output tape.

**Example 1:**
- Let's find the amount of elements in a array that are greater than 5.
    - R[0] - has the length of the array.
    - [R[1], ... (R_0)] - array
    - R[1] - must contain the answer. (The final answer)

```asm
loop: 
    R5 = (R0) - 5
    GGZ R5, bigger_5
after_if:
    GGZ R0, loop
    R1 = R6
HALT
bigger_5:
    R6 = R6 + 1
    GOTO after_if
```

- Note: 
    - GGZ - Go to if greater than zero.
    - GLZ - Go to if less than zero.
    - GEZ - Go to if equal to zero.
    - GLEZ - Go to if less than or equal to zero.
    - () - means the value of the indexed register.


**Example 2:**
Let's imagine we have number in binary system, you need to convert it to decimal system
- R[0] - has the length of the binary number.
- [R[1], ... (R_0)] - binary number
- You need to return the number in R[R(0) + 1]

```asm

R6 = 1
loop:
    R7 = (R0) * R6
    R5 = R5 + R7
    R6 = R6 * 2
    R0 = R0 - 1
GGZ R0, loop
HALT
```