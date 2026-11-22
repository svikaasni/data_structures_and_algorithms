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

---

# LeetCode 1524 – Number of Sub-arrays With Odd Sum

## Problem Description
Given an integer array `arr`, return the number of subarrays whose sum is odd.

Since the answer can be large, return it modulo `10^9 + 7`.

**LeetCode:** [1524. Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)

## Approach: Prefix Sum + Parity

We use prefix sums to efficiently count subarrays with odd sums.

### Key Observation
A subarray sum is odd when the two prefix sums have different parity.

- Odd prefix - Even prefix = Odd
- Even prefix - Odd prefix = Odd
- Odd prefix - Odd prefix = Even
- Even prefix - Even prefix = Even

### Variables Used
- `odd`: Count of odd prefix sums.
- `even`: Count of even prefix sums.
- `prefix`: Running prefix sum.
- `result`: Number of subarrays with odd sums.
- `MOD`: Modulo value (`10^9 + 7`).

Initially:
- `odd = 0`
- `even = 1` (empty prefix sum is zero).

## Python Solution

```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix = 0
        result = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                result += odd
                even += 1
            else:
                result += even
                odd += 1

        return result % MOD
```

## Example

**Input:**
```python
arr = [1, 3, 5]
```

**Output:**
```python
4
```

**Explanation:**

The subarrays with odd sums are:
- `[1]` → Sum = 1
- `[3]` → Sum = 3
- `[5]` → Sum = 5
- `[1, 3, 5]` → Sum = 9

Total = 4.

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(n) | Single traversal of the array |
| Space | O(1) | Uses constant extra variables |

## Concepts Learned
- Prefix Sum
- Odd and Even Parity
- Subarray Counting
- Mathematical Observation
- Space Optimization

## Test Cases

| Input | Output |
|---|---:|
| `[1, 3, 5]` | 4 |
| `[2, 4, 6]` | 0 |
| `[1, 2, 3]` | 4 |
| `[1]` | 1 |

## Key Takeaway

Instead of generating every possible subarray and calculating its sum, prefix sum parity allows us to count odd-sum subarrays in **O(n) time and O(1) space**.

---


# LeetCode Problem Solutions – Python 3

This repository contains Python solutions for LeetCode problems, focusing on problem-solving, algorithms, and data structures.

## Problems Solved

| No. | Problem Name | Difficulty | Concepts |
|---|---|---|---|
| 40 | Combination Sum II | Medium | Backtracking, Recursion, Sorting |
| 41 | First Missing Positive | Hard | Cyclic Sort, Array Manipulation |
| 2243 | Calculate Digit Sum of a String | Easy | Strings, Loops, Mathematics |

---

## 1. LeetCode 40 – Combination Sum II

**Problem:** Find all unique combinations of candidates that sum up to a given target. Each number can be used only once.

**Example:**

Input:
```python
candidates = [10,1,2,7,6,1,5]
target = 8
```

Output:
```python
[[1,1,6], [1,2,5], [1,7], [2,6]]
```

**Approach:**
- Sort the input array.
- Use backtracking to explore possible combinations.
- Skip duplicate elements to avoid duplicate combinations.
- Use `i + 1` to ensure each element is used only once.
- Stop exploring when the sum exceeds the target.

**Key Concepts:** Backtracking, Recursion, Sorting, Duplicate Handling.

---

## 2. LeetCode 41 – First Missing Positive

**Problem:** Find the smallest missing positive integer from an unsorted integer array in O(n) time and O(1) extra space.

**Example:**

Input:
```python
nums = [3, 4, -1, 1]
```

Output:
```python
2
```

**Approach:**
- Use the Cyclic Sort technique.
- Place each positive number at its correct index.
- Ignore negative numbers, zero, and numbers greater than the array length.
- Find the first index where the value does not match `index + 1`.
- Return `n + 1` if all positions are correct.

**Key Concepts:** Cyclic Sort, Array Manipulation, In-place Swapping, Index Mapping.

---

## 3. LeetCode 2243 – Calculate Digit Sum of a String

**Problem:** Repeatedly divide a numeric string into groups of size `k`, calculate the digit sum of each group, and concatenate the sums until the string length is less than or equal to `k`.

**Example:**

Input:
```python
s = "11111222223"
k = 3
```

Output:
```python
"135"
```

**Approach:**
- Divide the string into groups of size `k`.
- Calculate the sum of digits in each group.
- Convert each sum into a string.
- Concatenate the group sums.
- Repeat until the string length is less than or equal to `k`.

**Key Concepts:** String Manipulation, Loops, Slicing, Mathematics.

---

## Technologies Used

- **Language:** Python 3
- **Platform:** LeetCode
- **Topics:** Arrays, Strings, Backtracking, Recursion, Sorting, Cyclic Sort.

## Learning Outcomes

