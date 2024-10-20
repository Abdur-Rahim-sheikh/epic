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

- Even in bootstrapping, the first compiler needs to be written in other established language. Let's say python built the first compiler of a new language called ChukEm. Now in chukEm language we desgined a very basic compiler program and compiled it with the python compiler. 
As it's the basic one it's very inefficient and cannot understand complex logic. Now we wrote another compiler CE-v2, which the version one is able to compile but it has more capability and efficiency. But this time it was self-hosted. And gradually we improve the power of the self-hosted compiler.

#### Just in Time Compilation (JIT)
- **Just in Time Compilation:** The source code is compiled at runtime. It is used in virtual machines like Java, .NET, etc.
- Explanation:
    - JVM compiles the source code into bytecode.
    - As the execution proceeds, the JVM profiles the code and identifies the `hot methods` which are executed frequently.
    - The JVM then uses the JIT compiler to compile the hot methods into native machine code.
    - The native machine code is then executed for that method instead of the bytecode.


```mermaid
flowchart TB;

subgraph MainFlow
    java([Java Program]) -- Compile --> bytecode[Java Bytecode];
    bytecode --> Interpreter;
    Interpreter --> ExecDecision{Has Native Code?};
    ExecDecision -- Yes --> ExecuteCompiled[Execute Stored native Code];
    ExecDecision -- No --> ExecuteInterpreted[Execute Interpreted Code];
    ExecuteCompiled & ExecuteInterpreted --> Execution;
    Execution --> Output[(Output)];
end

subgraph HotMethod[Hot Method]
    Profiler -- "If Method Hot?" --> JIT[Just in Time Compiler];
    JIT -- "Compile to Native Code" --> NativeCode[Native Machine Code & Store in Interpreter];
end

Interpreter -- Execute's Periodically --> Profiler;
NativeCode --store --> Interpreter;
```
