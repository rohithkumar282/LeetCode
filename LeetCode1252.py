'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = []
        count = 0
        for i in range(n):
            matrix.append([0]*m)
        for ele in indices:
            for i in range(len(matrix[ele[0]])):
                matrix[ele[0]][i]+=1
            for j in range(len(matrix)):
                matrix[j][ele[1]]+=1

        for ele in matrix:
            for ele1 in ele:
                if ele1%2!=0:
                    count=count+1
        return count

