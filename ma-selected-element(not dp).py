class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        prev = float('-inf')
        count = 0
        ans = 0

        for num in nums:
            if num > prev + 1:
                prev = num
                count = 1

            elif num == prev + 1:
                prev = num
                count += 1

            else:
                prev += 1
                count += 1

            ans = max(ans, count)

        return ans
