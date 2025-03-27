---
created: 2025-03-26 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Tail Call Optimization (TCO) - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---



Below is a comprehensive breakdown covers the what, why, and how of Tail Call Optimization, using visual diagrams and code examples to illustrate the key concepts. It highlights the nuances of TCO in Swift, emphasizing the lack of a guarantee and the importance of understanding the potential for stack overflow if TCO is not applied. The use of multiple diagrams, mathematical concepts and illustrative examples, ensures the information is accessible and easy to understand.



## 1. What is a Tail Call? (Conceptual Explanation and Diagram)

Before diving into optimization, we need to understand what a "tail call" *is*. A tail call occurs when a function's *very last* action is to call *another* function (or itself, in the case of recursion). Importantly, after that call, the original function does *nothing* else – it doesn't perform any calculations, modify variables, or have any further instructions. It simply returns whatever the called function returns.

```mermaid
---
title: "What is a Tail Call?"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph LR
    subgraph Function_A["Function A"]
        A1[Do some work...]
        A2{Last action?}
        A2 -- "Yes, call Function B" --> B[Function B]
        A2 -- "No" --> C[Return Value]
        B --> D[Return Value from B]
    end
    style Function_A fill:#eef3,stroke:#333,stroke-width:2px
    B --> F[some actions...]
     style B fill:#fdd3,stroke:#333,stroke-width:2px
    
```

**Explanation of the Diagram:**

*   **`Function A`**:  Represents any function.
*   **`A1`**: Represents any work that the function might do *before* the potential tail call.
*   **`A2`**:  This is the crucial decision point.  Is the *last* action a function call?
*   **`Yes` (Tail Call):** If the last action is to call `Function B`, and `Function A` does nothing further except return `Function B`'s result, this is a tail call.
*   **`No` (Not a Tail Call):**  If `Function A` does *anything* after calling another function (even something as simple as adding 1 to the result), it's *not* a tail call.
*   **`Function B`**: Represents the function being called in the tail position.

---

## 2. Tail Call Optimization (TCO) - The Optimization

TCO is a compiler optimization. When a compiler detects a tail call, it can *reuse* the current function's stack frame instead of creating a new one for the called function. This has two major benefits:

*   **Stack Overflow Prevention:** In recursive functions, without TCO, each recursive call adds a new stack frame.  Deep recursion can lead to a stack overflow error (running out of stack memory). TCO prevents this because the stack doesn't grow with each call.
*   **Performance Improvement:**  Creating and destroying stack frames has a (small) overhead. TCO avoids this overhead, making tail-recursive functions potentially as efficient as loops.

```mermaid
---
title: "Tail Call Optimization (TCO) - The Optimization"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph LR
    subgraph Without_TCO["Without TCO<br>(Stack Growth)"]
        style Without_TCO fill:#fdd3,stroke:#333,stroke-width:2px
        A["Frame:<br>factorial(5)"] --> B["Frame:<br>factorial(4)"]
        B --> C["Frame:<br>factorial(3)"]
        C --> D["Frame:<br>factorial(2)"]
        D --> E["Frame:<br>factorial(1)"]
        E --> F["Frame:<br>factorial(0)"]
        F --> G["Return 1"]
        
    end

    subgraph With_TCO["With TCO<br>(Constant Stack Space)"]
        style With_TCO fill:#ddf3,stroke:#333,stroke-width:2px
        X["Frame:<br>factorial (n, acc)"]
        X --> X
    end

    
```

**Explanation of the Diagram:**

*   **`Without_TCO`**: This illustrates the typical stack behavior for a recursive function *without* TCO. Each call to `factorial` creates a new stack frame, leading to potential stack overflow for large inputs.
*   **`With_TCO`**:  This shows how TCO optimizes the stack.  The `factorial` function's frame is *reused* for each "recursive" call.  The `acc` (accumulator) parameter is the key to making this tail-recursive (explained below).

----

## 3. Tail Recursion: TCO's Best Friend

TCO is most beneficial in the context of *tail recursion*. Tail recursion is a special case of recursion where the recursive call is a tail call.  This allows the compiler to transform the recursion into a loop-like structure, avoiding stack growth.

**Example: Factorial (Non-Tail Recursive - Swift)**

```swift
func factorial(n: Int) -> Int {
    if n == 0 {
        return 1
    } else {
        return n * factorial(n: n - 1) // NOT a tail call
    }
}
```

This is *not* tail-recursive. The last operation is `n * factorial(n: n - 1)`. After `factorial(n: n - 1)` returns, the result must be multiplied by `n`.

**Example: Factorial (Tail Recursive - Swift)**

```swift
func factorialTail(n: Int, acc: Int = 1) -> Int {
    if n == 0 {
        return acc
    } else {
        return factorialTail(n: n - 1, acc: acc * n) // Tail call!
    }
}
```

This *is* tail-recursive.  We've introduced an accumulator parameter (`acc`). The *last* operation is the call to `factorialTail` itself.  No further calculation is done after the recursive call. All the work have finished prior calling the `factorialTail` function.

----

## 4. TCO in Swift: The Good, the Bad, and the Workaround

Here's the crucial point about Swift and TCO:

