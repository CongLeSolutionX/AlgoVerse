---
created: 2025-01-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
---



# Objective-C Implementations of Sorting Algorithms with Unit Tests

Below are Objective-C implementations for various sorting algorithms, following current best practices. Each algorithm includes edge case handling and accompanying unit tests using `XCTest` framework.

---

## 1. Insertion Sort

**Description:**

Insertion Sort builds the final sorted array one item at a time. It's efficient for small data sets. The algorithm iterates over the input array and inserts each element into its proper place in the sorted portion.

**Implementation:**

```objective-c
// InsertionSort.h

#import <Foundation/Foundation.h>

@interface InsertionSort : NSObject

+ (NSArray<NSNumber *> *)insertionSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// InsertionSort.m

#import "InsertionSort.h"

@implementation InsertionSort

+ (NSArray<NSNumber *> *)insertionSort:(NSArray<NSNumber *> *)array {
    // Edge case: Empty or single-element array
    if (array.count <= 1) {
        return array;
    }

    NSMutableArray<NSNumber *> *result = [array mutableCopy];
    for (NSInteger i = 1; i < result.count; i++) {
        NSNumber *key = result[i];
        NSInteger j = i - 1;

        // Move elements greater than key to one position ahead
        while (j >= 0 && [result[j] compare:key] == NSOrderedDescending) {
            result[j + 1] = result[j];
            j--;
        }
        result[j + 1] = key;
    }
    return [result copy];
}

@end
```

**Edge Case Handling:**

- **Empty Arrays:** Returns the empty array without modification.
- **Single-Element Arrays:** Returns the array as it is already sorted.
- **Arrays with Duplicate Elements:** Correctly sorts while maintaining stability.

**Unit Tests:**

```objective-c
// InsertionSortTests.m

#import <XCTest/XCTest.h>
#import "InsertionSort.h"

@interface InsertionSortTests : XCTestCase

@end

@implementation InsertionSortTests

- (void)testInsertionSort_withIntegers {
    NSArray<NSNumber *> *input = @[@5, @2, @9, @1, @5, @6];
    NSArray<NSNumber *> *expected = @[@1, @2, @5, @5, @6, @9];
    XCTAssertEqualObjects([InsertionSort insertionSort:input], expected);

    XCTAssertEqualObjects([InsertionSort insertionSort:@[]], @[]);

    XCTAssertEqualObjects([InsertionSort insertionSort:@[@42]], @[@42]);

    NSArray<NSNumber *> *inputWithDuplicates = @[@3, @-1, @0, @-1, @2];
    NSArray<NSNumber *> *expectedWithDuplicates = @[@-1, @-1, @0, @2, @3];
    XCTAssertEqualObjects([InsertionSort insertionSort:inputWithDuplicates], expectedWithDuplicates);
}

- (void)testInsertionSort_withStrings {
    NSArray<NSString *> *input = @[@"banana", @"apple", @"cherry"];
    NSArray<NSString *> *expected = @[@"apple", @"banana", @"cherry"];
    XCTAssertEqualObjects([InsertionSort insertionSort:input], expected);
}

- (void)testInsertionSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3, @4, @5];
    XCTAssertEqualObjects([InsertionSort insertionSort:input], input);
}

@end
```

---

## 2. Selection Sort

**Description:**

Selection Sort repeatedly finds the minimum element from the unsorted portion and moves it to the sorted portion.

**Implementation:**

```objective-c
// SelectionSort.h

#import <Foundation/Foundation.h>

@interface SelectionSort : NSObject

+ (NSArray<NSNumber *> *)selectionSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// SelectionSort.m

#import "SelectionSort.h"

@implementation SelectionSort

+ (NSArray<NSNumber *> *)selectionSort:(NSArray<NSNumber *> *)array {
    if (array.count <= 1) {
        return array;
    }

    NSMutableArray<NSNumber *> *result = [array mutableCopy];

    for (NSInteger i = 0; i < result.count - 1; i++) {
        NSInteger minIndex = i;
        for (NSInteger j = i + 1; j < result.count; j++) {
            if ([result[j] compare:result[minIndex]] == NSOrderedAscending) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            [result exchangeObjectAtIndex:i withObjectAtIndex:minIndex];
        }
    }
    return [result copy];
}

@end
```

**Edge Case Handling:**

