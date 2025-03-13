---
created: 2025-03-12 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://www.packtpub.com/en-us/product/python-data-structures-and-algorithms-9781786467355"
---



# Sorting Algorithms
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


This document is an expansion of the initial version [here](./Sorting_Algorithms.md), exploring various sorting algorithms in Python, focusing on their characteristics, performance, and implementation details. We'll cover both comparison-based and non-comparison-based sorting techniques, analyzing their time and space complexities, stability, and suitability for different scenarios.


---

## Comparison-Based Sorting Algorithms

Comparison-based sorting algorithms determine the order of elements by comparing pairs of elements.  The fundamental operation is the comparison between two elements.

### Key Factors in Evaluating Sorting Algorithms

Several factors are crucial when evaluating the performance and suitability of a sorting algorithm:

*   **Time Complexity:**  Measures how the runtime of the algorithm grows as the input size (n) increases.  We usually consider the best-case, average-case, and worst-case scenarios, often expressed using Big O notation (e.g., O(n), O(n log n), O(n^2)).
*   **Space Complexity:**  Measures the amount of extra memory (auxiliary space) the algorithm requires.  In-place algorithms use O(1) extra space, while others might require O(n) or more.
*   **Stability:** A sorting algorithm is stable if it preserves the relative order of equal elements.  If two elements have the same value, their original order in the input array is maintained in the sorted output.
*   **Ease of Implementation:**  Some algorithms are simpler to implement than others.  This can be a factor when choosing an algorithm for a specific task.
*   **Adaptability**: Adaptability refers to how efficiently an algorithm can handle nearly sorted input.  Adaptive algorithms perform better when the input is already partially sorted.

---

### Bubble Sort

Bubble Sort is a simple, intuitive sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.  The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

*   **Mechanism:**  Compares adjacent elements and swaps them if they are out of order.  Larger (or smaller, depending on the desired order) elements "bubble" to the end of the list with each pass.
*   **Time Complexity:**
    *   Worst-case: O(n^2) - Occurs when the input array is in reverse order.
    *   Average-case: O(n^2)
    *   Best-case: O(n) - Occurs when the input array is already sorted.  An optimized version of Bubble Sort can detect this and terminate early.
*   **Space Complexity:** O(1) - In-place algorithm.
*   **Stability:** Stable.
*    **Pseudocode**

    ```md
    procedure bubbleSort(A : list of sortable items)
        n = length(A)
        repeat
            swapped = false
            for i = 1 to n-1 inclusive do
                /* if this pair is out of order */
                if A[i-1] > A[i] then
                    /* swap them and remember something changed */
                    swap(A[i-1], A[i])
                    swapped = true
                end if
            end for
        until not swapped
    end procedure
    ```


---

### Insertion Sort

Insertion Sort builds the final sorted array one item at a time.  It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.  However, it is very efficient for small datasets or nearly sorted data.

*   **Mechanism:**  Iterates through the input array, consuming one element at a time.  For each element, it finds the correct position within the already-sorted portion of the array and inserts it there, shifting larger elements to the right.
*   **Time Complexity:**
    *   Worst-case: O(n^2) - Occurs when the input array is in reverse order.
    *   Average-case: O(n^2)
    *   Best-case: O(n) - Occurs when the input array is already sorted.
*   **Space Complexity:** O(1) - In-place algorithm.
*   **Stability:** Stable.
*   **Adaptability:** Highly adaptive; performs very well on nearly sorted data.
*   **Pseudocode**

    ```md
    procedure insertionSort(A : list of sortable items)
        n = length(A)
        for i = 1 to n - 1 inclusive do
            /* store A[i] to the variable value */
            value = A[i]
            j = i - 1
            /* move elements of A[0..i-1], that are greater than value,
               to one position ahead of their current position */
            while j >= 0 and A[j] > value do
                A[j + 1] = A[j]
                j = j - 1
            end while
            A[j + 1] = value
        end for
    end procedure
    ```

---

### Selection Sort

Selection Sort divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list.  Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.  The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

*   **Mechanism:**  Finds the minimum (or maximum) element in the unsorted portion of the array and swaps it with the first element of the unsorted portion.
*   **Time Complexity:**
    *   Worst-case: O(n^2)
    *   Average-case: O(n^2)
    *   Best-case: O(n^2) - Selection Sort's performance is not affected by the initial order of the input.
