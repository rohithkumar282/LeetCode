'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/reshape-the-matrix/
'''

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        numbers = [j for i in nums for j in i]
        if len(numbers)!=r*c:
            return nums
        return [numbers[i*c:(i+1)*c] for i in range(r)]
