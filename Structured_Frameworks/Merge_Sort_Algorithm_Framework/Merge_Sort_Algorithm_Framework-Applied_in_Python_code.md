---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---

# Merge Sort Algorithm Framework  - Applied in Python code

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## **1. Python Implementation of Merge Sort**

First, let's implement the standard Merge Sort algorithm in Python.

```python
# Merge Sort Implementation in Python

def merge_sort(arr):
    # Base case: arrays with less than 2 elements are already "sorted"
    if len(arr) <= 1:
        return arr

    # Divide step: split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer step: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine step: merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list
    """
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from left and right lists and add the smallest to merged list
    while left_index < len(left) and right_index < len(right):
        # For stability, use <= to maintain order of equal elements
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    if left_index < len(left):
        merged.extend(left[left_index:])
    if right_index < len(right):
        merged.extend(right[right_index:])

    return merged
```

**Explanation:**

- **`merge_sort` Function:**
  - Checks if the array length is less than or equal to 1 (base case).
  - Divides the array into two halves.
  - Recursively sorts each half.
  - Merges the sorted halves.

- **`merge` Function:**
  - Merges two sorted lists into one sorted list.
  - Uses two indices to track the current position in each list.
  - Compares elements and merges them while maintaining stability.

---

## **2. Demonstrating the Characteristics**

### **A. Stability**

Merge Sort is a stable sorting algorithm. To demonstrate stability, we'll sort a list of tuples where the first element is the key for sorting, and the second element distinguishes the original order.

```python
# Sample data to demonstrate stability
data = [
    (3, 'a'),
    (1, 'b'),
    (2, 'c'),
    (3, 'd'),
    (2, 'e'),
    (1, 'f'),
]

def merge_sort_stable(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort_stable(left)
    right_sorted = merge_sort_stable(right)

    return merge_stable(left_sorted, right_sorted)

def merge_stable(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements and maintain stability
    while left_index < len(left) and right_index < len(right):
        if left[left_index][0] <= right[right_index][0]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Sorting the data
sorted_data = merge_sort_stable(data)

# Printing the sorted data
for item in sorted_data:
    print(item)
```

**Output:**

```
(1, 'b')
(1, 'f')
(2, 'c')
(2, 'e')
(3, 'a')
(3, 'd')
```

**Explanation:**

- The tuples are sorted based on the first element.
- When the first elements are equal, the original order is preserved (e.g., `(1, 'b')` comes before `(1, 'f')`).

### **B. Divide and Conquer**

To visualize the divide and conquer strategy, we can add print statements to show how the array is split and merged.

```python
def merge_sort_trace(arr, depth=0):
    indent = '  ' * depth
    print(f"{indent}merge_sort({arr})")
    if len(arr) <= 1:
        print(f"{indent}Returning {arr}")
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort_trace(left, depth + 1)
    right_sorted = merge_sort_trace(right, depth + 1)

    merged = merge_trace(left_sorted, right_sorted, depth + 1)
    print(f"{indent}Merged {left_sorted} and {right_sorted} into {merged}")
    return merged

def merge_trace(left, right, depth):
    indent = '  ' * depth
    print(f"{indent}Merging {left} and {right}")
    merged = []
    left_index = 0
    right_index = 0

    # Same merge logic as before
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    print(f"{indent}Result of merge: {merged}")
    return merged

# Sample array
array_to_sort = [38, 27, 43, 3, 9, 82, 10]

# Perform merge sort with tracing
sorted_array = merge_sort_trace(array_to_sort)
```

**Sample Output:**

```
merge_sort([38, 27, 43, 3, 9, 82, 10])
  merge_sort([38, 27, 43])
    merge_sort([38])
    Returning [38]
    merge_sort([27, 43])
      merge_sort([27])
      Returning [27]
      merge_sort([43])
      Returning [43]
      Merging [27] and [43]
      Result of merge: [27, 43]
    Merged [27] and [43] into [27, 43]
    Merging [38] and [27, 43]
    Result of merge: [27, 38, 43]
  Merged [38] and [27, 43] into [27, 38, 43]
  merge_sort([3, 9, 82, 10])
    merge_sort([3, 9])
      merge_sort([3])
      Returning [3]
      merge_sort([9])
      Returning [9]
      Merging [3] and [9]
      Result of merge: [3, 9]
    Merged [3] and [9] into [3, 9]
    merge_sort([82, 10])
      merge_sort([82])
      Returning [82]
      merge_sort([10])
      Returning [10]
      Merging [82] and [10]
      Result of merge: [10, 82]
    Merged [82] and [10] into [10, 82]
    Merging [3, 9] and [10, 82]
    Result of merge: [3, 9, 10, 82]
  Merged [3, 9] and [10, 82] into [3, 9, 10, 82]
  Merging [27, 38, 43] and [3, 9, 10, 82]
  Result of merge: [3, 9, 10, 27, 38, 43, 82]
Merged [27, 38, 43] and [3, 9, 10, 82] into [3, 9, 10, 27, 38, 43, 82]
```

**Explanation:**

- Each call to `merge_sort_trace` prints the current subarray being sorted.
- The indentation reflects the depth of recursion.
- You can see how the array is divided down to single elements and then merged back up.

### **C. Time Complexity Measurement**

We can measure the execution time for arrays of different sizes to observe the **O(n log n)** time complexity.

