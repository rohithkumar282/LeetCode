'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/rotate-image/
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i<j:
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
        for i in range(len(matrix)):
            for j in range((int)(len(matrix[i])/2)):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][len(matrix[i])-1-j]
                matrix[i][len(matrix[i])-1-j]=temp


        """
        Do not return anything, modify matrix in-place instead.
        """