*   **Good (Optimization is Available) :** The Swift compiler *can* perform TCO, particularly in optimized builds (`-O`). Optimization is built into the Swift compiler, but there's no explicit keyword to *guarantee* it.
*   **Bad (No Guarantee):** Unlike some functional languages (e.g., Scheme), Swift *does not guarantee* TCO. There's no language-level enforcement. This is a very important thing to remember.
*   **Workaround (Manual Transformation):** If you absolutely need the guarantee of loop-like behavior (and stack safety), you can manually transform a tail-recursive function into a loop.

**Example: Factorial (Iterative - Swift - "Manual TCO")**

```swift
func factorialIterative(n: Int) -> Int {
    var acc = 1
    var currentN = n
    while currentN > 0 {
        acc *= currentN
        currentN -= 1
    }
    return acc
}
```

This version uses a `while` loop and achieves the same result as the tail-recursive version, but with guaranteed constant stack space.

---

## 5. Why Doesn't Swift *Guarantee* TCO?

There are several reasons for this design choice:

*   **Debugging:**  Retaining stack frames makes debugging easier.  You can see the full call history.  With TCO, the stack trace would be much shorter (and potentially less informative).
*   **Interoperability:**  Swift interoperates with Objective-C, which doesn't have TCO.
*   **Complexity:**  Guaranteeing TCO can add complexity to the compiler.
*   **Developer Control:**  The Swift designers likely wanted to give developers more control over performance characteristics.  If you *need* the loop-like behavior, you can write it explicitly.

---

## 6. Illustrative Use Cases

Here are the breakdowns of TCO's use cases and benefits with different scenarios:
```mermaid
---
title: "Illustrative Use Cases of Tail Call Optimization"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'themeVariables': {
      'fontSize': '12px',
      'fontFamily': 'Fantasy'
    }
  }
}%%
mindmap
    root((Tail Call Optimization Use Cases))
      Recursive_Algorithms
        Description[Algorithms naturally expressed recursively, like tree traversals, graph algorithms, and mathematical functions.]
        Benefit[Prevents stack overflow for deeply recursive calls.]
        Example[Calculating Fibonacci numbers, traversing a directory structure.]
      Functional_Programming
        Description[Functional programming paradigms often favor recursion over iteration.]
        Benefit[Makes recursion as efficient as iteration in many cases.]
        Example[Using `map`, `filter`, `reduce` implemented recursively.]
      Compilers_Interpreters
        Description[Used in compiler and interpreter implementations for function calls.]
        Benefit[Improves performance and prevents stack overflow.]
        Example[Implementing a recursive descent parser.]
      State_Machines
        Description[Representing state transitions as function calls.]
        Benefit[Allows for clean and maintainable state machine code.]
        Example[Implementing a game's AI or a network protocol.]
      Event_Loops
        Description[Handling asynchronous events with callbacks.]
        Benefit[Prevents stack growth in long-running event loops.]
        Example[Processing user input or network events.]

```

**Explanation:**

*   **Recursive Algorithms:** This is the classic use case. Many algorithms are naturally recursive.
*   **Functional Programming:** Functional languages often encourage recursion.
*   **Compilers/Interpreters:** TCO is used internally in compilers and interpreters.
*   **State Machines:** State transitions can be modeled as function calls.
*   **Event Loops:** Asynchronous event handling can use tail calls.

---

## 7. TCO vs. Non-TCO: Performance Comparison (Illustrative)

While we can't run benchmarks directly here, we can *conceptually* illustrate the performance difference:

```mermaid
---
title: "TCO vs. Non-TCO: Performance Comparison"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph LR
    subgraph Performance_Comparison["Performance Comparison<br> (Illustrative)"]
        style Performance_Comparison fill:#ddd3,stroke:#333,stroke-width:2px
        A["Large Input"] --> B{"Non-Tail Recursive"}
        A --> C{"Tail Recursive<br>(with TCO)"}
        B --> D["High Stack Usage, Potential Overflow, Slower"]
        C --> E["Constant Stack Usage, No Overflow, Faster"]
    end
```

*   **Large Input:**  The differences become more pronounced with larger inputs (deeper recursion).
*   **Non-Tail Recursive:**  High stack usage, potential for stack overflow, and slower execution due to stack frame overhead.
*   **Tail Recursive (with TCO):** Constant stack usage (like a loop), no risk of stack overflow, and faster execution.

---

## 8. Key Terms and Summary

```mermaid
---
title: "Tail Call Optimization - Key Terms and Summary"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'themeVariables': {
      'fontSize': '12px',
      'fontFamily': 'Fantasy'
    }
  }
}%%
mindmap
    root(("Tail Call Optimization<br>(TCO)"))
      Definition
        Short[Compiler optimization for tail calls.]
        Long[Reuses stack frame for tail calls, preventing stack growth and improving performance.]
      Tail_Call
        Definition[A function call that is the *last* operation performed by another function.]
      Tail_Recursion
        Definition[A special case of recursion where the recursive call is a tail call.]
      Benefits
        Stack_Overflow_Prevention[Avoids stack overflow errors in deeply recursive functions.]
        Performance_Improvement[Reduces overhead of creating new stack frames.]
      Swift_Specifics
        Available[The Swift compiler *can* perform TCO, especially with optimization flags.]
        Not_Guaranteed[Swift *does not guarantee* TCO at the language level.]
        Workaround[Manually transform tail-recursive functions into loops if stack safety is critical.]
      Use_Cases
        Recursive_Algorithms
        Functional_Programming
        Compilers_Interpreters
        State_Machines
        Event_Loops
      Alternatives
        Iterative_Solutions[Use loops instead of recursion.]
        
```




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---