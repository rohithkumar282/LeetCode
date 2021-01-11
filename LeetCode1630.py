'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/arithmetic-subarrays/
'''

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arr=[]
        result = []
        flag=1
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            diff = arr[1]-arr[0]
            for j in range(1,len(arr)-1):
                if (arr[j+1]-arr[j]!=diff):
                    flag=0
                    break
            if flag==1:
                result.append(True)
            else:
                result.append(False)
            flag=1
        return result
