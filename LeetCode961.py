'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
'''
from collections import Counter
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        temp = Counter(A)
        temp = sorted(temp.items(), key = lambda x:x[1],reverse=True)
        return temp[0][0]
