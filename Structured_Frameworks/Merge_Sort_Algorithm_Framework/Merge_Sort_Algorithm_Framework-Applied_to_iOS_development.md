---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---

# Merge Sort Algorithm Framework  - Applied to iOS development

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---

## **1. Sorting Large Datasets Efficiently**

When working with large datasets fetched from databases or APIs, you might need an efficient sorting algorithm that maintains stability (preserves the order of equal elements).

**Example: Sorting an Array of Custom Objects**

Suppose you have an array of `Person` objects that you want to sort based on their `lastName`.

```swift
import Foundation

struct Person {
    let firstName: String
    let lastName: String
}

// Sample data
let people = [
    Person(firstName: "John", lastName: "Smith"),
    Person(firstName: "Alice", lastName: "Johnson"),
    Person(firstName: "Bob", lastName: "Smith"),
    Person(firstName: "Carol", lastName: "Adams"),
]

// Merge Sort Implementation
func mergeSort(_ array: [Person]) -> [Person] {
    // Base case
    guard array.count > 1 else { return array }
    
    // Divide
    let middleIndex = array.count / 2
    let leftArray = Array(array[0..<middleIndex])
    let rightArray = Array(array[middleIndex...])
    
    // Conquer
    return merge(mergeSort(leftArray), mergeSort(rightArray))
}

func merge(_ left: [Person], _ right: [Person]) -> [Person] {
    var leftIndex = 0
    var rightIndex = 0
    
    var orderedArray: [Person] = []
    
    // Compare elements and merge
    while leftIndex < left.count && rightIndex < right.count {
        let leftPerson = left[leftIndex]
        let rightPerson = right[rightIndex]
        
        if leftPerson.lastName < rightPerson.lastName {
            orderedArray.append(leftPerson)
            leftIndex += 1
        } else if leftPerson.lastName > rightPerson.lastName {
            orderedArray.append(rightPerson)
            rightIndex += 1
        } else {
            // Last names are equal; maintain original order (stability)
            orderedArray.append(leftPerson)
            leftIndex += 1
        }
    }
    
    // Append remaining elements
    if leftIndex < left.count {
        orderedArray.append(contentsOf: left[leftIndex...])
    }
    if rightIndex < right.count {
        orderedArray.append(contentsOf: right[rightIndex...])
    }
    
    return orderedArray
}

// Usage
let sortedPeople = mergeSort(people)
for person in sortedPeople {
    print("\(person.firstName) \(person.lastName)")
}
```

**Output:**

```
Carol Adams
Alice Johnson
John Smith
Bob Smith
```

**Explanation:**

- The `mergeSort` function recursively divides the array and merges the sorted halves.
- The `merge` function compares `lastName` properties to order the `Person` objects.
- Stability ensures that `John Smith` comes before `Bob Smith` as in the original array.

---

## **2. Customizing Sorting Behavior**

You might need to sort based on multiple criteria or custom conditions that aren't directly supported by Swift's standard sorting methods.

**Example: Sorting by Multiple Properties**

Adjust the merge function to sort first by `lastName`, then by `firstName` if the last names are the same.

```swift
func merge(_ left: [Person], _ right: [Person]) -> [Person] {
    var leftIndex = 0
    var rightIndex = 0
    var orderedArray: [Person] = []
    
    while leftIndex < left.count && rightIndex < right.count {
        let leftPerson = left[leftIndex]
        let rightPerson = right[rightIndex]
        
        if leftPerson.lastName < rightPerson.lastName {
            orderedArray.append(leftPerson)
            leftIndex += 1
        } else if leftPerson.lastName > rightPerson.lastName {
            orderedArray.append(rightPerson)
            rightIndex += 1
        } else {
            // Last names are equal; compare first names
            if leftPerson.firstName <= rightPerson.firstName {
                orderedArray.append(leftPerson)
                leftIndex += 1
            } else {
                orderedArray.append(rightPerson)
                rightIndex += 1
            }
        }
    }
    
    // Append remaining elements
    if leftIndex < left.count {
        orderedArray.append(contentsOf: left[leftIndex...])
    }
    if rightIndex < right.count {
        orderedArray.append(contentsOf: right[rightIndex...])
    }
    
    return orderedArray
}

// Usage remains the same
let sortedPeople = mergeSort(people)
for person in sortedPeople {
    print("\(person.firstName) \(person.lastName)")
}
```

