'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/add-digits/
'''

class Solution:
    def addDigits(self, num: int) -> int:
        string = sum(list(map(int,list(str(num)))))
        if (len(str(string))!=1):
            string = self.addDigits(string)
        return string