- **Empty Arrays:** Returns the empty array.
- **Single-Element Arrays:** Returns the array as is.
- **Unsorted Arrays:** Properly sorts any unsorted array.

**Unit Tests:**

```objective-c
// SelectionSortTests.m

#import <XCTest/XCTest.h>
#import "SelectionSort.h"

@interface SelectionSortTests : XCTestCase

@end

@implementation SelectionSortTests

- (void)testSelectionSort_withIntegers {
    NSArray<NSNumber *> *input = @[@64, @25, @12, @22, @11];
    NSArray<NSNumber *> *expected = @[@11, @12, @22, @25, @64];
    XCTAssertEqualObjects([SelectionSort selectionSort:input], expected);

    NSArray<NSNumber *> *negativeInput = @[@-3, @-1, @-2];
    NSArray<NSNumber *> *negativeExpected = @[@-3, @-2, @-1];
    XCTAssertEqualObjects([SelectionSort selectionSort:negativeInput], negativeExpected);

    XCTAssertEqualObjects([SelectionSort selectionSort:@[]], @[]);
}

- (void)testSelectionSort_withStrings {
    NSArray<NSString *> *input = @[@"delta", @"alpha", @"charlie", @"bravo"];
    NSArray<NSString *> *expected = @[@"alpha", @"bravo", @"charlie", @"delta"];
    XCTAssertEqualObjects([SelectionSort selectionSort:input], expected);
}

- (void)testSelectionSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3, @4];
    XCTAssertEqualObjects([SelectionSort selectionSort:input], input);
}

@end
```

---

## 3. Bubble Sort

**Description:**

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.

**Implementation:**

```objective-c
// BubbleSort.h

#import <Foundation/Foundation.h>

@interface BubbleSort : NSObject

+ (NSArray<NSNumber *> *)bubbleSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// BubbleSort.m

#import "BubbleSort.h"

@implementation BubbleSort

+ (NSArray<NSNumber *> *)bubbleSort:(NSArray<NSNumber *> *)array {
    NSMutableArray<NSNumber *> *result = [array mutableCopy];
    NSInteger n = result.count;
    if (n <= 1) {
        return result;
    }

    BOOL swapped;
    do {
        swapped = NO;
        for (NSInteger i = 0; i < n - 1; i++) {
            if ([result[i] compare:result[i + 1]] == NSOrderedDescending) {
                [result exchangeObjectAtIndex:i withObjectAtIndex:i + 1];
                swapped = YES;
            }
        }
        n--;
    } while (swapped);
    return [result copy];
}

@end
```

**Edge Case Handling:**

- **Optimized:** Stops if no swaps occur in a pass (already sorted).
- **Handles Duplicates:** Maintains the order of duplicates (stable).

**Unit Tests:**

```objective-c
// BubbleSortTests.m

#import <XCTest/XCTest.h>
#import "BubbleSort.h"

@interface BubbleSortTests : XCTestCase

@end

@implementation BubbleSortTests

- (void)testBubbleSort_withIntegers {
    NSArray<NSNumber *> *input = @[@5, @1, @4, @2, @8];
    NSArray<NSNumber *> *expected = @[@1, @2, @4, @5, @8];
    XCTAssertEqualObjects([BubbleSort bubbleSort:input], expected);

    XCTAssertEqualObjects([BubbleSort bubbleSort:@[]], @[]);

    XCTAssertEqualObjects([BubbleSort bubbleSort:@[@42]], @[@42]);
}

- (void)testBubbleSort_withDuplicates {
    NSArray<NSNumber *> *input = @[@3, @2, @1, @2, @3];
    NSArray<NSNumber *> *expected = @[@1, @2, @2, @3, @3];
    XCTAssertEqualObjects([BubbleSort bubbleSort:input], expected);
}

- (void)testBubbleSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3, @4, @5];
    XCTAssertEqualObjects([BubbleSort bubbleSort:input], input);
}

@end
```

---

## 4. Merge Sort

**Description:**

Merge Sort divides the array into halves, sorts them recursively, and then merges the sorted halves.

**Implementation:**

