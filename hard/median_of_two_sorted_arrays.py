
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search
        return

if __name__ == "__main__":
    s = Solution()
    nums1 = []
    nums2 = []
    for i in range(len(nums1)):
        print(s.findMedianSortedArrays(nums1=nums1[i], nums2=nums2[i]))
