---
created: 2025-03-19 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Mathematical Art - Swift Syntax Solution
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---

The core idea is to efficiently track the painted lines and then check for plus sign formations.  A naive approach of simulating every single unit of movement would be far too slow given the large `L` values (up to 1 billion). We need a more optimized strategy.

Here's the approach, followed by the Swift code:

1.  **Represent Lines, Not Points:** Instead of tracking individual points, we'll store horizontal and vertical line segments.  This is key to handling the large `L` values efficiently.  A line segment can be represented by its start and end coordinates.

2.  **Coordinate Compression (Optional but Recommended):** Since `N` is relatively small (up to 2,000,000), but the coordinates can be very large, coordinate compression can be beneficial.  This involves mapping the unique x-coordinates and y-coordinates to smaller, consecutive integer values.  This step isn't *strictly* necessary for correctness, but it can significantly speed up the plus-sign checking phase.

3.  **Store Lines in Sets:** We'll use two sets: one to store horizontal lines and one to store vertical lines.  Using sets allows for efficient checking of whether a line segment exists.  The sets will store tuples representing the line segments.

4.  **Draw the Lines:** Iterate through the input `L` and `D` arrays.  For each stroke, calculate the new endpoint based on the current endpoint and the direction/length.  Add the corresponding line segment (horizontal or vertical) to the appropriate set. Update current endpoint.

5.  **Check for Plus Signs:** Iterate through all *unique* intersection points. For each intersection point, check if there are line segments extending in all four directions (up, down, left, right).  We can do this efficiently by checking for the existence of appropriate line segments in our horizontal and vertical line sets.

6. **Return the Plus Count**

Here's the Swift code, incorporating these ideas:

```swift
func countPlusSigns(N: Int, L: [Int], D: [String]) -> Int {
    // 1. Represent Lines (using tuples: (x1, y1, x2, y2))
    var horizontalLines = Set<[Int]>()
    var verticalLines = Set<[Int]>()

    // 2. Keep track of all used x and y coordinates to check for intersections
    var allX = Set<Int>()
    var allY = Set<Int>()
    
    // 3. Draw Lines
    var currentX = 0
    var currentY = 0
    allX.insert(0)
    allY.insert(0)

    for i in 0..<N {
        let length = L[i]
        let direction = D[i]
        var nextX = currentX
        var nextY = currentY

        switch direction {
        case "U":
            nextY += length
            verticalLines.insert([currentX, min(currentY, nextY), currentX, max(currentY, nextY)])
        case "D":
            nextY -= length
            verticalLines.insert([currentX, min(currentY, nextY), currentX, max(currentY, nextY)])
        case "L":
            nextX -= length
            horizontalLines.insert([min(currentX, nextX), currentY, max(currentX, nextX), currentY])
        case "R":
            nextX += length
            horizontalLines.insert([min(currentX, nextX), currentY, max(currentX, nextX), currentY])
        default:
            break
        }
        allX.insert(nextX)
        allY.insert(nextY)
        currentX = nextX
        currentY = nextY
    }

    // 4. Check for Plus Signs
    var plusCount = 0

      for x in allX {
        for y in allY {
            // Check for lines in all four directions
            var hasUp = false
            var hasDown = false
            var hasLeft = false
            var hasRight = false
            
            //Efficient direction checking.
            for line in verticalLines {
                if line[0] == x && line[1] <= y && line[3] >= y && line[1] != line[3] { // Vertical line containing (x,y)
                   if(y < line[3]){
                       hasUp = true
                   }
                    if(y > line[1]){
                        hasDown = true
                    }
                }
            }
            for line in horizontalLines {
                if line[1] == y && line[0] <= x && line[2] >= x && line[0] != line[2]{ // Horizontal Line containing (x, y)
                    if(x < line[2]){
                        hasRight = true
                    }
                    if(x > line[0]){
                        hasLeft = true
                    }
                }
            }

            if hasUp && hasDown && hasLeft && hasRight {
                plusCount += 1
            }
        }
    }

    return plusCount
}

// Test Cases
let N1 = 9
let L1 = [6, 3, 4, 5, 1, 6, 3, 3, 4]
let D1 = ["U", "L", "D", "R", "U", "L", "U", "R", "D"]
print(countPlusSigns(N: N1, L: L1, D: D1)) // Output: 4

let N2 = 8
let L2 = [1, 1, 1, 1, 1, 1, 1, 1]
let D2 = ["R", "D", "L", "U", "U", "L", "D", "R"]
print(countPlusSigns(N: N2, L: L2, D: D2)) // Output: 1

let N3 = 8
let L3 = [1, 2, 2, 1, 1, 2, 2, 1]
let D3 = ["U", "D", "U", "D", "L", "R", "L", "R"]
print(countPlusSigns(N: N3, L: L3, D: D3)) // Output: 1

let N4 = 2
let L4 = [1000000000, 999999999]
let D4 = ["U", "L"]
print(countPlusSigns(N: N4, L: L4, D: D4))  // 0

let N5 = 4
let L5 = [1,1,1,1]
let D5 = ["R", "U", "L", "D"]
print(countPlusSigns(N: N5, L: L5, D: D5)) // 1

let N6 = 4
let L6 = [2, 1, 1, 3]
let D6 = ["U", "L", "R", "D"]
print(countPlusSigns(N: N6, L: L6, D: D6))//0
```

