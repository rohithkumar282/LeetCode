'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/length-of-last-word/
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        count=0
        if n==0 or (n==1 and s==" "):
            return 0
        else:
            for i in range(n-1,-1,-1):
                print(i)
                if s[i].isalpha() and s[i]!=" ":
                    count=count+1
                elif s[i]==" " and i!=n-1 and count>0:
                    return count
                if i==0 and count>=0:
                    return count
