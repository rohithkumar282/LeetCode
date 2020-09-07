'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)-len(nums2)
        for j in range(len(nums2)):
            nums1[k+j] = nums2[j]
        nums1.sort()
