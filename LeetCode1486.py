'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/xor-operation-in-an-array/
'''
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        i = 0
        result = 0
        while(i<n):
            nums.append(start+2*i)
            if i==0:
                result = nums[0]
            elif i>0:
                result = result^nums[i]
            i = i+1
        return result