- Improved problem-solving and logical thinking.
- Practiced recursion and backtracking.
- Learned efficient array manipulation techniques.
- Understood string slicing and digit operations.
- Practiced time and space complexity analysis.

## Repository Structure

```text
LeetCode/
│
├── 40_Combination_Sum_II.py
├── 41_First_Missing_Positive.py
├── 2243_Calculate_Digit_Sum.py
└── README.md
```

## Goal

Consistently practice LeetCode problems to strengthen Data Structures and Algorithms (DSA) skills and prepare for technical interviews and coding assessments.

---

# LeetCode Practice – Problems 2911 & 42

This repository contains Python solutions for two LeetCode problems, focusing on Dynamic Programming, Two Pointers, and Array Optimization.

---

# 1. LeetCode 2911 – Minimum Changes to Make K Semi-palindromes

**Difficulty:** Hard  
**Topics:** Dynamic Programming, Strings, Divisors, Precomputation

## Problem Description

Given a string `s` and an integer `k`, divide the string into exactly `k` non-empty contiguous substrings.

Each substring must be a semi-palindrome. Return the minimum number of character changes required to make all substrings semi-palindromes.

## Python Solution

```python
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        # Calculate minimum changes for every substring
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for r in range(d):
                        left = i + r
                        right = i + r + (groups - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(2, n + 1):
            for p in range(1, k + 1):
                for j in range(i - 1):
                    if dp[j][p - 1] != INF:
                        dp[i][p] = min(
                            dp[i][p],
                            dp[j][p - 1] + cost[j][i - 1]
                        )

        return dp[n][k]
```

## Approach

1. Calculate the minimum changes required to convert each substring into a semi-palindrome.
2. Find all valid divisors of the substring length.
3. Divide the substring into groups based on the divisor.
4. Compare characters from both ends of each group.
5. Use Dynamic Programming to divide the string into exactly `k` valid substrings with minimum changes.

## Complexity Analysis

- **Time Complexity:** O(n⁴ + kn²) for this implementation.
- **Space Complexity:** O(n² + nk).

## Key Concepts

- Dynamic Programming
- String Manipulation
- Divisors and Modulo
- Palindrome Checking
- Substring Partitioning

---

# 2. LeetCode 42 – Trapping Rain Water

**Difficulty:** Hard  
**Topics:** Arrays, Two Pointers, Greedy Algorithm

## Problem Description

Given an array `height` representing an elevation map where each bar has a width of 1, calculate how much water can be trapped between the bars after raining.

## Example 1

**Input:**
```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

**Output:**
```python
6
```

## Example 2

**Input:**
```python
height = [4,2,0,3,2,5]
```

**Output:**
```python
9
```

## Python Solution – Two Pointers

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
```

## Approach

1. Initialize two pointers at the beginning and end of the array.
2. Maintain the maximum height encountered from both sides.
3. Process the side with the smaller current boundary.
4. Calculate trapped water using the difference between the maximum boundary and current height.
5. Continue until both pointers meet.

## Water Calculation Formula

`Water = min(left_max, right_max) - height[i]`

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Key Concepts

- Two Pointer Technique
- Greedy Algorithm
- Array Traversal
- Prefix Maximum
- Suffix Maximum
- Space Optimization

---

# Overall Learning Outcomes

| Problem | Main Technique | Time Complexity | Space Complexity |
|---|---|---|---|
| LeetCode 2911 | Dynamic Programming | O(n⁴ + kn²) | O(n² + nk) |
| LeetCode 42 | Two Pointers | O(n) | O(1) |

## Skills Practiced

- Python Programming
- Problem Solving
- Dynamic Programming
- String Manipulation
- Array Optimization
- Algorithm Complexity Analysis

**Goal:** Improve problem-solving skills and develop optimized solutions for technical interviews and coding assessments.

---

*Language: Python 3 | Platform: LeetCode*


---


# LeetCode 2914 – Minimum Number of Changes to Make Binary String Beautiful

## Problem
Given a binary string `s` of even length, find the minimum number of character changes required to make the string beautiful.

A string is beautiful if every pair of adjacent characters is equal (`00` or `11`).

## Approach – Greedy

1. Initialize a counter `count = 0`.
2. Traverse the string in steps of 2.
3. Compare each pair of adjacent characters.
4. If the characters are different, increment the counter.
5. Return the total count.

## Python Solution

```python
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                count += 1

        return count
```

## Example

**Input:**
```python
s = "1001"
```

**Output:**
```python
2
```

**Explanation:**

- Pair `"10"` requires one change.
- Pair `"01"` requires one change.
- Total minimum changes = 2.

## Complexity Analysis

- **Time Complexity:** O(n) – Each pair is checked once.
- **Space Complexity:** O(1) – Only a counter is used.

## Key Concepts
- Greedy Algorithm
- String Traversal
- Pair Comparison

