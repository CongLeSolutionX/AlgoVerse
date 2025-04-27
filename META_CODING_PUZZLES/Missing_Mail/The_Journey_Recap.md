---
created: 2025-03-19 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# The Journey Recap
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---



## Problem Recap

**Goal:** Maximize the total *expected* profit from collecting packages delivered over `N` days.
**Inputs:**
*   `N`: Number of days.
*   `V`: Array of package values for each day (`V[i]` for day `i`).
*   `C`: Cost to enter the room and collect packages.
*   `S`: Probability of packages being stolen at the end of any day *if not collected*.
**Dynamics:**
*   Expected value accumulates daily: `E_today = E_yesterday_after_theft + V[today]`.
*   If collected: Profit = `E_today - C`. Room becomes empty (`E = 0` for next day).
*   If not collected: `E_next_day_start = (1 - S) * E_today_end`.
*   High precision required (8 digits).

## Approach 1: Simple Greedy (Implied)

*   **Logic:** Collect whenever the potential value in the room (`currentExpectedValue + V[i]`) strictly exceeds the cost `C`.
*   **Rationale:** The most basic intuition – only collect if the immediate reward surpasses the cost.
*   **Outcome:** Likely fails many test cases.
*   **Limitations:** Completely ignores the risk (`S`). If `S` is high, waiting accumulates significant risk. If `S` is low, this might collect too early, resetting the potentially large accumulating value for a small immediate profit and losing future gains. It also ignores *how much* `potentialValue` exceeds `C`.

## Approach 2: `C/S` Threshold Greedy

*   **Logic:** Calculate a threshold `T = C / S`. Collect if the potential value `potentialValue = currentExpectedValue + V[i]` meets or exceeds this threshold (and also exceeds `C`). Handle `S=0` separately (threshold becomes infinite, effectively never collecting based on this rule alone).
*   **Rationale:** Tries to balance the cost `C` against the expected loss due to theft *in the next step* (`S * potentialValue`). Collecting is desirable if the cost `C` is less than the expected loss avoided (`S * potentialValue`), leading to `potentialValue > C / S`. This is a locally optimal decision criterion.
*   **Implementation Details:** Involved careful handling of `S=0`, floating-point comparisons using `epsilon`, and sometimes explicit logic for the last day or final collection after the loop.
*   **Outcome:** Improved results (e.g., 8/24 or 12/24 test cases passed). It handles some trade-offs correctly.
*   **Limitations:** Still fundamentally greedy. It only considers the immediate "cost vs. expected loss" trade-off. It fails to properly value the *future potential* that is preserved by *not* collecting. Sample Case #4 provided a clear counter-example where this logic dictated collecting, but the optimal solution involved waiting, even though the `C/S` threshold was met. The value `(1-S)*potentialValue` carried forward might enable much larger future profits that outweigh the immediate gain minus cost.

## Approach 3: Dynamic Programming - Conceptualization

*   **Realization:** The failure of greedy methods indicates that the optimal decision on day `i` depends on the expected outcome of following the optimal strategy from day `i+1` onwards. This defines an optimal substructure suitable for Dynamic Programming.
*   **State Definition:** Define `f(i, E)` as the maximum expected *additional* profit obtainable from the start of day `i` to the end, given the expected value currently in the room is `E`. The goal is `f(0, 0)`.
*   **Recurrence Relation:**
    `f(i, E) = max( Profit_if_Collect, Profit_if_Dont_Collect )`
    `Profit_if_Collect = (E + V[i] - C) + f(i+1, 0)`
    `Profit_if_Dont_Collect = f(i+1, (1 - S) * (E + V[i]))`
*   **Base Case:** `f(N, E) = max(0.0, E - C)` (final collection decision after day N-1).
*   **Key Insight:** The value function `f(i, E)` is convex with respect to `E`. This implies that for any given day `i`, there should exist a threshold value for the potential `E + V[i]`. If the potential value meets or exceeds this threshold, collecting is optimal; otherwise, waiting is optimal.
*   **Challenge:** The state `E` is continuous (`Double`). Standard DP tabulation (filling a table) is infeasible due to the infinite possible values of `E`. Memoization might work with discretization or hashing, but precision issues make this very difficult and unreliable.

