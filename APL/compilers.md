### Compilers
<img src="compilation_phases.png" width="600" height="450" style="filter: brightness(90%);">

#### Lexical Analysis vs Syntax Analysis
- **Lexical Analysis:** Converts the source code into tokens.
- **Syntax Analysis:** Converts the tokens into a parse tree.

#### compilation + interpretation
```mermaid
flowchart LR
    S([Source Program])--> T(Translator);
    T --> IP(Intermediate Program);
    IP --> vm(Virtual Machine)
    I[/Input/] --> vm
    vm --> O[/Output/]
```

#### Linking
- **Static Linking:** The linking is done at compile time.
- **Dynamic Linking:** The linking is done at runtime.

```mermaid
flowchart LR
    S([Source Program])--> C(Compiler);
    C --Object Code --> L(Linker);
    LR[/Library Routine/] --> L;
    L --> O[/Output/]
```

Above diagram shows a dynamic linking process.

#### Cross Compilation or transpilation
- **Cross Compilation:** The source code is compiled on one machine and the object code is run on another machine.

- **Transpilation:** The source code is converted from one language to another language.

```mermaid
flowchart LR
    S([Source Program])--Compiler 1--> ASP(Alternative Source Program e.g. C);
    ASP --Compiler 2--> O[/Assembly Language/]
```

#### Bootstrapping
- **Bootstrapping:** The process of writing a compiler in the language that it compiles. Which is called self-hosting.
- How It's done? Initially, a compiler is written in another language. Then the compiler is compiled using the existing compiler. The new compiler is then used to compile itself.

#### Just in Time Compilation (JIT)
- **Just in Time Compilation:** The source code is compiled at runtime. It is used in virtual machines like Java, .NET, etc.

```mermaid
flowchart TD;
    java([Java Program]) -- Java Compiler --> byte(Java Byte Code);
    byte --> BI(Byte Code Interpreter);
    subgraph compilation;
        I[/Input/] --> BI;
        BI --> O[/Output/]
    end
    subgraph JIT[Just in Time Compilation];
        direction LR;
        Input --> ML(Machine Language)
        ML --> Output
    end
    byte --> ML
```