## LeetCode Link
https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

**Status:** Solved ✅

---

# LeetCode 45 – Jump Game II

## Problem
Given an integer array `nums`, where each element represents the maximum number of steps you can jump forward, find the minimum number of jumps required to reach the last index.

## Approach – Greedy Algorithm

1. Initialize three variables:
   - `jumps = 0`
   - `current_end = 0`
   - `farthest = 0`
2. Traverse the array until the second-last index.
3. Update the farthest reachable position using `i + nums[i]`.
4. Whenever the current index reaches `current_end`, increment the jump count.
5. Update `current_end` to `farthest`.
6. Return the minimum number of jumps.

## Python Solution

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
```

## Example 1

**Input:**
```python
nums = [2, 3, 1, 1, 4]
```

**Output:**
```python
2
```

**Explanation:**

- Start at index 0.
- Jump from index 0 to index 1.
- Jump from index 1 to index 4.
- Minimum jumps required = 2.

## Example 2

**Input:**
```python
nums = [2, 3, 0, 1, 4]
```

**Output:**
```python
2
```

## Complexity Analysis

- **Time Complexity:** O(n) – The array is traversed once.
- **Space Complexity:** O(1) – Only three variables are used.

## Key Concepts
- Greedy Algorithm
- Array Traversal
- Range Tracking
- Optimization

## LeetCode Link
https://leetcode.com/problems/jump-game-ii/

**Status:** Solved ✅

---

# LeetCode 46 – Permutations

## Problem Statement
Given an array `nums` containing distinct integers, return all possible permutations in any order.

A permutation is a rearrangement of all elements in a particular sequence.

## Approach – Backtracking

Backtracking is used to generate all possible arrangements by exploring different choices.

### Algorithm
1. Initialize an empty result list.
2. Create a recursive function `backtrack()`.
3. Select an element from the remaining elements.
4. Add the selected element to the current path.
5. Recursively explore the remaining elements.
6. Use `pop()` to undo the selection.
7. When no elements remain, add the current permutation to the result.
8. Return all permutations.

## Python Solution

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return

            for i in range(len(remaining)):
                path.append(remaining[i])

                backtrack(
                    path,
                    remaining[:i] + remaining[i+1:]
                )

                path.pop()

        backtrack([], nums)

        return result
```

## Example 1

**Input:**
```python
nums = [1, 2, 3]
```

**Output:**
```python
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
```

**Explanation:**

There are 6 possible permutations of the three elements.

## Example 2

**Input:**
```python
nums = [0, 1]
```

**Output:**
```python
[[0, 1], [1, 0]]
```

## Complexity Analysis

- **Time Complexity:** O(n × n!) – Generates n! permutations, each containing n elements.
- **Space Complexity:** O(n × n!) – Stores all permutations. Auxiliary recursion space is O(n).

## Key Concepts
- Backtracking
- Recursion
- Array Manipulation
- List Slicing
- Depth-First Search (DFS)

## Important Python Functions

| Function | Purpose |
|---|---|
| `append()` | Adds an element to the current path |
| `pop()` | Removes the last selected element |
| `path[:]` | Creates a copy of the current permutation |
| `backtrack()` | Explores possible arrangements |

## Leet

---

# LeetCode 3041 – Maximize Consecutive Elements in an Array After Modification

## Problem Description
Given a 0-indexed array `nums`, you can increase the value of any element by at most one. You need to select a subsequence of the modified array such that the selected elements form a consecutive sequence of integers.

Return the maximum possible length of such a subsequence.

## Approach: Sorting + Dynamic Programming

1. Sort the array to process elements in increasing order.
2. Maintain a DP dictionary to store the maximum length of a consecutive subsequence ending at a particular value.
3. For each element `num`:
   - Update `dp[num + 1]` using the best sequence ending at `num`.
   - Update `dp[num]` using the best sequence ending at `num - 1`.
4. Maintain the maximum length throughout the traversal.

## Python Solution

```python
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0

        for num in nums:
            dp[num + 1] = max(dp.get(num + 1, 0),
                              dp.get(num, 0) + 1)

            dp[num] = max(dp.get(num, 0),
                          dp.get(num - 1, 0) + 1)

            ans = max(ans, dp[num], dp[num + 1])

        return ans
```

## Example

**Input:**
```python
nums = [2, 1, 5, 1, 1]
```

**Output:**
```python
4
```

**Explanation:**

After modification, we can select the consecutive sequence:

`[1, 2, 3, 4]`

Therefore, the maximum possible length is `4`.

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(n log n) | Sorting + DP traversal |
| Space | O(n) | DP dictionary |

## Key Concepts
- Array Manipulation
- Sorting
- Greedy Optimization
- Dynamic Programming
- Hash Maps

