'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/matrix-diagonal-sum/
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        coords = []
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j and [i,j] not in coords:
                    total = total + mat[i][j]
                    coords.append([i,j])
                elif i+j==len(mat)-1 and [i,j] not in coords:
                    total = total + mat[i][j]
                    coords.append([i,j])
        return total
