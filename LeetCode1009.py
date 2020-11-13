'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/complement-of-base-10-integer/
'''
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        number = bin(N)[2:]
        result = ''
        for i in number:
            if i=='0':
                result = result+'1'
            else:
                result = result+'0'
        return int(result,2)
