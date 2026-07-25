# Traversal

Traversal is one of the most basic and essential techniques in Arrays and Strings. It involves visiting each element exactly once (or in a specific order) to process, search, modify, or collect information.

Almost every array or string problem begins with traversal.

---

## 📌 When to Use Traversal

Use traversal when a problem asks you to:

- Search for an element
- Find maximum or minimum
- Calculate sum or average
- Count occurrences
- Modify elements
- Validate a condition
- Compare arrays or strings
- Build a new array or string
- Process each element exactly once

---

## 💡 Core Idea

Visit every element one by one and perform the required operation.

Instead of repeatedly accessing elements randomly, process them sequentially.

---

## ⏱️ Time Complexity

| Traversal Type | Complexity |
|---------------|------------|
| Single Traversal | **O(n)** |
| Reverse Traversal | **O(n)** |
| Two Independent Traversals | **O(n)** |
| Nested Traversal | **O(n²)** |

Space Complexity: **O(1)** (if no extra data structure is used)

---

# Python Templates

### Traverse an Array

```python
for num in nums:
    print(num)
```

---

### Traverse Using Index

```python
for i in range(len(nums)):
    print(nums[i])
```

---

### Reverse Traversal

```python
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
```

---

### Traverse a String

```python
for ch in s:
    print(ch)
```

---

### Traverse with Index and Value

```python
for i, num in enumerate(nums):
    print(i, num)
```

---

## Common Operations

### Find Maximum

```python
maximum = nums[0]

for num in nums:
    maximum = max(maximum, num)
```

---

### Find Minimum

```python
minimum = nums[0]

for num in nums:
    minimum = min(minimum, num)
```

---

### Calculate Sum

```python
total = 0

for num in nums:
    total += num
```

---

### Count Occurrences

```python
count = 0

for num in nums:
    if num == target:
        count += 1
```

---

### Find First Occurrence

```python
for i, num in enumerate(nums):
    if num == target:
        print(i)
        break
```

---

### Modify Elements

```python
for i in range(len(nums)):
    nums[i] *= 2
```

---

### Build a New Array

```python
result = []

for num in nums:
    result.append(num * 2)
```

---

## Common Patterns

### Pattern 1: Simple Traversal

```python
for num in nums:
    # Process num
```

---

### Pattern 2: Index-Based Traversal

```python
for i in range(len(nums)):
    # Use nums[i]
```

---

### Pattern 3: Reverse Traversal

```python
for i in range(len(nums) - 1, -1, -1):
    # Process from end
```

---

### Pattern 4: Simultaneous Index and Value

```python
for i, num in enumerate(nums):
    # Use both index and value
```

---

### Pattern 5: Conditional Traversal

```python
for num in nums:
    if condition(num):
        # Perform action
```

---

## Problems to Practice

### Easy

- ✅ Linear Search
- ✅ Find Maximum Number
- ✅ Find Minimum Number
- ✅ Remove Element
- ✅ Remove Duplicates from Sorted Array
- ✅ Find Numbers with Even Number of Digits
- ✅ Richest Customer Wealth
- ✅ Running Sum of 1D Array
- ✅ Shuffle the Array
- ✅ Kids With the Greatest Number of Candies

---

### Medium

- ✅ Product of Array Except Self
- ✅ Rotate Array
- ✅ Spiral Matrix
- ✅ Diagonal Traverse
- ✅ Set Matrix Zeroes
- ✅ Sort Colors
- ✅ Merge Intervals
- ✅ Game of Life

---

## Tips

- Traversal is the foundation of almost every array and string algorithm.
- Choose **value-based traversal** when you only need elements.
- Choose **index-based traversal** when you need to modify elements or access neighbors.
- Use **reverse traversal** when deleting elements or processing from the end.
- Avoid nested loops unless the problem genuinely requires comparing every pair.

---

# Cheat Sheet

```python
# Value traversal
for num in nums:
    ...

# Index traversal
for i in range(len(nums)):
    ...

# Reverse traversal
for i in range(len(nums) - 1, -1, -1):
    ...

# Index and value
for i, num in enumerate(nums):
    ...

# Traverse string
for ch in s:
    ...

# Sum
total += num

# Maximum
maximum = max(maximum, num)

# Minimum
minimum = min(minimum, num)
```

---

## Key Takeaway

> **Traversal is the process of visiting each element in an array or string to perform operations efficiently.**
>
> Whenever you need to **search**, **count**, **update**, **compare**, or **process every element**, traversal is usually the first technique to consider.