## Key Takeaway
This problem demonstrates how sorting combined with dynamic programming can efficiently find the longest consecutive subsequence when each element can be increased by at most one.

**LeetCode Problem:** [3041 – Maximize Consecutive Elements in an Array After Modification](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/)

**Difficulty:** Hard

**Language:** Python 3

---

# LeetCode 47 – Permutations II

## Problem Description
Given an integer array `nums` that may contain duplicate elements, return all possible unique permutations.

The solution must not contain duplicate permutations.

## Approach: Backtracking + Sorting

1. Sort the input array to place duplicate elements next to each other.
2. Create a `used` array to track which elements have already been selected.
3. Use backtracking to generate permutations.
4. Skip duplicate elements using the condition:
   ```python
   if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
       continue
   ```
5. Once the permutation reaches the original array length, add a copy of it to the result.
6. Backtrack by removing the last element and marking it as unused.

## Python Solution

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return res
```

## Example 1

**Input:**
```python
nums = [1, 1, 2]
```

**Output:**
```python
[[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

**Explanation:**

The array contains duplicate values, but the algorithm generates only unique permutations.

## Example 2

**Input:**
```python
nums = [1, 2, 3]
```

**Output:**
```python
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
```

## Complexity Analysis

Let:
- `n` = Number of elements.
- `k` = Number of unique permutations.

| Complexity | Value |
|---|---|
| Time | O(n × n!) |
| Auxiliary Space | O(n) |
| Output Space | O(k × n) |

## Key Concepts
- Backtracking
- Recursion
- Sorting
- Duplicate Handling
- Boolean Visited Array

## Key Takeaway
Backtracking explores all possible arrangements, while sorting and duplicate-skipping conditions ensure that each unique permutation is generated only once.

## Related Problem
- [LeetCode 46 – Permutations](https://leetcode.com/problems/permutations/)

**LeetCode Problem:** [47 – Permutations II](https://leetcode.com/problems/permutations-ii/)

**Difficulty:** Medium

**Language:** Python 3

---

# LeetCode 48 – Rotate Image

## Problem Description
Given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees clockwise.

The rotation must be performed in-place without creating another matrix.

## Approach: Transpose + Reverse

The matrix can be rotated efficiently using two steps:

1. **Transpose the Matrix**
   - Convert rows into columns.
   - Swap `matrix[i][j]` with `matrix[j][i]`.
   - Traverse only the upper triangular portion to avoid swapping elements twice.

2. **Reverse Each Row**
   - Reverse every row of the transposed matrix.
   - This produces the required 90-degree clockwise rotation.

## Python Solution

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = (
                    matrix[j][i], matrix[i][j]
                )

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
```

## Example

**Input:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Output:**
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

**Explanation:**

First, transpose the matrix:

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

Then reverse each row to obtain the final rotated matrix.

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(n²) | Matrix transposition and row reversal |
| Auxiliary Space | O(1) | In-place modification |

## Key Concepts
- 2D Arrays
- Matrix Traversal
- Matrix Transposition
- In-place Swapping
- Row Reversal

## Key Takeaway
A 90-degree clockwise matrix rotation can be performed efficiently using the **Transpose + Reverse** technique without allocating an additional matrix.

## Related Problems
- [LeetCode 54 – Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [LeetCode 73 – Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- [LeetCode 1886 – Determine Whether Matrix Can Be Obtained By Rotation](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/)

**LeetCode Problem:** [48 – Rotate Image](https://leetcode.com/problems/rotate-image/)

**Difficulty:** Medium

**Language:** Python 3

---

# LeetCode 2124 – Check if All A's Appears Before All B's

## Problem Statement
Given a string `s` consisting only of characters `'a'` and `'b'`, determine whether every occurrence of `'a'` appears before every occurrence of `'b'`.

Return `True` if the condition is satisfied; otherwise, return `False`.

## Approach: String Traversal

The solution checks whether the substring `"ba"` exists in the given string.

- If `"ba"` exists, an `'a'` appears after a `'b'`, violating the condition.
- If `"ba"` does not exist, all `'a'` characters appear before all `'b'` characters.

## Python Solution

```python
class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
```

## Example

**Input:**
```python
s = "aaabbb"
```

**Output:**
```python
True
```

**Explanation:**
All occurrences of `'a'` appear before `'b'`.

**Input:**
```python
s = "abab"
```

**Output:**
```python
False
```

**Explanation:**
An `'a'` appears after a `'b'`, so the condition is violated.

## Complexity Analysis

- **Time Complexity:** O(n) – The string is traversed to check for the substring `"ba"`.
- **Space Complexity:** O(1) – No additional data structures are used.

## Key Concepts
- String Manipulation
- Substring Checking
- Logical Conditions
- Time and Space Complexity

## LeetCode Details
- **Problem Number:** 2124
- **Difficulty:** Easy
- **Language:** Python
- **Topic:** String