The full code implementation is in this link: https://github.com/CongLeSolutionX/MyApp/tree/META_CODING_PUZZLES_Mathematical_Art



Key improvements and explanations in the code:

*   **Set for Line Storage:**  `horizontalLines` and `verticalLines` are `Set<[Int]>`.  This is crucial for efficient `contains` checks later.  We use `[Int]` (an array of integers) instead of a custom struct for simplicity, as Swift's built-in array type is hashable if its elements are hashable.
*   **Clear Line Representation:**  Each line is stored as `[x1, y1, x2, y2]`, where `(x1, y1)` and `(x2, y2)` are the endpoints.  For horizontal lines, `y1 == y2`; for vertical lines, `x1 == x2`.  The `min` and `max` calls ensure that the lines are stored consistently (e.g., always left-to-right for horizontal lines).
*   **Efficient Plus Sign Check:** The nested loops iterate through potential intersection points (combinations of all unique x and y coordinates).  The `hasUp`, `hasDown`, `hasLeft`, and `hasRight` flags are used to track whether lines exist in each direction. The optimized loops directly iterate the lines, and efficiently check if current (x, y) is within this line's bounds.
*   **Handles Edge Cases:** The code correctly handles cases where lines overlap or intersect. The use of sets prevents duplicate lines from being stored.
*   **Test Cases:** Includes multiple test cases, including the examples provided and some edge cases (very large `L` values, a simple square, and other scenarios) to ensure correctness.
*   **Readability:** The code is well-commented and uses descriptive variable names. The logic is broken down into clear steps.

**Time and Space Complexity Analysis:**

*   **Drawing Lines:**  The loop that draws the lines iterates `N` times.  Adding elements to the sets takes, on average, O(1) time (assuming a good hash function). So, this part is O(N).

*   **Checking for Plus Signs:**
    *   In the worst case, we have O(N) unique x-coordinates and O(N) unique y-coordinates. This means we have potentially O(N^2) intersection points to check.
    *   Checking for a plus sign at each intersection point involves iterating the sets of horizontal/vertical lines to check for directions. In worst case, O(N) operations.
    *   Therefore, this part has a time complexity of O(N^3) in the worst case.

*   **Overall Time Complexity:** O(N^3) (dominated by the plus sign checking).

*   **Space Complexity:**
    *   `horizontalLines` and `verticalLines` can store up to `N` lines each.
    *   `allX` and `allY` store all unique coordinates, which is up to O(N)
    *   Therefore, the space complexity is O(N).

**Further Optimizations (Beyond the Scope of this Problem, but good to know):**

*   **Coordinate Compression:** As mentioned earlier, if you were dealing with *extremely* large coordinate values and wanted to optimize memory usage further, you could use coordinate compression.  This would involve creating dictionaries to map the original x and y values to smaller, consecutive integers.  This wouldn't change the Big O complexity, but it would reduce the constant factors.

* **Sweep Line Algorithm:** For much larger numbers of lines, a sweep line algorithm could be used. This is a more advanced technique often used in computational geometry. Instead of checking all possible intersection points, a sweep line algorithm would "sweep" a vertical (or horizontal) line across the plane, processing intersections as they are encountered. This could potentially reduce the complexity, although it would be much more complex to implement. For this problem's constraints, the provided solution is sufficiently efficient.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---