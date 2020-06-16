'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for ele in nums:
            if len(str(ele))%2==0:
                count+=1
        return count
