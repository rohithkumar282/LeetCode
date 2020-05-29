'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        romans1={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        n=len(s)
        i=0
        while(i<n):
            if ((i<n-1) and (s[i]+s[i+1]=='IV' or s[i]+s[i+1]=='IX' or s[i]+s[i+1]=='XL'or s[i]+s[i+1]=='XC' or s[i]+s[i+1]=='CD' or s[i]+s[i+1]=='CM')):
                a=s[i]+s[i+1]
                print(a)
                print(romans1.get(a))
                total=total+romans1.get(a)
                i=i+2
            else:
                total=total+romans.get(s[i])
                i=i+1
        return total
