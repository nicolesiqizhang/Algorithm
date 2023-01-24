from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left <=  right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                a = mid
                b = mid
                while (a - 1) >= 0 and nums[a - 1] == target:
                    a = a - 1
                while (b + 1) <= len(nums) - 1 and nums[b + 1] == target:
                    b = b + 1
                return [a,b]
        return [-1,-1]


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    print("answer:",solution.searchRange(nums,target))


if __name__=="__main__":
    main()






