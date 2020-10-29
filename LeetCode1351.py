'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for ele in grid:
            ele.sort()
            for ele1 in ele:
                if  ele1>=0:
                    break
                else:
                    count+=1
        return count
