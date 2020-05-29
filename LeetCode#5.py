'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome=[]
        length=[]
        k=0
        b=''
        for i in range(len(s)):
            a=''
            a=a+s[i]
            if i==0:
                b=s[i]
            for j in range(i+1,len(s)):
                a=a+s[j]
                if a == a[::-1]:
                    k=1
                    longest_palindrome.append(a)
                    length.append(len(a))
        if k==0:
            return b
        max_len=max(length)
        return (longest_palindrome[length.index(max_len)])
