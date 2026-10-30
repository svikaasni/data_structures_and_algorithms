# LeetCode DSA Practice – Python

A collection of LeetCode problems solved using Python, focusing on Bit Manipulation, Arrays, Dynamic Programming, and Backtracking.

---

## 📚 Problems Covered

| No. | LeetCode Problem | Problem No. | Difficulty | Topic |
|---|---|---:|---|---|
| 1 | Single Number | 136 | Easy | XOR |
| 2 | Missing Number | 268 | Easy | Math / XOR |
| 3 | Number of 1 Bits | 191 | Easy | Bit Manipulation |
| 4 | Counting Bits | 338 | Easy | Dynamic Programming |
| 5 | Subsets | 78 | Medium | Backtracking / Bit Manipulation |

---

# 1. Single Number

**LeetCode:** 136  
**Difficulty:** Easy

### Problem

Given a non-empty array of integers, every element appears twice except for one. Find that single number.

### Example

```python
Input: nums = [4, 1, 2, 1, 2]
Output: 4
```

### Optimized Python Solution – XOR

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
```

### Explanation

XOR properties:

- `a ^ a = 0`
- `a ^ 0 = a`
- `a ^ b = b ^ a`

Duplicate numbers cancel each other, leaving the unique number.

### Complexity

- Time: O(n)
- Space: O(1)

---

# 2. Missing Number

**LeetCode:** 268  
**Difficulty:** Easy

### Problem

Given an array containing `n` distinct numbers in the range `[0, n]`, find the missing number.

### Example

```python
Input: nums = [3, 0, 1]
Output: 2
```

### Approach 1 – Mathematical Formula

Formula:

`Expected Sum = n * (n + 1) // 2`

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual
```

### Approach 2 – XOR

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i, num in enumerate(nums):
            result ^= i ^ num

        return result
```

### Explanation

All matching numbers cancel through XOR, leaving only the missing number.

### Complexity

| Approach | Time | Space |
|---|---|---|
| Mathematical | O(n) | O(1) |
| XOR | O(n) | O(1) |

---

# 3. Number of 1 Bits

**LeetCode:** 191  
**Difficulty:** Easy

### Problem

Given a positive integer `n`, return the number of set bits (1s) in its binary representation.

### Example

```python
Input: n = 11
Output: 3
```

Binary representation: `1011`

### Approach 1 – Using bin()

```python
class Solution:
    def hamming
