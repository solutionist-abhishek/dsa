# Frequency Counting

Frequency Counting is one of the most fundamental techniques used in Arrays and Strings. It helps you efficiently count how many times each element appears in a collection, often reducing brute-force `O(n²)` solutions to `O(n)`.

---

## 📌 When to Use Frequency Counting

Use this technique when a problem asks about:

- Counting occurrences of elements
- Detecting duplicates
- Finding unique elements
- Comparing two arrays or strings
- Anagrams
- Majority element
- Missing or extra elements
- Character frequency
- Pair counting based on frequency

---

## 💡 Core Idea

Store the frequency of each element in a hash map (dictionary).

Instead of searching repeatedly, count once and use the stored frequencies.

---

## ⏱️ Time Complexity

| Operation | Complexity |
|-----------|------------|
| Build Frequency Map | **O(n)** |
| Lookup Frequency | **O(1)** (average) |
| Overall | **O(n)** |

Space Complexity: **O(n)**

---

# Python Template

### Using Dictionary

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

---

### Using Counter

```python
from collections import Counter

freq = Counter(nums)
```

---

## Common Operations

### Count Frequency

```python
freq = Counter(nums)
print(freq[5])
```

---

### Check Duplicate

```python
if freq[x] > 1:
    print("Duplicate")
```

---

### Find Unique Elements

```python
for num, count in freq.items():
    if count == 1:
        print(num)
```

---

### Find Maximum Frequency

```python
max_freq = max(freq.values())
```

---

### Element with Maximum Frequency

```python
max_element = max(freq, key=freq.get)
```

---

### Remove an Element

```python
del freq[x]
```

---

### Sort by Frequency

```python
sorted(freq.items(), key=lambda x: x[1])
```

Descending

```python
sorted(freq.items(), key=lambda x: x[1], reverse=True)
```

---

## Common Patterns

### Pattern 1: Count Everything

```python
freq = Counter(nums)
```

---

### Pattern 2: Compare Frequencies

```python
Counter(s) == Counter(t)
```

Used in **Anagram** problems.

---

### Pattern 3: Build Frequency While Traversing

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

---

### Pattern 4: Decrease Frequency

```python
freq[x] -= 1

if freq[x] == 0:
    del freq[x]
```

Useful in sliding window problems.

---

## Problems to Practice

### Easy

- ✅ Contains Duplicate
- ✅ Valid Anagram
- ✅ Majority Element
- ✅ Single Number
- ✅ Find Lucky Integer in an Array
- ✅ Unique Number of Occurrences
- ✅ Find the Difference
- ✅ Ransom Note
- ✅ First Unique Character in a String

---

### Medium

- ✅ Top K Frequent Elements
- ✅ Sort Characters By Frequency
- ✅ Group Anagrams
- ✅ Find All Anagrams in a String
- ✅ Longest Palindrome
- ✅ Equal Row and Column Pairs
- ✅ Maximum Number of Balloons
- ✅ Hand of Straights

---

## Tips

- Prefer `collections.Counter` for cleaner code.
- Use a dictionary when custom updates are needed.
- Frequency counting often serves as the foundation for **Sliding Window** problems.
- Always check whether the problem involves counting, duplicates, or comparisons before considering nested loops.

---

# Cheat Sheet

```python
from collections import Counter

freq = Counter(nums)

freq[x]          # Frequency of x

freq.get(x, 0)   # Safe lookup

freq[x] += 1     # Increment

freq[x] -= 1     # Decrement

del freq[x]      # Delete key

max(freq.values())           # Maximum frequency

max(freq, key=freq.get)      # Element with maximum frequency

Counter(a) == Counter(b)     # Compare frequencies
```

---

## Key Takeaway

> **Frequency Counting transforms repeated searching into constant-time lookups using a hash map.**
>
> Whenever you see **count**, **duplicate**, **unique**, **anagram**, or **occurrence**, think **Frequency Counting** first.
