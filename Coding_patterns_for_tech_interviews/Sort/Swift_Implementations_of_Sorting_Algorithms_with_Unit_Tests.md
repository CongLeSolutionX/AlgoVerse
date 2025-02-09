---
created: 2025-01-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
---



# Swift Implementations of Sorting Algorithms with Unit Tests


Below are Swift implementations for various sorting algorithms, following current best practices. Each algorithm includes edge case handling and accompanying unit tests using Swift's `XCTest` framework.

---

## 1. Insertion Sort

**Description:**

Insertion Sort builds the final sorted array one item at a time. It is efficient for small data sets. The algorithm iterates over the input array and inserts each element into its proper place in the sorted portion.

**Implementation:**

```swift
func insertionSort<T: Comparable>(_ array: [T]) -> [T] {
    // Edge case: Empty or single-element array
    guard array.count > 1 else { return array }
    
    var result = array
    for i in 1..<result.count {
        let key = result[i]
        var j = i - 1
        
        // Move elements greater than key to one position ahead
        while j >= 0 && result[j] > key {
            result[j + 1] = result[j]
            j -= 1
        }
        result[j + 1] = key
    }
    return result
}
```

**Edge Case Handling:**

- **Empty Arrays:** Returns the empty array without modification.
- **Single-Element Arrays:** Returns the array as it is already sorted.
- **Arrays with Duplicate Elements:** Correctly sorts while maintaining stability.

**Unit Tests:**

```swift
import XCTest

class InsertionSortTests: XCTestCase {
    func testInsertionSort_withIntegers() {
        XCTAssertEqual(insertionSort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        XCTAssertEqual(insertionSort([Int]()), [])
        XCTAssertEqual(insertionSort([42]), [42])
        XCTAssertEqual(insertionSort([3, -1, 0, -1, 2]), [-1, -1, 0, 2, 3])
    }
    
    func testInsertionSort_withStrings() {
        XCTAssertEqual(insertionSort(["banana", "apple", "cherry"]), ["apple", "banana", "cherry"])
    }
    
    func testInsertionSort_withAlreadySortedArray() {
        XCTAssertEqual(insertionSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    }
}
```

---

## 2. Selection Sort

**Description:**

Selection Sort repeatedly finds the minimum element from the unsorted portion and moves it to the sorted portion.

**Implementation:**

```swift
func selectionSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }
    
    var result = array
    for i in 0..<result.count - 1 {
        var minIndex = i
        for j in i + 1..<result.count {
            if result[j] < result[minIndex] {
                minIndex = j
            }
        }
        if minIndex != i {
            result.swapAt(i, minIndex)
        }
    }
    return result
}
```

**Edge Case Handling:**

- **Empty Arrays:** Returns the empty array.
- **Single-Element Arrays:** Returns the array as is.
- **Unsorted Arrays:** Properly sorts any unsorted array.

**Unit Tests:**

```swift
class SelectionSortTests: XCTestCase {
    func testSelectionSort_withIntegers() {
        XCTAssertEqual(selectionSort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])
        XCTAssertEqual(selectionSort([-3, -1, -2]), [-3, -2, -1])
        XCTAssertEqual(selectionSort([Int]()), [])
    }
    
    func testSelectionSort_withStrings() {
        XCTAssertEqual(selectionSort(["delta", "alpha", "charlie", "bravo"]),
                       ["alpha", "bravo", "charlie", "delta"])
    }

    func testSelectionSort_withAlreadySortedArray() {
        XCTAssertEqual(selectionSort([1, 2, 3, 4]), [1, 2, 3, 4])
    }
}
```

---

## 3. Bubble Sort

**Description:**

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.

**Implementation:**

```swift
func bubbleSort<T: Comparable>(_ array: [T]) -> [T] {
    var result = array
    let n = result.count
    guard n > 1 else { return result }

    for i in 0..<n {
        var swapped = false
        for j in 0..<(n - i - 1) {
            if result[j] > result[j + 1] {
                result.swapAt(j, j + 1)
                swapped = true
            }
        }
        if !swapped {
            break
        }
    }
    return result
}
```

**Edge Case Handling:**

- **Optimized:** Stops if no swaps occur in a pass (already sorted).
- **Handles Duplicates:** Maintains the order of duplicates (stable).

**Unit Tests:**

