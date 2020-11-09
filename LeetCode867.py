'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/transpose-matrix/
'''
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A[0])):
            result.append([ele[i] for ele in A])
        return result
