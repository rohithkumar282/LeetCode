'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/max-consecutive-ones/
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count=0
        for ele in nums:
            if ele==1:
                count=count+1
                print(count)
            else:
                count=0
            if count>=max_count:
                max_count = count
        return max_count