**Output:**

```
Carol Adams
Alice Johnson
Bob Smith
John Smith
```

**Explanation:**

- Now, if `lastName` is the same, the `firstName` is used to determine order.
- This customization is helpful when sorting on multiple attributes.

---

## **3. Educational Applications and Visualizations**

If you're developing educational apps or need to demonstrate sorting algorithms, implementing Merge Sort allows you to illustrate each step of the process.

**Example: Visualizing Merge Sort Steps**

```swift
func mergeSortWithLogging(_ array: [Int]) -> [Int] {
    guard array.count > 1 else { return array }
    
    let middleIndex = array.count / 2
    let leftArray = Array(array[0..<middleIndex])
    let rightArray = Array(array[middleIndex...])
    
    let leftSorted = mergeSortWithLogging(leftArray)
    let rightSorted = mergeSortWithLogging(rightArray)
    
    let merged = mergeWithLogging(leftSorted, rightSorted)
    print("Merging \(leftSorted) and \(rightSorted) into \(merged)")
    return merged
}

func mergeWithLogging(_ left: [Int], _ right: [Int]) -> [Int] {
    // Same as the standard merge function but may include logging
    // ...
}

// Usage
let numbers = [38, 27, 43, 3, 9, 82, 10]
let sortedNumbers = mergeSortWithLogging(numbers)
```

**Output:**

```
Merging [38] and [27] into [27, 38]
Merging [43] and [3] into [3, 43]
Merging [27, 38] and [3, 43] into [3, 27, 38, 43]
Merging [9] and [82] into [9, 82]
Merging [9, 82] and [10] into [9, 10, 82]
Merging [3, 27, 38, 43] and [9, 10, 82] into [3, 9, 10, 27, 38, 43, 82]
```

**Explanation:**

- The functions print each merging step.
- This is useful for visualization in educational apps or for debugging.

---

## **4. Sorting Data in Custom Data Structures**

When you have custom data structures (e.g., linked lists, trees), you may need to implement your own sorting algorithms.

**Example: Sorting a Linked List**

Swift's `Array` type benefits from built-in sorting, but linked lists don't. Implementing Merge Sort for a linked list:

```swift
class ListNode {
    var value: Int
    var next: ListNode?
    
    init(_ value: Int) {
        self.value = value
        self.next = nil
    }
}

// Merge Sort for Linked Lists
func sortList(_ head: ListNode?) -> ListNode? {
    guard head != nil && head?.next != nil else { return head }
    
    // Split the list
    let middle = getMiddle(head)
    let nextToMiddle = middle?.next
    middle?.next = nil
    
    let left = sortList(head)
    let right = sortList(nextToMiddle)
    
    return sortedMerge(left, right)
}

func getMiddle(_ head: ListNode?) -> ListNode? {
    var slow = head
    var fast = head?.next
    while fast != nil {
        fast = fast?.next
        if fast != nil {
            slow = slow?.next
            fast = fast?.next
        }
    }
    return slow
}

func sortedMerge(_ a: ListNode?, _ b: ListNode?) -> ListNode? {
    if a == nil { return b }
    if b == nil { return a }
    
    var result: ListNode?
    
    if a!.value <= b!.value {
        result = a
        result?.next = sortedMerge(a?.next, b)
    } else {
        result = b
        result?.next = sortedMerge(a, b?.next)
    }
    return result
}

// Usage
let node1 = ListNode(4)
node1.next = ListNode(2)
node1.next?.next = ListNode(1)
node1.next?.next?.next = ListNode(3)

if let sortedHead = sortList(node1) {
    var currentNode: ListNode? = sortedHead
    while currentNode != nil {
        print(currentNode!.value)
        currentNode = currentNode?.next
    }
}
```

**Output:**

```
1
2
3
4
```

**Explanation:**

- Merge Sort is suitable for linked lists because it doesn't require random access.
- The space complexity is optimized since we rearrange existing nodes.

---

## **5. Implementing Background Sorting with Multithreading**

For performance optimization, you might want to perform sorting in the background to keep the UI responsive.