```objective-c
// MergeSort.h

#import <Foundation/Foundation.h>

@interface MergeSort : NSObject

+ (NSArray<NSNumber *> *)mergeSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// MergeSort.m

#import "MergeSort.h"

@implementation MergeSort

+ (NSArray<NSNumber *> *)mergeSort:(NSArray<NSNumber *> *)array {
    if (array.count <= 1) {
        return array;
    }

    NSUInteger middle = array.count / 2;
    NSArray<NSNumber *> *left = [array subarrayWithRange:NSMakeRange(0, middle)];
    NSArray<NSNumber *> *right = [array subarrayWithRange:NSMakeRange(middle, array.count - middle)];

    return [self mergeLeft:[self mergeSort:left] right:[self mergeSort:right]];
}

+ (NSArray<NSNumber *> *)mergeLeft:(NSArray<NSNumber *> *)left right:(NSArray<NSNumber *> *)right {
    NSMutableArray<NSNumber *> *result = [NSMutableArray array];
    NSUInteger i = 0, j = 0;

    while (i < left.count && j < right.count) {
        if ([left[i] compare:right[j]] != NSOrderedDescending) {
            [result addObject:left[i]];
            i++;
        } else {
            [result addObject:right[j]];
            j++;
        }
    }

    while (i < left.count) {
        [result addObject:left[i]];
        i++;
    }

    while (j < right.count) {
        [result addObject:right[j]];
        j++;
    }

    return [result copy];
}

@end
```

**Edge Case Handling:**

- **Recursive Base Case:** Handles arrays with less than two elements.
- **Stable Sorting:** Equal elements maintain their original order.

**Unit Tests:**

```objective-c
// MergeSortTests.m

#import <XCTest/XCTest.h>
#import "MergeSort.h"

@interface MergeSortTests : XCTestCase

@end

@implementation MergeSortTests

- (void)testMergeSort_withIntegers {
    NSArray<NSNumber *> *input = @[@12, @11, @13, @5, @6, @7];
    NSArray<NSNumber *> *expected = @[@5, @6, @7, @11, @12, @13];
    XCTAssertEqualObjects([MergeSort mergeSort:input], expected);

    XCTAssertEqualObjects([MergeSort mergeSort:@[]], @[]);

    XCTAssertEqualObjects([MergeSort mergeSort:@[@42]], @[@42]);
}

- (void)testMergeSort_withStrings {
    NSArray<NSString *> *input = @[@"banana", @"apple", @"cherry", @"date"];
    NSArray<NSString *> *expected = @[@"apple", @"banana", @"cherry", @"date"];
    XCTAssertEqualObjects([MergeSort mergeSort:input], expected);
}

- (void)testMergeSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3, @4, @5];
    XCTAssertEqualObjects([MergeSort mergeSort:input], input);
}

@end
```

---

## 5. Quick Sort

**Description:**

Quick Sort selects a pivot and partitions the array into elements less than and greater than the pivot, sorting them recursively.

**Implementation:**

```objective-c
// QuickSort.h

#import <Foundation/Foundation.h>

@interface QuickSort : NSObject

+ (NSArray<NSNumber *> *)quickSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// QuickSort.m

#import "QuickSort.h"

@implementation QuickSort

+ (NSArray<NSNumber *> *)quickSort:(NSArray<NSNumber *> *)array {
    if (array.count <= 1) {
        return array;
    }

    NSNumber *pivot = array[array.count / 2];
    NSMutableArray<NSNumber *> *less = [NSMutableArray array];
    NSMutableArray<NSNumber *> *equal = [NSMutableArray array];
    NSMutableArray<NSNumber *> *greater = [NSMutableArray array];

    for (NSNumber *number in array) {
        NSComparisonResult result = [number compare:pivot];
        if (result == NSOrderedAscending) {
            [less addObject:number];
        } else if (result == NSOrderedSame) {
            [equal addObject:number];
        } else {
            [greater addObject:number];
        }
    }

    NSArray<NSNumber *> *sortedLess = [self quickSort:less];
    NSArray<NSNumber *> *sortedGreater = [self quickSort:greater];

    NSMutableArray<NSNumber *> *result = [NSMutableArray arrayWithArray:sortedLess];
    [result addObjectsFromArray:equal];
    [result addObjectsFromArray:sortedGreater];

    return [result copy];
}

@end
```

**Edge Case Handling:**

- **Handles Duplicates:** Correctly sorts arrays with duplicate elements.
- **Functional Approach:** Uses recursion and partitioning.

