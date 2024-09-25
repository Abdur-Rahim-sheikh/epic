## There are some task to do in lab 1
link to the doc: [lab1](https://docs.google.com/document/d/1-sXsrMe71SvzVxSF8bey14EAN66hWJa3P95h89LKsMY/edit)
1. [Consider a table of early computer characteristics. You will see there that Zuse’s Z3 machine was Turing complete “in theory”. Research this a little: what does that mean? Why did that computer lack for being “practically Turing-complete”?](#task1)
2. [Consider Atanasoff–Berry computer. Was is Turing-complete? What were its pioneering contributions?](#task2)
3. [What language was named after the first ever programmer? Is it still used today? For what applications? What are the companies developing compilers for this language?](#task3)
4. [LAPACK is one of the modern standard libraries for linear algebra computations (employed, e.g., by Python’s NumPy package and by many others). What language is its reference implementation written in? Which other Python packages use some code written in that language?](#task4)
5. [Consider Jensen’s device that was mentioned in the slides. What are its pitfalls (not considering call-by-name inefficiency in general)? What are some other programming applications of call-by-name if it is supported by a language?](#task5)
6. [Languages either turing complete or not](#task6)



### Task 1
Consider a [table of early computer characteristics](https://en.wikipedia.org/wiki/History_of_computing_hardware#Early_digital_computer_characteristics). You will see there that Zuse’s Z3 machine was Turing complete “in theory”. Research this a little: what does that mean? Why did that computer lack for being “practically Turing-complete”?

**Response:** The Z3's lack of conditional branching and fixed-point arithmetic operations made it "Theoritically" turing complete, because it had no loop control or conditional branching. Though without them we can theoritically solve a algorithm but would need huge ammount of line which no computer storage might be able to hold, so it was not "Practically" turing complete. 

### Task 2
Consider [Atanasoff–Berry computer](https://en.wikipedia.org/wiki/Atanasoff%E2%80%93Berry_computer). Was is Turing-complete? What were its pioneering contributions?

 **Response:** The Atanasoff–Berry computer was neither programmable nor turing complete. It was a special-purpose machine designed to solve systems of linear algebraic equations. It was the first electronic digital computer. It was the first to use binary digits to represent data and perform calculations. It was the first to use electronic switches to perform calculations. 

### Task 3
What language was named after the first ever programmer? Is it still used today? For what applications? What are the companies developing compilers for this language?

**Response:** Ada was named after Ada Lovelace, the first ever programmer. Ada is still used today in the field of avionics, aerospace, and military systems. The companies developing compilers for Ada are AdaCore, Green Hills Software, and DDC-I.

### Task 4
LAPACK is one of the modern standard libraries for linear algebra computations (employed, e.g., by Python’s NumPy package and by many others). What language is its reference implementation written in? Which other Python packages use some code written in that language?

**Response:** The reference implementation of LAPACK is written in Fortran. Other Python packages that use some code written in Fortran are SciPy, scikit-learn, and pandas.


### Task 5
Consider [Jensen’s device](https://en.wikipedia.org/wiki/Jensen%27s_device) that was mentioned in the slides. What are its pitfalls (not considering call-by-name inefficiency in general)? What are some other programming applications of call-by-name if it is supported by a language?

**Response:** Jensen's device is a programming technique that allows the definition of recursive functions in languages that do not support recursion. The pitfall of Jensen's device is that it can be difficult to understand and maintain. Some other programming applications of call-by-name are lazy evaluation, memoization, and implementing control structures like loops and conditionals.

### Task 6
Languages either turing complete or not
| Language | Turing Complete | Why not? |
| --- | --- | --- |
| Python | &check; | ... |
| C | &check; | ... |
| Java | &check; | ... |
| JavaScript | &check; | ... |
| HTML | &cross; | Dose not have `Conditional Logic`, `Loops`, `Memory Manipulation` |
| CSS | &cross; | Dose not have `Conditional Logic`, `Loops`, `Limited State Management` |
| SQL | &cross; | Basic sql can not implement all algorithm, but with extension yes |
