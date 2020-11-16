'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        for ele in matrix:
            lucky = min(ele)
            pos = ele.index(lucky)
            key = 0
            for i in range(len(matrix)):
                temp = matrix[i][pos]
                if temp>lucky:
                    key = 1
                    break
            if key==0:
                result.append(lucky)
        return result