*   **Space Complexity:** O(1) - In-place algorithm.
*   **Stability:** Typically unstable, but can be implemented stably with slight modifications (at the cost of potentially increased space complexity).
*    **Pseudocode:**
    ```
    procedure selectionSort(A : list of sortable items)
        n = length(A)
        for i = 0 to n - 2 inclusive do
            /* find the minimum element in the unsorted A[i .. n-1] */
            /* assume the minimum is the first element */
            minIndex = i
            /* test against elements after i to find the smallest */
            for j = i + 1 to n - 1 inclusive do
                /* if this element is less, then it is the new minimum */
                if A[j] < A[minIndex] then
                    /* found new minimum; remember its index */
                    minIndex = j
                end if
            end for
            /* swap A[i] and A[minIndex] if i is not minIndex*/
            if minIndex != i then
                swap(A[i], A[minIndex])
            end if
        end for
    end procedure
    ```

```

---

### Quick Sort

Quick Sort is a highly efficient, divide-and-conquer sorting algorithm.  It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.  The sub-arrays are then recursively sorted.

*   **Mechanism:**
    1.  **Pivot Selection:** Choose an element from the array to serve as the pivot.  Different pivot selection strategies exist (e.g., first element, last element, random element, median-of-three).
    2.  **Partitioning:** Rearrange the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it.  The pivot is now in its final sorted position.
    3.  **Recursion:** Recursively apply the above steps to the sub-arrays of elements less than and greater than the pivot.
*   **Time Complexity:**
    *   Worst-case: O(n^2) - Occurs when the pivot selection consistently results in unbalanced partitions (e.g., always choosing the smallest or largest element).
    *   Average-case: O(n log n)
    *   Best-case: O(n log n) - Occurs when the pivot selection consistently results in balanced partitions.
*   **Space Complexity:** O(log n) average, O(n) worst-case due to recursive calls.  The space complexity depends on the implementation and the depth of the recursion.  In-place partitioning is possible, but the recursive calls still consume stack space.
*   **Stability:** Typically unstable.
*   **Pseudocode**
    ```
    procedure quickSort(A : list of sortable items, low : integer, high : integer)
        if low < high then
            p = partition(A, low, high)
            quickSort(A, low, p - 1)
            quickSort(A, p + 1, high)
        end if
    end procedure

    procedure partition(A : list of sortable items, low : integer, high : integer)
        // pivot (Element to be placed at right position)
        pivot = A[high]

        i = (low - 1)  // Index of smaller element and indicates the
                       // correct position of pivot found so far

        for j = low to high - 1 inclusive do
            // If current element is smaller than the pivot
            if A[j] < pivot then
                i = i + 1  // increment index of smaller element
                swap A[i] and A[j]
            end if
        end for
        swap A[i + 1] and A[high]
        return (i + 1)
    end procedure
    ```

---

### Merge Sort

Merge Sort is another efficient, divide-and-conquer sorting algorithm. It divides the input array into two halves, calls itself recursively for the two halves, and then merges the two sorted halves.

*   **Mechanism:**
    1.  **Divide:** Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
    2.  **Conquer:** Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
*   **Time Complexity:**
    *   Worst-case: O(n log n)
    *   Average-case: O(n log n)
    *   Best-case: O(n log n) - Merge Sort's performance is consistent regardless of the initial order of the input.
*   **Space Complexity:** O(n) - Requires auxiliary space proportional to the input size for the merging process.  Not in-place.
*   **Stability:** Stable.
* **Pseudocode:**
    ```
    procedure mergeSort(A : list of sortable items, low : integer, high : integer)
      if low >= high then
          return  // Returns recursively
      end if

      mid = (low + high) / 2
      mergeSort(A, low, mid)  // Sort the left half
      mergeSort(A, mid + 1, high)  // Sort the right half
      merge(A, low, mid, high)  // Merge the two sorted halves
    end procedure
    
    procedure merge(A : list of sortable items, low : integer, mid : integer, high : integer)
      n1 = mid - low + 1
      n2 = high - mid

      // Create temp arrays
      L = new array[n1]
      R = new array[n2]

      // Copy data to temp arrays L[] and R[]
      for i = 0 to n1 - 1 inclusive do
        L[i] = A[low + i]
      end for
      for j = 0 to n2 - 1 inclusive do
        R[j] = A[mid + 1 + j]
      end for

      // Merge the temp arrays back into A[low..high]
      i = 0     // Initial index of first subarray
      j = 0     // Initial index of second subarray
      k = low     // Initial index of merged subarray

      while i < n1 and j < n2 do
        if L[i] <= R[j] then
          A[k] = L[i]
          i = i + 1
        else
          A[k] = R[j]
          j = j + 1
        end if
        k = k + 1
      end while

      // Copy the remaining elements of L[], if there are any
      while i < n1 do
        A[k] = L[i]
        i = i + 1
        k = k + 1
      end while

      // Copy the remaining elements of R[], if there are any
      while j < n2 do
        A[k] = R[j]
        j = j + 1
        k = k + 1
      end while
    end procedure
    ```

---

### Heap Sort

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.  A binary heap is a complete binary tree where each node is greater than or equal to (in a max-heap) or less than or equal to (in a min-heap) its children.

*   **Mechanism:**
    1.  **Build Max Heap:**  Transform the input array into a max-heap.  This ensures that the largest element is at the root of the heap.
    2.  **Repeatedly Extract Max:**  Swap the root (largest element) with the last element of the heap, reducing the heap size by one.  Then, "heapify" the reduced heap to restore the max-heap property.  Repeat this process until the heap size is 1.
*   **Time Complexity:**
    *   Worst-case: O(n log n)
    *   Average-case: O(n log n)
    *   Best-case: O(n log n)
*   **Space Complexity:** O(1) - In-place algorithm (if implemented iteratively).
*   **Stability:** Unstable.

*   **Pseudocode**
    ```
    procedure heapSort(A : list of sortable items)
        n = length(A)

        // Build max heap
        for i = n / 2 - 1 downto 0 inclusive do
            heapify(A, n, i)
        end for

        // One by one extract elements
        for i = n - 1 downto 0 inclusive do
            // Move current root to end
            swap(A[0], A[i])

            // call max heapify on the reduced heap
            heapify(A, i, 0)
        end for
    end procedure

    procedure heapify(A : list of sortable items, n : integer, i : integer)
        largest = i  // Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2

        // See if left child of root exists and is greater than root
        if left < n and A[left] > A[largest] then
            largest = left
        end if

        // See if right child of root exists and is greater than
        // the largest so far
        if right < n and A[right] > A[largest] then
            largest = right
        end if

        // Change root, if needed
        if largest != i then
            swap(A[i], A[largest])

            // Recursively heapify the affected sub-tree
            heapify(A, n, largest)
        end if
    end procedure
    ```

---

## Non-Comparison-Based Sorting Algorithms

Non-comparison-based sorting algorithms do not rely on comparing elements to determine their order.  Instead, they use other properties of the elements, such as their digits (in the case of integers) or their distribution.

### Bucket Sort

Bucket Sort is a distribution-based sorting algorithm that works by distributing the elements of an array into a number of buckets.  Each bucket is then sorted individually, either using a different sorting algorithm (like insertion sort) or by recursively applying the bucket sort algorithm.

*   **Mechanism:** Distribute elements into buckets based on their values. Then, sort each bucket and concatenate the buckets.
* **When it's good:** When the input data is uniformly distributed over a known range.
* **Time Complexity**:
    *   Worst-case:  O(n^2) (if all elements fall into the same bucket and a quadratic sorting algorithm is used for the buckets)
    *   Average-case: O(n + k), where n is the number of elements and k is the number of buckets.  This assumes a uniform distribution and that the bucket sorting is efficient.
    * Best-Case: O(n+k)
*   **Space Complexity:** O(n + k)
*   **Stability:** Stable (if the underlying sorting algorithm used for the buckets is stable).
* **Pseudocode:**

```
procedure bucketSort(A : list of sortable items, k : number of buckets)
    buckets = array of k empty lists
    M = the maximum key value in the input array
    for i = 0 to length(A) - 1 inclusive do
        insert A[i] into buckets[floor(k * A[i] / M)]
    end for
    for i = 0 to k - 1 inclusive do
        sort(buckets[i])  // Use insertion sort or another suitable algorithm
    end for
    return the concatenation of buckets[0], ...., buckets[k-1]
