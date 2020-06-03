'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_ret=list([-1,-1])
        n = len(nums)
        first1 = True
        if n < 1:
            if n==0:
                pass
        else:
            for i in range(0,(int)(n/2)):
                if nums[i]==target:
                    if first1:
                        first1 = False
                        target_ret[0]=i
                        target_ret[1]=i
                    else:
                        target_ret[1]=i
            for i in range((int)(n/2),n):
                if nums[i]==target:
                    if first1:
                        first1 = False
                        target_ret[0]=i
                        target_ret[1]=i
                    else:
                        target_ret[1]=i
        return target_ret
