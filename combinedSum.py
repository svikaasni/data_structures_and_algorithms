class Solution:
    def combinationSum(self, candidates, target):
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                backtrack(i, remaining - candidates[i])

                path.pop()

        candidates.sort()
        backtrack(0, target)

        return result
