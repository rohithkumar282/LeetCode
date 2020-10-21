'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        output = ""
        arr = list(s)
        while arr:
            ele = arr.pop()
            if ele=='#':
                new_no = ""
                new_no+= arr.pop(-2)
                new_no+= arr.pop(-1)
                result.append(int(new_no))
            else:
                result.append(int(ele))
        for ele in result:
            output = output+ chr(96+ele)
        output = output[::-1]
        return output
