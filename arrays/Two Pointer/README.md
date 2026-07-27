# Two Pointers

The **Two Pointers** technique is a powerful algorithmic approach where two indices traverse a data structure (usually an array or string) to solve problems efficiently. It often reduces the time complexity from **O(n²)** to **O(n)**.

---

## 📌 When to Use Two Pointers

Use this technique when:

- The input array is sorted.
- You need to find pairs or triplets satisfying a condition.
- You need to compare elements from both ends.
- You need to remove duplicates or partition an array.
- You need to process a string from both directions.
- The problem involves merging or comparing two sequences.

---

## 🎯 Common Patterns

### 1. Opposite Direction Pointers
- One pointer starts from the beginning.
- The other starts from the end.
- Move pointers based on conditions.

**Examples**
- Two Sum II
- Container With Most Water
- Valid Palindrome
- 3Sum
- Trapping Rain Water

---

### 2. Same Direction Pointers
- Both pointers start from the beginning.
- One pointer usually explores ahead while the other maintains a valid position.

**Examples**
- Remove Duplicates from Sorted Array
- Remove Element
- Move Zeroes
- Merge Sorted Arrays

---

### 3. Fast & Slow Pointers
- One pointer moves faster than the other.
- Commonly used in linked lists but also applicable to arrays.

**Examples**
- Find Duplicate Number
- Cycle Detection
- Middle of Linked List

---

## 📝 General Template

### Opposite Direction

```cpp
int left = 0;
int right = n - 1;

while (left < right) {
    if (condition) {
        // Found answer
    } else if (needLargerValue) {
        left++;
    } else {
        right--;
    }
}
```

### Same Direction

```cpp
int left = 0;

for (int right = 0; right < n; right++) {

    // Process right pointer

    while (invalidCondition) {
        left++;
    }
}
```

---

## ⏱️ Complexity

| Operation | Complexity |
|-----------|------------|
| Time | O(n) |
| Space | O(1) |

Most two-pointer algorithms visit each element at most once.

---

# 📚 Problems Solved

| # | Problem | Difficulty |
|---|---------|------------|
| 1 | Two Sum II - Input Array Is Sorted | Easy |
| 2 | Valid Palindrome | Easy |
| 3 | Merge Strings Alternately | Easy |
| 4 | Merge Sorted Array | Easy |
| 5 | Remove Duplicates from Sorted Array | Easy |
| 6 | Remove Element | Easy |
| 7 | Move Zeroes | Easy |
| 8 | Container With Most Water | Medium |
| 9 | 3Sum | Medium |
| 10 | Trapping Rain Water | Hard |

> Update this table as you solve more problems.

---

# 💡 Tips

- Think about whether the array is **sorted**.
- Determine if moving one pointer can improve the answer.
- Avoid nested loops when two pointers can achieve the same result.
- Always verify the loop condition (`left < right` or `left <= right`).
- Be careful with duplicate values in pair/triplet problems.

---

## 🚀 Goal

Master the Two Pointers technique to efficiently solve array and string problems by reducing unnecessary comparisons and achieving optimal time complexity.
