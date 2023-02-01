class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)
            res.extend(perms)
            nums.append(num)
        return res

nums = [1, 2, 3]
solution = Solution()
print(solution.permute(nums))