```swift
class BubbleSortTests: XCTestCase {
    func testBubbleSort_withIntegers() {
        XCTAssertEqual(bubbleSort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
        XCTAssertEqual(bubbleSort([Int]()), [])
        XCTAssertEqual(bubbleSort([42]), [42])
    }
    
    func testBubbleSort_withDuplicates() {
        XCTAssertEqual(bubbleSort([3, 2, 1, 2, 3]), [1, 2, 2, 3, 3])
    }

    func testBubbleSort_withAlreadySortedArray() {
        XCTAssertEqual(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    }
}
```

---

## 4. Merge Sort

**Description:**

Merge Sort divides the array into halves, sorts them recursively, and then merges the sorted halves.

**Implementation:**

```swift
func mergeSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }
    
    let middle = array.count / 2
    let left = mergeSort(Array(array[0..<middle]))
    let right = mergeSort(Array(array[middle..<array.count]))
    
    return merge(left, right)
}

func merge<T: Comparable>(_ left: [T], _ right: [T]) -> [T] {
    var leftIndex = 0, rightIndex = 0
    var ordered = [T]()
    
    while leftIndex < left.count && rightIndex < right.count {
        if left[leftIndex] <= right[rightIndex] {
            ordered.append(left[leftIndex])
            leftIndex += 1
        } else {
            ordered.append(right[rightIndex])
            rightIndex += 1
        }
    }
    
    // Append remaining elements
    if leftIndex < left.count {
        ordered.append(contentsOf: left[leftIndex...])
    }
    if rightIndex < right.count {
        ordered.append(contentsOf: right[rightIndex...])
    }
    
    return ordered
}
```

**Edge Case Handling:**

- **Recursive Base Case:** Handles arrays with less than two elements.
- **Stable Sorting:** Equal elements maintain their original order.

**Unit Tests:**

```swift
class MergeSortTests: XCTestCase {
    func testMergeSort_withIntegers() {
        XCTAssertEqual(mergeSort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])
        XCTAssertEqual(mergeSort([Int]()), [])
        XCTAssertEqual(mergeSort([42]), [42])
    }
    
    func testMergeSort_withStrings() {
        XCTAssertEqual(mergeSort(["banana", "apple", "cherry", "date"]),
                       ["apple", "banana", "cherry", "date"])
    }

    func testMergeSort_withAlreadySortedArray() {
        XCTAssertEqual(mergeSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    }
}
```

---

## 5. Quick Sort

**Description:**

Quick Sort selects a pivot and partitions the array into elements less than and greater than the pivot, sorting them recursively.

**Implementation:**

```swift
func quickSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }

    let pivot = array[array.count / 2]
    let less = array.filter { $0 < pivot }
    let equal = array.filter { $0 == pivot }
    let greater = array.filter { $0 > pivot }

    return quickSort(less) + equal + quickSort(greater)
}
```

**Edge Case Handling:**

- **Handles Duplicates:** Correctly sorts arrays with duplicate elements.
- **Functional Approach:** Uses filter for clarity.

**Unit Tests:**

```swift
class QuickSortTests: XCTestCase {
    func testQuickSort_withIntegers() {
        XCTAssertEqual(quickSort([10, 7, 8, 9, 1, 5]), [1, 5, 7, 8, 9, 10])
        XCTAssertEqual(quickSort([Int]()), [])
        XCTAssertEqual(quickSort([42]), [42])
    }
    
    func testQuickSort_withDuplicates() {
        XCTAssertEqual(quickSort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
    }

    func testQuickSort_withAlreadySortedArray() {
        XCTAssertEqual(quickSort([1, 2, 3]), [1, 2, 3])
    }
}
```

---

## 6. Heap Sort

**Description:**

Heap Sort leverages a binary heap data structure to sort an array.

**Implementation:**

```swift
func heapSort<T: Comparable>(_ array: [T]) -> [T] {
    var result = array
    let count = result.count
    
    // Build max heap
    for i in stride(from: count / 2 - 1, through: 0, by: -1) {
        heapify(&result, count, i)
    }
    
    // Extract elements from heap
    for i in stride(from: count - 1, through: 0, by: -1) {
        result.swapAt(0, i)
        heapify(&result, i, 0)
    }
    return result
}

private func heapify<T: Comparable>(_ array: inout [T], _ size: Int, _ root: Int) {
    var largest = root
    let left = 2 * root + 1
    let right = 2 * root + 2
    
    if left < size && array[left] > array[largest] {
        largest = left
    }
    
    if right < size && array[right] > array[largest] {
        largest = right
    }
    
    if largest != root {
        array.swapAt(root, largest)
        heapify(&array, size, largest)
    }
}
```

