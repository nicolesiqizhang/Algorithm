class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        # define DFS using the index of nums
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # consider include the nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # consider not to include the nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))

