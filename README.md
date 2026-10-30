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
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

### Approach 2 – Bit Manipulation

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count
```

### Approach 3 – Brian Kernighan's Algorithm

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count
```

### Explanation

- `n & 1` checks the last bit.
- `n >> 1` shifts bits to the right.
- `n & (n - 1)` removes the rightmost set bit.

### Complexity

| Approach | Time | Space |
|---|---|---|
| bin().count() | O(k) | O(k) |
| Right Shift | O(32) | O(1) |
| Brian Kernighan | O(k) | O(1) |

Here, `k` represents the number of set bits.

---

# 4. Counting Bits

**LeetCode:** 338  
**Difficulty:** Easy

### Problem

Given an integer `n`, return an array of length `n + 1`, where each element contains the number of 1s in the binary representation of its index.

### Example

```python
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

### Approach 1 – Using bin()

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            result.append(bin(i).count('1'))

        return result
```

### Approach 2 – Dynamic Programming (Optimized)

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
```

### Explanation

Formula:

`dp[i] = dp[i // 2] + (i % 2)`

- `i >> 1` divides the number by 2.
- `i & 1` checks whether the last bit is 1.
- `dp[i]` stores the total number of set bits.

### Complexity

| Approach | Time | Space |
|---|---|---|
| bin().count() | O(n log n) | O(n) |
| Dynamic Programming | O(n) | O(n) |

---

# 5. Subsets

**LeetCode:** 78  
**Difficulty:** Medium

### Problem

Given an integer array `nums` containing unique elements, return all possible subsets (the power set).

### Example

```python
Input: nums = [1, 2, 3]

Output:
[
    [],
    [1],
    [2],
    [1, 2],
    [3],
    [1, 3],
    [2, 3],
    [1, 2, 3]
]
```

### Important Formula

Total number of subsets:

`2^n`

### Approach 1 – Backtracking

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])
        return result
```

### Explanation

1. Start with an empty subset.
2. Add the current subset to the result.
3. Choose an element.
4. Recursively explore the remaining elements.
5. Remove the last element using `pop()`.

**Backtracking Pattern:**

`Choose → Explore → Undo`

### Approach 2 – Bit Manipulation

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        for i in range(1 << n):
            subset = []

            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])

            result.append(subset)

        return result
```

### Explanation

- `1 << n` generates `2^n` combinations.
- `1 << j` identifies the bit position.
- `i & (1 << j)` checks whether an element is selected.
- If the bit is 1, add that element to the subset.

### Complexity

- Time: O(n × 2^n)
- Auxiliary Space: O(n), excluding output.

---

# Important Python & DSA Concepts

| Concept | Usage |
|---|---|
| XOR (`^`) | Cancel duplicate numbers |
| AND (`&`) | Check binary bits |
| Right Shift (`>>`) | Divide by 2 |
| Left Shift (`<<`) | Multiply by powers of 2 |
| `bin()` | Convert integer to binary |
| `enumerate()` | Get index and value |
| `append()` | Add elements |
| `pop()` | Remove the last element |
| Recursion | Solve smaller subproblems |
| Backtracking | Explore all possible choices |
| Dynamic Programming | Reuse previously calculated results |

---

# Important Formulas to Remember

1. XOR: `a ^ a = 0`
2. Expected sum: `n * (n + 1) // 2`
3. Set bit check: `n & 1`
4. Remove rightmost set bit: `n & (n - 1)`
5. Number of subsets: `2^n`
6. Divide by 2 using bits: `n >> 1`
7. Multiply by 2 using bits: `n << 1`

---

# Learning Progress

- [x] Single Number – 136
- [x] Missing Number – 268
- [x] Number of 1 Bits – 191
- [x] Counting Bits – 338
- [x] Subsets – 78

---

## Key Takeaways

- Use XOR to solve problems involving duplicate numbers.
- Use bit manipulation to efficiently work with binary representations.
- Use Dynamic Programming when previously calculated results can be reused.
- Use Backtracking to generate combinations and explore possibilities.

**Practice Goal:** Understand the logic, implement the solution independently, and analyze time and space complexity before moving to the next problem.

---

**Language:** Python 3  
**Platform:** LeetCode  
**Repository:** DSA Practice