**Edge Case Handling:**

- **Encapsulation:** Uses a private `heapify` function.
- **Handles Empty and Single-Element Arrays:** Returns the array as is.

**Unit Tests:**

```swift
class HeapSortTests: XCTestCase {
    func testHeapSort_withIntegers() {
        XCTAssertEqual(heapSort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])
        XCTAssertEqual(heapSort([Int]()), [])
        XCTAssertEqual(heapSort([42]), [42])
    }
    
    func testHeapSort_withStrings() {
        XCTAssertEqual(heapSort(["delta", "alpha", "charlie", "bravo"]),
                       ["alpha", "bravo", "charlie", "delta"])
    }

    func testHeapSort_withAlreadySortedArray() {
        XCTAssertEqual(heapSort([1, 2, 3, 4]), [1, 2, 3, 4])
    }
}
```

---

## 7. Radix Sort

**Description:**

Radix Sort sorts numbers by processing individual digits. It requires linear auxiliary space.

**Implementation:**

```swift
func radixSort(_ array: [Int]) -> [Int] {
    guard array.count > 0 else { return array }

    var result = array
    let maxNumber = result.max() ?? 0
    var digitPlace = 1

    while maxNumber / digitPlace > 0 {
        result = countingSortForRadix(result, digitPlace)
        digitPlace *= 10
    }
    return result
}

private func countingSortForRadix(_ array: [Int], _ digitPlace: Int) -> [Int] {
    let base = 10
    var count = [Int](repeating: 0, count: base)
    var output = [Int](repeating: 0, count: array.count)
    
    for number in array {
        let digit = (number / digitPlace) % base
        count[digit] += 1
    }
    
    for i in 1..<base {
        count[i] += count[i - 1]
    }
    
    for number in array.reversed() {
        let digit = (number / digitPlace) % base
        count[digit] -= 1
        output[count[digit]] = number
    }
    return output
}
```

**Edge Case Handling:**

- **Non-Negative Integers:** Works for positive integers. Negative number support requires modification.
- **Handles Empty Arrays:** Returns empty array.

**Unit Tests:**

```swift
class RadixSortTests: XCTestCase {
    func testRadixSort_withIntegers() {
        XCTAssertEqual(radixSort([170, 45, 75, 90, 802, 24, 2, 66]),
                       [2, 24, 45, 66, 75, 90, 170, 802])
        XCTAssertEqual(radixSort([Int]()), [])
        XCTAssertEqual(radixSort([42]), [42])
    }
    
    func testRadixSort_withZeros() {
        XCTAssertEqual(radixSort([0, 0, 0]), [0, 0, 0])
    }

    func testRadixSort_withAlreadySortedArray() {
        XCTAssertEqual(radixSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    }
}
```

---

## 8. Counting Sort

**Description:**

Counting Sort counts occurrences of each unique element in the array and calculates positions.

**Implementation:**

```swift
func countingSort(_ array: [Int]) -> [Int] {
    guard array.count > 0 else { return array }
    let maxValue = array.max() ?? 0
    let minValue = array.min() ?? 0
    let range = maxValue - minValue + 1
    
    var countArray = [Int](repeating: 0, count: range)
    var outputArray = [Int](repeating: 0, count: array.count)
    
    for number in array {
        countArray[number - minValue] += 1
    }
    
    for i in 1..<countArray.count {
        countArray[i] += countArray[i - 1]
    }
    
    for number in array.reversed() {
        countArray[number - minValue] -= 1
        outputArray[countArray[number - minValue]] = number
    }
    return outputArray
}
```

**Edge Case Handling:**

- **Supports Negative Numbers:** Adjusts index with `minValue`.
- **Handles Empty Arrays:** Returns empty array.

**Unit Tests:**

```swift
class CountingSortTests: XCTestCase {
    func testCountingSort_withIntegers() {
        XCTAssertEqual(countingSort([4, 2, 2, 8, 3, 3, 1]),
                       [1, 2, 2, 3, 3, 4, 8])
        XCTAssertEqual(countingSort([Int]()), [])
    }
    
    func testCountingSort_withNegativeIntegers() {
        XCTAssertEqual(countingSort([0, -5, 2, -1, 3, -2, 1]),
                       [-5, -2, -1, 0, 1, 2, 3])
    }

    func testCountingSort_withAlreadySortedArray() {
        XCTAssertEqual(countingSort([1, 2, 3]), [1, 2, 3])
    }
}
```