**Unit Tests:**

```objective-c
// QuickSortTests.m

#import <XCTest/XCTest.h>
#import "QuickSort.h"

@interface QuickSortTests : XCTestCase

@end

@implementation QuickSortTests

- (void)testQuickSort_withIntegers {
    NSArray<NSNumber *> *input = @[@10, @7, @8, @9, @1, @5];
    NSArray<NSNumber *> *expected = @[@1, @5, @7, @8, @9, @10];
    XCTAssertEqualObjects([QuickSort quickSort:input], expected);

    XCTAssertEqualObjects([QuickSort quickSort:@[]], @[]);

    XCTAssertEqualObjects([QuickSort quickSort:@[@42]], @[@42]);
}

- (void)testQuickSort_withDuplicates {
    NSArray<NSNumber *> *input = @[@3, @6, @8, @10, @1, @2, @1];
    NSArray<NSNumber *> *expected = @[@1, @1, @2, @3, @6, @8, @10];
    XCTAssertEqualObjects([QuickSort quickSort:input], expected);
}

- (void)testQuickSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3];
    XCTAssertEqualObjects([QuickSort quickSort:input], input);
}

@end
```

---

## 6. Heap Sort

**Description:**

Heap Sort leverages a binary heap data structure to sort an array.

**Implementation:**

```objective-c
// HeapSort.h

#import <Foundation/Foundation.h>

@interface HeapSort : NSObject

+ (NSArray<NSNumber *> *)heapSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// HeapSort.m

#import "HeapSort.h"

@implementation HeapSort

+ (NSArray<NSNumber *> *)heapSort:(NSArray<NSNumber *> *)array {
    NSMutableArray<NSNumber *> *result = [array mutableCopy];
    NSInteger count = result.count;

    // Build max heap
    for (NSInteger i = count / 2 - 1; i >= 0; i--) {
        [self heapifyArray:result size:count index:i];
    }

    // Extract elements from heap
    for (NSInteger i = count - 1; i >= 0; i--) {
        [result exchangeObjectAtIndex:0 withObjectAtIndex:i];
        [self heapifyArray:result size:i index:0];
    }
    return [result copy];
}

+ (void)heapifyArray:(NSMutableArray<NSNumber *> *)array size:(NSInteger)size index:(NSInteger)index {
    NSInteger largest = index;
    NSInteger left = 2 * index + 1;
    NSInteger right = 2 * index + 2;

    if (left < size && [array[left] compare:array[largest]] == NSOrderedDescending) {
        largest = left;
    }
    if (right < size && [array[right] compare:array[largest]] == NSOrderedDescending) {
        largest = right;
    }
    if (largest != index) {
        [array exchangeObjectAtIndex:index withObjectAtIndex:largest];
        [self heapifyArray:array size:size index:largest];
    }
}

@end
```

**Edge Case Handling:**

- **Encapsulation:** Uses a helper `heapifyArray` method.
- **Handles Empty and Single-Element Arrays:** Returns the array as is.

**Unit Tests:**

```objective-c
// HeapSortTests.m

#import <XCTest/XCTest.h>
#import "HeapSort.h"

@interface HeapSortTests : XCTestCase

@end

@implementation HeapSortTests

- (void)testHeapSort_withIntegers {
    NSArray<NSNumber *> *input = @[@12, @11, @13, @5, @6, @7];
    NSArray<NSNumber *> *expected = @[@5, @6, @7, @11, @12, @13];
    XCTAssertEqualObjects([HeapSort heapSort:input], expected);

    XCTAssertEqualObjects([HeapSort heapSort:@[]], @[]);

    XCTAssertEqualObjects([HeapSort heapSort:@[@42]], @[@42]);
}

- (void)testHeapSort_withStrings {
    NSArray<NSString *> *input = @[@"delta", @"alpha", @"charlie", @"bravo"];
    NSArray<NSString *> *expected = @[@"alpha", @"bravo", @"charlie", @"delta"];
    XCTAssertEqualObjects([HeapSort heapSort:input], expected);
}

- (void)testHeapSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3, @4];
    XCTAssertEqualObjects([HeapSort heapSort:input], input);
}

@end
```

---

## 7. Counting Sort

**Description:**

Counting Sort counts occurrences of each unique element in the array and calculates positions.

**Implementation:**

