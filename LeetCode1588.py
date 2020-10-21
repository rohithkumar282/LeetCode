'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(1,len(arr)+1,2):
            j = 0
            while(j+i<=len(arr) and i<=len(arr)):
                temp = arr[j:j+i]
                total = total+sum(temp)
                j = j+1
        return total
