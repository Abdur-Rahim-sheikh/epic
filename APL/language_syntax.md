## Programming language syntax

#### Formal language are designed to be unambiguous and concise. 

#### Syntax vs Semantics
- Syntax: What constitutes a valid "text" in a language.
- Semantics: How one should interpret a valid "text".

#### Core components of a formal language
- There are 3 core components of a formal language
    - Alphabet: A set of finite symbols.
    - String: A finite sequence of symbols from the alphabet.
    - Language: A set of strings that are formed from the alphabet.

#### Formal grammer
To define a formal language, we use grammers. A grammer G = (N, T, P, S) consists of:
- N: A set of non-terminal symbols. (Generally uppercase letters)
- T: A set of terminal symbols. (Generally lowercase letters)
- P: A set of production rules. $ S \longrightarrow aSb | \epsilon $
- S: A start symbol. (Generally `S` represents the start symbol)

#### Noam Chomsky's hierarchy 
- **Type 0:** Recursively enumerable languages or Unrestricted grammars
- **Type 1:** Context-sensitive grammars
- **Type 2:** Context-free grammars, most common in programming languages
- **Type 3:** Regular grammars