```objective-c
// CountingSort.h

#import <Foundation/Foundation.h>

@interface CountingSort : NSObject

+ (NSArray<NSNumber *> *)countingSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// CountingSort.m

#import "CountingSort.h"

@implementation CountingSort

+ (NSArray<NSNumber *> *)countingSort:(NSArray<NSNumber *> *)array {
    if (array.count == 0) {
        return array;
    }

    NSNumber *maxNumber = [array valueForKeyPath:@"@max.self"];
    NSNumber *minNumber = [array valueForKeyPath:@"@min.self"];
    NSInteger range = maxNumber.integerValue - minNumber.integerValue + 1;

    NSMutableArray<NSNumber *> *countArray = [NSMutableArray arrayWithCapacity:range];
    for (NSInteger i = 0; i < range; i++) {
        countArray[i] = @0;
    }

    // Count occurrences
    for (NSNumber *number in array) {
        NSInteger index = number.integerValue - minNumber.integerValue;
        countArray[index] = @([countArray[index] integerValue] + 1);
    }

    // Modify count array
    for (NSInteger i = 1; i < countArray.count; i++) {
        countArray[i] = @([countArray[i] integerValue] + [countArray[i - 1] integerValue]);
    }

    NSMutableArray<NSNumber *> *outputArray = [NSMutableArray arrayWithCapacity:array.count];
    for (NSInteger i = 0; i < array.count; i++) {
        outputArray[i] = @0;
    }

    // Build output array
    for (NSInteger i = array.count - 1; i >= 0; i--) {
        NSInteger index = [array[i] integerValue] - minNumber.integerValue;
        NSInteger position = [countArray[index] integerValue] - 1;
        outputArray[position] = array[i];
        countArray[index] = @([countArray[index] integerValue] - 1);
    }

    return [outputArray copy];
}

@end
```

**Edge Case Handling:**

- **Supports Negative Numbers:** Adjusts index with `minNumber`.
- **Handles Empty Arrays:** Returns empty array.

**Unit Tests:**

```objective-c
// CountingSortTests.m

#import <XCTest/XCTest.h>
#import "CountingSort.h"

@interface CountingSortTests : XCTestCase

@end

@implementation CountingSortTests

- (void)testCountingSort_withIntegers {
    NSArray<NSNumber *> *input = @[@4, @2, @2, @8, @3, @3, @1];
    NSArray<NSNumber *> *expected = @[@1, @2, @2, @3, @3, @4, @8];
    XCTAssertEqualObjects([CountingSort countingSort:input], expected);

    XCTAssertEqualObjects([CountingSort countingSort:@[]], @[]);
}

- (void)testCountingSort_withNegativeIntegers {
    NSArray<NSNumber *> *input = @[@0, @-5, @2, @-1, @3, @-2, @1];
    NSArray<NSNumber *> *expected = @[@-5, @-2, @-1, @0, @1, @2, @3];
    XCTAssertEqualObjects([CountingSort countingSort:input], expected);
}

- (void)testCountingSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3];
    XCTAssertEqualObjects([CountingSort countingSort:input], input);
}

@end
```

---

## 8. Radix Sort

**Note:**

Objective-C does not natively support generic typing similar to Swift's protocols. Radix Sort is complex in Objective-C for general-purpose use, especially with negative numbers. However, here's a simplified version assuming non-negative integers.

**Implementation:**

```objective-c
// RadixSort.h

#import <Foundation/Foundation.h>

@interface RadixSort : NSObject

+ (NSArray<NSNumber *> *)radixSort:(NSArray<NSNumber *> *)array;

@end
```

