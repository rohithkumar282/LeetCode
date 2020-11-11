'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/maximum-number-of-balloons/
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        string = ['b', 'a', 'l', 'o', 'n']
        count = [0] * 5
        for i in range(len(string)):
            count[i] = text.count(string[i])
        count[2] = count[2]// 2
        count[3] = count[3]// 2
        return min(count)
