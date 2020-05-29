'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/squares-of-a-sorted-array/
'''

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n=len(A)
        for i in range(n):
            A[i]=A[i]*A[i]
        A.sort()
        return A