## Approach 4: Dynamic Programming - Backward Threshold Calculation (Successful Approach)

*   **Core Idea:** Since we know a threshold `T[i]` exists for the `potentialValue` on day `i` due to convexity, can we calculate these thresholds directly without computing the full `f(i, E)` function? Yes, by working backward.
*   **Threshold Definition:** `T[i]` is the specific `potentialValue` (`v`) where the expected profit from collecting equals the expected profit from not collecting.
    `(v - C) + f(i+1, 0) = f(i+1, (1 - S) * v)`
*   **Backward Calculation:**
    1.  Start from `i = N-1` down to `0`. Assume thresholds `T[i+1], ..., T[N-1]` are already known.
    2.  To find `T[i]`, we need to evaluate `f(i+1, 0)` and `f(i+1, (1 - S) * v)`.
    3.  **`calculateFutureProfit` Function:** Create a helper function that simulates the process *forward* from a `startDay` with a `startE`, using the *already computed future thresholds* (`T[startDay], ..., T[N-1]`) to make optimal decisions at each step in the simulation. This function effectively calculates `f(startDay, startE)`.
    4.  **Binary Search:** The threshold equation `Balance(v) = [(v - C) + f(i+1, 0)] - f(i+1, (1 - S) * v) = 0` needs to be solved for `v`. Since `Balance(v)` is monotonic (non-decreasing), we can use binary search over a range of possible `potentialValue`s (`v`) to find the root `v` where `Balance(v)` transitions from negative to non-negative. This root is the optimal threshold `T[i]`. Use sufficient iterations (e.g., 100) for high precision with `Double`.
    5.  Store `T[i]`. Repeat for the previous day.
*   **Forward Pass:** Once all optimal thresholds `T[0], ..., T[N-1]` are computed, perform a final forward simulation from day 0:
    *   Maintain `currentExpectedValue`.
    *   On day `i`, calculate `potentialValue = currentExpectedValue + V[i]`.
    *   Compare `potentialValue` against the computed `T[i]`.
    *   Collect if `potentialValue >= T[i]` (and `potentialValue > C`), update `totalProfit`, reset `currentExpectedValue = 0`.
    *   Otherwise, update `currentExpectedValue = (1 - S) * potentialValue`.
    *   The final `totalProfit` accumulated during this pass is the maximum expected profit. (The final post-loop collection is implicitly handled by the `calculateFutureProfit` logic used during threshold calculation and potentially verified in the final forward pass logic, ensuring the value `f(N, E) = max(0, E-C)` is correctly applied).
*   **Complexity:** `O(N^2 * log(ValueRange))`, which was acceptable.
*   **Precision:** Using `Double` internally and a small `epsilon` was crucial.

## Why the Final Approach Worked

1.  **Optimal Substructure:** It correctly identified and utilized the problem's DP nature.
2.  **Time-Varying Decisions:** It acknowledged that the optimal decision (threshold) is not fixed but changes depending on the remaining time horizon (`N-i`) and the values (`V`) yet to come, implicitly captured by the backward calculation.
3.  **Correct Valuation of Future:** The thresholds derived from the `f(i+1, E)` function accurately balanced the immediate profit of collecting against the expected future profit of *not* collecting and allowing the value to potentially grow (despite theft risk).
4.  **Circumvented Continuous State:** Instead of calculating the full `f(i, E)` function, it focused only on finding the critical decision points (the thresholds `T[i]`), which was computationally feasible.
5.  **Precise Calculation:** The use of `Double` and binary search allowed for the high precision required to find the correct thresholds.

This iterative process of proposing a model, testing it, analyzing failures (especially against insightful examples like Sample Case #4), and refining the model based on optimal control principles (DP, convexity, thresholds) led to the correct solution.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---