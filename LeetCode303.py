'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/range-sum-query-immutable/
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums


    def sumRange(self, i: int, j: int) -> int:
        total=0
        for k in range(i,j+1):
            total=total+self.nums[k]
        return total