end procedure

```

---

### Radix Sort

Radix Sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.  A positional notation is required, but because integers can represent strings of characters (e.g., names or dates) and specially formatted floating point numbers, radix sort is not limited to integers.

*   **Mechanism:** Sorts elements digit by digit, starting from the least significant digit (LSD) to the most significant digit (MSD) or vice versa. It uses a stable sorting algorithm (like counting sort) as a subroutine to sort the digits at each position.
* **Time Complexity**:
  *   Worst-case: O(nk), where n is the number of elements and k is the number of digits (or the maximum number of digits in any element).
  *   Average-case: O(nk)
  *   Best-case: O(nk)
*   **Space Complexity:** O(n + k)
*   **Stability:** Stable.
*   **Pseudocode**
    ```
    procedure radixSort(A : list of sortable items, d : number of digits)
        for i = 0 to d - 1 inclusive do
            // Use a stable sort to sort array A on digit i
            countingSort(A, i) // Example using Counting Sort
        end for
    end procedure
    
    procedure countingSort(A, digit_place)
       // Implementation of counting sort based on the current digit_place
       // Create a count array (size depends on the base, e.g., 10 for decimal)
       // Store the count of each digit in count array
       // Modify the count array to store the actual position of this digit in output array
       // Build the output array
    end procedure
    ```
    **Counting Sort (Subroutine for Radix Sort)**: Counting sort is often used as the stable sorting subroutine in radix sort. It works by counting the occurrences of each distinct element (in this case, each digit) and using those counts to determine the positions of the elements in the sorted output.

---

## Summary Table

| Algorithm       | Worst-Case Time Complexity | Average-Case Time Complexity | Best-Case Time Complexity | Space Complexity | Stability | Adaptability |
| --------------- | -------------------------- | ---------------------------- | -------------------------- | ---------------- | --------- | ------------ |
| Bubble Sort     | O(n^2)                     | O(n^2)                       | O(n)                      | O(1)             | Stable    | Yes          |
| Insertion Sort  | O(n^2)                     | O(n^2)                       | O(n)                      | O(1)             | Stable    | Yes          |
| Selection Sort  | O(n^2)                     | O(n^2)                       | O(n^2)                     | O(1)             | Unstable  | No           |
| Quick Sort      | O(n^2)                     | O(n log n)                    | O(n log n)                    | O(log n) avg, O(n) worst | Unstable  | No           |
| Merge Sort      | O(n log n)                    | O(n log n)                    | O(n log n)                    | O(n)             | Stable    | No           |
| Heap Sort       | O(n log n)                    | O(n log n)                    | O(n log n)                    | O(1)             | Unstable  | No           |
| Bucket Sort     | O(n^2)                     | O(n + k)                     | O(n + k)                   | O(n + k)          | Stable    | Yes          |
| Radix Sort      | O(nk)                      | O(nk)                        | O(nk)                      | O(n + k)          | Stable    | No           |

---

## Choosing the Right Sorting Algorithm

The best sorting algorithm to use depends on the specific requirements of the task:

*   **Small datasets or nearly sorted data:** Insertion Sort is a good choice.
*   **Guaranteed O(n log n) performance:** Merge Sort or Heap Sort are suitable.  Merge Sort is stable, while Heap Sort is in-place.
*   **Average-case performance is most important:** Quick Sort is often the fastest in practice, but its worst-case performance should be considered.
* **Uniformly distributed data over a known range:** Consider Bucket sort.
*   **Sorting integers with a limited number of digits:** Radix Sort can be very efficient.
* **Stable Sorting is required:** Merge Sort, Insertion Sort, Bubble Sort and Radix Sort are stable.

----

## Mathematical Representation of Time Complexity

The time complexity of an algorithm is often represented using Big O notation.  Here's a formal definition:

A function *f(n)* is said to be O(g(n)) if there exist positive constants *c* and *n₀* such that:

$$
0 \le f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0
$$

This means that *f(n)* grows no faster than *g(n)*, up to a constant factor, for sufficiently large values of *n*.

For example, for Bubble Sort, in the worst case:

$$
f(n) = \frac{n(n-1)}{2} = \frac{1}{2}n^2 - \frac{1}{2}n
$$

We can say that *f(n)* is O(n^2) because we can choose *c* = 1 and *n₀* = 1, and the inequality holds:

$$
0 \le \frac{1}{2}n^2 - \frac{1}{2}n \le 1 \cdot n^2 \quad \text{for all } n \ge 1
$$






---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---