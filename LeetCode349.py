'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/intersection-of-two-arrays/
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_list=[]
        for i in range(len(nums1)):
            if (nums1[i] in nums2) and (nums1[i] not in final_list):
                final_list.append(nums1[i])
        return final_list
