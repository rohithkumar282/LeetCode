'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/remove-element/
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        k=1
        while i<n:
            if nums[i]==val:
                for j in range(i,len(nums)-1):
                    nums[j]=nums[j+1]
                nums.pop(-1)
                n=n-1
                i=0
                k=0
            if i==0 and k==0:
                i=0
                k=1
            else:
                i=i+1
        if len(nums)==1 and nums[0]==val:
            nums.pop(-1)
        return len(nums)
