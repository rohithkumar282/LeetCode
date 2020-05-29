'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        number=0
        while(n!=0):
            digit=n%10
            number=number*10+digit
            n=(int)(n/10)
        if number == x:
            return 1
        elif x<0 & number==-x:
            return 1
        else:
            return 0