```python
import time
import random
import matplotlib.pyplot as plt  # Ensure matplotlib is installed
import sys
sys.setrecursionlimit(10000)  # Increase recursion limit if necessary

def time_merge_sort():
    sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
    times = []

    for n in sizes:
        arr = [random.randint(1, 10000) for _ in range(n)]
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        print(f"Size: {n}, Time: {elapsed_time:.6f} seconds")

    # Plotting the results
    plt.plot(sizes, times, marker='o')
    plt.title('Merge Sort Execution Time')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

# Run the timing function
time_merge_sort()
```

**Explanation:**

- We generate random arrays of different sizes.
- We record the time taken to sort each array using `merge_sort`.
- We plot the input sizes against the execution times to visualize the time complexity.

**Note:** The execution times should increase roughly in proportion to \( n \log n \).

### **D. Space Complexity**

Merge Sort requires additional space proportional to the input size. To demonstrate space usage, we can track the maximum memory used during execution.

However, measuring actual memory usage programmatically requires profiling tools or additional packages (e.g., `memory_profiler`). For simplicity, we can explain that the algorithm requires \( O(n) \) space due to:

- Temporary arrays created during merging.
- Call stack usage due to recursion (depth of \( \log n \)).

### **E. Recursive Nature**

The implementation already demonstrates recursion. The depth of recursive calls will be approximately \( \log n \). You can observe the recursive calls in the output of `merge_sort_trace`.

---

## **3. How to Execute the Python Code**

To run the provided code and observe the characteristics:

### **Requirements:**

- **Python 3.x** installed on your system.
- **Matplotlib** library for plotting (install using `pip install matplotlib`).

### **Steps:**

1. **Copy the Code:**

   Copy the code snippets provided into a Python file, e.g., `merge_sort_demo.py`.

2. **Run Stability Demonstration:**

   To test stability, ensure you include the code under **A. Stability** and run the script:

   ```bash
   python merge_sort_demo.py
   ```

   - Observe the output to verify that equal elements retain their original order.

3. **Run Divide and Conquer Visualization:**

   Include the code under **B. Divide and Conquer** in your script.

   - Run the script and observe the printed steps showing how the array is divided and merged.

4. **Run Time Complexity Measurement:**

   Include the code under **C. Time Complexity Measurement**.

   - Execute the script.
   - A plot window will appear showing the execution time against input size.
   - Ensure `matplotlib` is installed.

   ```bash
   pip install matplotlib
   ```

5. **Adjust Recursion Limit (if necessary):**

   If you encounter a `RecursionError`, increase the recursion limit:

   ```python
   import sys
   sys.setrecursionlimit(10000)  # Adjust as needed
   ```

6. **Observe Space Complexity:**

   While we can't measure space complexity directly without extra tools, you can understand that the function creates new lists during execution. Reading the code and understanding the algorithm provides insights into space usage.

---

## **4. Advanced Demonstrations**

### **A. In-place Merge Sort**

Implementing an in-place merge sort reduces space complexity but increases algorithmic complexity.

```python
def merge_sort_in_place(arr, left=0, right=None):
    if right is None:
        right = len(arr)

    # Base case
    if right - left <= 1:
        return

    mid = (left + right) // 2

    merge_sort_in_place(arr, left, mid)
    merge_sort_in_place(arr, mid, right)

    merge_in_place(arr, left, mid, right)

def merge_in_place(arr, left, mid, right):
    # Temporary arrays are avoided; merging is done within the array
    left_index = left
    right_index = mid

    while left_index < right_index and right_index < right:
        if arr[left_index] <= arr[right_index]:
            left_index += 1
        else:
            # Rotate the element at right_index to the position at left_index
            value = arr[right_index]
            arr[left_index+1:right_index+1] = arr[left_index:right_index]
            arr[left_index] = value

            # Update indices
            left_index += 1
            right_index += 1

# Usage
arr_in_place = [5, 2, 4, 6, 1, 3]
merge_sort_in_place(arr_in_place)
print(arr_in_place)
```

**Explanation:**

- The in-place merge avoids using extra space but is more complex.
- This implementation is not stable.

### **B. Parallel Merge Sort**

Utilizing multiple processors to perform sorting in parallel.

```python
from multiprocessing import Pool

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide step
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Create a pool of workers
    with Pool(2) as pool:
        left_sorted, right_sorted = pool.map(merge_sort, [left, right])

    # Combine step
    return merge(left_sorted, right_sorted)

# Usage
if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = parallel_merge_sort(arr)
    print(sorted_arr)
```

**Explanation:**

- The `multiprocessing` module allows splitting the sorting across processes.
- Effective for large datasets on systems with multiple cores.

**Note:** Multiprocessing requires the `if __name__ == '__main__':` guard in Windows.

---

## **5. Conclusion**

By running the provided Python code, you can:

- **Observe Stability:** See how the algorithm maintains the order of equal elements.
- **Visualize Divide and Conquer:** Understand how the algorithm splits and merges data.
- **Measure Time Complexity:** Empirically confirm the \( O(n \log n) \) time complexity.
- **Understand Space Complexity:** Recognize the trade-offs between time and space.

**Key Takeaways:**

- **Merge Sort** is an efficient, comparison-based, and stable sorting algorithm.
- It uses the **divide and conquer** paradigm for sorting.
- It has a **time complexity** of \( O(n \log n) \) in all cases.
- The **space complexity** is \( O(n) \) due to the additional arrays used during merging.
- Understanding and implementing sorting algorithms enhances problem-solving skills and algorithmic knowledge in programming.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---