---

## 9. Bucket Sort

**Description:**

Bucket Sort divides elements into buckets and sorts each bucket individually.

**Implementation:**

```swift
func bucketSort(_ array: [Double]) -> [Double] {
    guard array.count > 0 else { return array }

    var buckets: [[Double]] = .init(repeating: [], count: array.count)

    for number in array {
        let index = Int(number * Double(array.count))
        buckets[index].append(number)
    }

    // Sorting each bucket using insertion sort
    for i in 0..<buckets.count {
        buckets[i] = insertionSort(buckets[i])
    }

    return buckets.flatMap { $0 }
}
```

**Edge Case Handling:**

- **Range Assumption:** Assumes input is in `[0, 1)`.
- **Handles Empty and Single-Element Arrays:** Returns the array as is.

**Unit Tests:**

```swift
class BucketSortTests: XCTestCase {
    func testBucketSort_withFloatingNumbers() {
        let array: [Double] = [0.78, 0.17, 0.39, 0.26,
                               0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
        let sortedArray = bucketSort(array)
        XCTAssertEqual(sortedArray, array.sorted())
    }
    
    func testBucketSort_withEmptyArray() {
        XCTAssertEqual(bucketSort([]), [])
    }

    func testBucketSort_withSingleElement() {
        XCTAssertEqual(bucketSort([0.42]), [0.42])
    }
}
```

---

## 10. Timsort

**Description:**

Timsort is a hybrid sorting algorithm combining Insertion Sort and Merge Sort.

**Implementation:**

```swift
func timSort<T: Comparable>(_ array: [T]) -> [T] {
    let minRun = calculateMinRun(n: array.count)
    var result = array
    var i = 0
    while i < result.count {
        let end = min(i + minRun, result.count)
        let range = i..<end
        let sortedRun = insertionSort(Array(result[range]))
        result.replaceSubrange(range, with: sortedRun)
        i += minRun
    }

    var size = minRun
    while size < result.count {
        var left = 0
        while left < result.count {
            let mid = left + size - 1
            let right = min((left + 2 * size - 1), result.count - 1)
            if mid < right {
                let merged = merge(
                    Array(result[left...mid]),
                    Array(result[(mid + 1)...right])
                )
                result.replaceSubrange(left...right, with: merged)
            }
            left += 2 * size
        }
        size *= 2
    }
    return result
}

private func calculateMinRun(n: Int) -> Int {
    var n = n
    var r = 0
    while n >= 64 {
        r |= n & 1
        n >>= 1
    }
    return n + r
}
```

**Edge Case Handling:**

- **Adaptable:** Efficient for partially sorted data.
- **Handles All Array Sizes:** Dynamic calculation of `minRun`.

**Unit Tests:**

```swift
class TimSortTests: XCTestCase {
    func testTimSort_withIntegers() {
        XCTAssertEqual(timSort([5, 21, 7, 23, 19]), [5, 7, 19, 21, 23])
        XCTAssertEqual(timSort([Int]()), [])
        XCTAssertEqual(timSort([42]), [42])
    }
    
    func testTimSort_withStrings() {
        XCTAssertEqual(timSort(["delta", "alpha", "charlie", "bravo"]),
                       ["alpha", "bravo", "charlie", "delta"])
    }

    func testTimSort_withAlreadySortedArray() {
        XCTAssertEqual(timSort([1, 2, 3, 4]), [1, 2, 3, 4])
    }
}
```

---

# Notes on Best Practices and Edge Cases

- **Generics and Protocols:** Used generics and constrained types to `Comparable` for flexibility.
- **Immutability:** Original arrays are not modified; functions return new sorted arrays.
- **Edge Cases:** All algorithms handle empty arrays and single-element arrays gracefully.
- **Stability:** Algorithms that are stable maintain the relative order of equal elements (e.g., Merge Sort, Insertion Sort).
- **Private Helpers:** Helper functions like `heapify` and `calculateMinRun` are marked `private` for encapsulation.

# How to Run Tests

To run the tests:

1. Open Xcode and create a new macOS or iOS project or a playground.
2. Add a new Swift file for the implementations.
3. Add a test target if not already present.
4. Add a new test case class for the unit tests and include the test methods.
5. Run the tests using `Product > Test` (⌘U).


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---