'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/counting-bits/
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(num+1):
            result.append(list(bin(i)[2:]).count('1'))
        return result
