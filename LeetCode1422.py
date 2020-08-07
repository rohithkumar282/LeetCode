'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
'''


class Solution:
    def maxScore(self, s: str) -> int:
        max_sum=0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:len(s)]
            print(left,right)
            left_count = left.count('0')
            right_count = right.count('1')
            if left_count+right_count>max_sum:
                max_sum = left_count+right_count
        return max_sum
