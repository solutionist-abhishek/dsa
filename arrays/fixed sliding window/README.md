# Fixed Sliding Window

## 📌 What is Fixed Sliding Window?

The **Fixed Sliding Window** technique is used when you need to process **all contiguous subarrays (or substrings) of a fixed size `k`** efficiently.

Instead of recalculating the result for every window from scratch, we:
1. Build the first window.
2. Slide the window by one position.
3. Remove the outgoing element.
4. Add the incoming element.

This reduces the time complexity from **O(n × k)** to **O(n)**.

---

## 🧠 When to Use

Use this technique when:
- The window size is **fixed**.
- The problem asks for a contiguous subarray/substring of length `k`.
- You need maximum, minimum, sum, average, frequency, etc., over every window.

Common keywords:
- Size `k`
- Consecutive elements
- Contiguous subarray
- Contiguous substring

---

## ⚡ Pattern

```python
# Build first window
for i in range(k):
    # process nums[i]

# Slide the window
for right in range(k, len(nums)):
    # remove outgoing element
    # add incoming element
```

---

## 🎯 General Steps

1. Initialize the first window of size `k`.
2. Store its result.
3. Move the window one step at a time.
4. Remove the leftmost element.
5. Add the new rightmost element.
6. Update the answer.

---

## ⏱ Complexity

| Operation | Complexity |
|-----------|------------|
| Time | **O(n)** |
| Space | **O(1)** (excluding output) |

---

## 📝 Common Problems

### Easy
- Maximum Average Subarray I
- Maximum Sum Subarray of Size K
- Find All Anagrams in a String
- Sliding Window Maximum (using deque)

### Medium
- Defuse the Bomb
- Grumpy Bookstore Owner
- Number of Sub-arrays of Size K and Average ≥ Threshold

---

## 💡 Tips

- Always process the **first window separately**.
- Update the window by:
  - Removing the outgoing element.
  - Adding the incoming element.
- Be careful with window boundaries.
- If frequencies are involved, use a **HashMap** instead of recalculating.

---

## 🚫 Common Mistakes

- Forgetting to remove the outgoing element.
- Incorrect loop boundaries.
- Recomputing every window from scratch.
- Off-by-one indexing errors.

---

## 🧩 Template

```python
left = 0

# Build first window
window = 0
for right in range(k):
    window += nums[right]

ans = window

# Slide the window
for right in range(k, len(nums)):
    window -= nums[left]
    left += 1
    window += nums[right]
    ans = max(ans, window)

return ans
```

---

## 🔑 Key Takeaway

> **Fixed Sliding Window = Fixed-size contiguous window + Remove one element + Add one element while sliding.**

Think of it as maintaining information about a window instead of rebuilding it every time.
