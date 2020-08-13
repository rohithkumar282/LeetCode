'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1,len(A)-1):
            if A[i-1]<A[i] and A[i]>A[i+1]:
                return i
