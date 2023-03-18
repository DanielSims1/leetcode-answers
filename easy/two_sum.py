"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[j] + n == target:
                    return [i, j]


if __name__ == "__main__":
    s = Solution()

    nums = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    targets = [9, 6, 6]

    for i in range(len(nums)):
        print(s.twoSum(nums=nums[i], target=targets[i]))
