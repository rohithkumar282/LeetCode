'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/thousand-separator/
'''

class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = ""
        temp_result=[]
        if n<1000:
            return str(n)
        else:
            m = str(n)
            while(m):
                temp_result.append(m[-3:])
                m = m[:-3]
            temp_result.reverse()
            for ele in temp_result:
                result = result+ele+'.'
            result = result[:-1]
            return result