```objective-c
// RadixSort.m

#import "RadixSort.h"

@implementation RadixSort

+ (NSArray<NSNumber *> *)radixSort:(NSArray<NSNumber *> *)array {
    if (array.count == 0) {
        return array;
    }

    NSNumber *maxNumber = [array valueForKeyPath:@"@max.self"];
    NSInteger maxDigits = floor(log10(maxNumber.doubleValue)) + 1;

    NSMutableArray<NSNumber *> *result = [array mutableCopy];
    NSInteger placeValue = 1;

    for (NSInteger d = 0; d < maxDigits; d++) {
        result = [[self countingSortForRadix:result placeValue:placeValue] mutableCopy];
        placeValue *= 10;
    }
    return [result copy];
}

+ (NSArray<NSNumber *> *)countingSortForRadix:(NSArray<NSNumber *> *)array placeValue:(NSInteger)placeValue {
    NSInteger base = 10;
    NSMutableArray<NSNumber *> *countArray = [NSMutableArray arrayWithCapacity:base];
    for (NSInteger i = 0; i < base; i++) {
        countArray[i] = @0;
    }

    // Count occurrences
    for (NSNumber *number in array) {
        NSInteger digit = (number.integerValue / placeValue) % base;
        countArray[digit] = @([countArray[digit] integerValue] + 1);
    }

    // Modify count array
    for (NSInteger i = 1; i < base; i++) {
        countArray[i] = @([countArray[i] integerValue] + [countArray[i - 1] integerValue]);
    }

    NSMutableArray<NSNumber *> *outputArray = [NSMutableArray arrayWithCapacity:array.count];
    for (NSInteger i = 0; i < array.count; i++) {
        outputArray[i] = @0;
    }

    // Build output array
    for (NSInteger i = array.count - 1; i >= 0; i--) {
        NSInteger digit = (array[i].integerValue / placeValue) % base;
        NSInteger position = [countArray[digit] integerValue] - 1;
        outputArray[position] = array[i];
        countArray[digit] = @([countArray[digit] integerValue] - 1);
    }
    return [outputArray copy];
}

@end
```

**Edge Case Handling:**

- **Non-Negative Integers:** Works for positive integers. Negative number support requires significant modification.
- **Handles Empty Arrays:** Returns empty array.

**Unit Tests:**

```objective-c
// RadixSortTests.m

#import <XCTest/XCTest.h>
#import "RadixSort.h"

@interface RadixSortTests : XCTestCase

@end

@implementation RadixSortTests

- (void)testRadixSort_withIntegers {
    NSArray<NSNumber *> *input = @[@170, @45, @75, @90, @802, @24, @2, @66];
    NSArray<NSNumber *> *expected = @[@2, @24, @45, @66, @75, @90, @170, @802];
    XCTAssertEqualObjects([RadixSort radixSort:input], expected);

    XCTAssertEqualObjects([RadixSort radixSort:@[]], @[]);

    XCTAssertEqualObjects([RadixSort radixSort:@[@42]], @[@42]);
}

- (void)testRadixSort_withZeros {
    NSArray<NSNumber *> *input = @[@0, @0, @0];
    NSArray<NSNumber *> *expected = @[@0, @0, @0];
    XCTAssertEqualObjects([RadixSort radixSort:input], expected);
}

- (void)testRadixSort_withAlreadySortedArray {
    NSArray<NSNumber *> *input = @[@1, @2, @3, @4, @5];
    XCTAssertEqualObjects([RadixSort radixSort:input], input);
}

@end
```

---

## Notes on Best Practices and Edge Cases

- **Use of Foundation Collections:** Utilized `NSArray` and `NSMutableArray` for dynamic arrays.
- **Generics Limitation:** Objective-C doesn't support generics like Swift, so methods work with `NSNumber` or `NSString` where appropriate.
- **Immutability and Copying:** Methods return new sorted arrays to avoid side effects.
- **Edge Cases:** All algorithms handle empty arrays and single-element arrays gracefully.
- **Stability:** Stable algorithms maintain the relative order of equal elements (e.g., Merge Sort, Insertion Sort).
- **Helper Methods Encapsulation:** Helper methods like `heapifyArray` are encapsulated within the class implementation.

---

# How to Run Tests

To run the tests:

1. **Create an Xcode Project:**

   - Open Xcode and select **File > New > Project**.
   - Choose **macOS > Command Line Tool** or **iOS > Application** as appropriate.
   - Enable the checkbox **Include Unit Tests**.

2. **Add Sorting Classes:**

   - Add new Objective-C class files for each sorting algorithm (e.g., `InsertionSort.h` and `InsertionSort.m`).
   - Copy the implementation code into the corresponding files.

3. **Add Unit Test Classes:**

   - In the test target, add new test case files for each algorithm (e.g., `InsertionSortTests.m`).
   - Import the sorting class in each test file.
   - Copy the unit test code into the test files.

4. **Run Tests:**

   - Select the test scheme.
   - Run tests using **Product > Test** or press **⌘U**.

---


