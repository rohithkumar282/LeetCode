'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
'''


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum1=0
        list_sum=[]
        for i in range(n):
            sum1=0
            for j in range(i,n):
                sum1=sum1+nums[j]
                list_sum.append(sum1)
        list_sum.sort()
        sum1=0
        sum1 = sum(list_sum[left-1:right])

        return int(sum1%(10**9 + 7))