**Example: Sorting in a Background Thread**

```swift
let largeDataSet = (1...1_000_000).map { _ in Int.random(in: 1...1_000_000) }

DispatchQueue.global(qos: .background).async {
    let sortedDataSet = mergeSort(largeDataSet)
    DispatchQueue.main.async {
        // Update the UI or use the sorted data
        print("Sorting completed")
    }
}
```

**Explanation:**

- The sorting task is dispatched to a background queue.
- Upon completion, updates are made on the main queue to avoid UI glitches.
- Implementing your own `mergeSort` allows for custom optimizations or logging.

---

## **6. Sorting Immutable Data Structures**

In functional programming or when working with immutable data, you need to return new sorted arrays without mutating the original data.

**Example: Sorting Without Mutation**

```swift
func immutableMergeSort(_ array: [Int]) -> [Int] {
    guard array.count > 1 else { return array }
    // Same as standard merge sort; arrays in Swift are value types
}

// Usage
let originalArray = [5, 2, 9, 1, 5, 6]
let sortedArray = immutableMergeSort(originalArray)

print("Original Array: \(originalArray)")
print("Sorted Array: \(sortedArray)")
```

**Output:**

```
Original Array: [5, 2, 9, 1, 5, 6]
Sorted Array: [1, 2, 5, 5, 6, 9]
```

**Explanation:**

- The original array remains unchanged.
- This is essential when the data should not be modified, such as in Redux-like state management.

---

## **7. Implementing Custom Collections**

If you have custom collection types, you may need to implement sorting methods that are optimized for them.

**Example: Sorting a Custom Collection**

```swift
struct CustomCollection<Element> {
    private var elements: [Element]
    
    // Initializers and other methods...
}

extension CustomCollection where Element: Comparable {
    func mergeSort() -> CustomCollection {
        // Implement Merge Sort tailored to CustomCollection
        // For example, sorting `elements` array internally
    }
}

// Usage
var customCollection = CustomCollection(elements: [5, 2, 9, 1, 5, 6])
let sortedCollection = customCollection.mergeSort()
```

**Explanation:**

- By implementing `mergeSort` within your custom collection, you provide an optimized sorting mechanism.
- This can be particularly useful if the data structure requires special handling during sorting.

---

## **8. Handling Sorting in Performance-Critical Applications**

In applications where you need to ensure consistent performance regardless of input (e.g., time-sensitive applications), Merge Sort’s predictable time complexity can be beneficial.

**Example: Real-Time Data Sorting**

```swift
// Suppose you have a real-time data application
func sortRealTimeData(_ data: [DataPoint]) -> [DataPoint] {
    // Implement Merge Sort to guarantee O(n log n) performance
    return mergeSort(data)
}
```

**Explanation:**

- Since Merge Sort has a worst-case time complexity of O(n log n), it ensures consistent performance.
- This consistency is crucial in real-time applications where delays must be minimized.

---

## **Additional Notes**

- **Swift's Built-in Sorting Methods:** Swift's standard library provides efficient and optimized sorting methods like `sorted()` and `sort()`, which should be preferred for most use cases.

  ```swift
  let sortedPeople = people.sorted { $0.lastName < $1.lastName }
  ```

- **Educational Value:** Implementing Merge Sort helps in understanding the fundamentals of algorithms, which can improve problem-solving skills in development.

- **Customization and Control:** Writing your own sorting function allows you to tailor the algorithm to specific needs, such as logging, custom comparison logic, or working with unconventional data structures.

---

## **Conclusion**

Applying Merge Sort in iOS development is useful when you:

- **Need a Stable Sort:** Merge Sort maintains the relative order of equal elements, which is important in certain applications.

- **Work with Custom Data Structures:** When standard sorting methods are not applicable, such as with linked lists or custom collections.

- **Require Consistent Performance:** Merge Sort guarantees O(n log n) time complexity in all cases.

- **Want to Educate or Visualize Algorithms:** Implementing the algorithm from scratch is valuable for educational tools or visualizations.

- **Need Custom Sorting Logic:** When sorting criteria are complex or involve multiple properties.

**Remember:** For production code, use Swift's built-in sorting functions unless you have a specific reason not to. They are highly optimized and cover most sorting needs.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---