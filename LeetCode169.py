'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/majority-element/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = []
        set_nums = list(set(nums))
        for ele in set_nums:
            n = nums.count(ele)
            if n>len(nums)/2:
                count.append(n)
            else:
                count.append(0)
        return set_nums[count.index(max(count))]
