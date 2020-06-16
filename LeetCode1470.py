'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/shuffle-the-array/
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final_array=[]
        for i in range(n):
            final_array.append(nums[i])
            final_array.append(nums[n+i])
        return final_array
