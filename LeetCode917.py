'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/reverse-only-letters/
'''

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        index=[]
        loc_index=0
        rev = ""
        for i in range(len(S)):
            if S[i].isalpha():
                index.append(i)
        index = index[::-1]
        for i in range(len(S)):
            if S[i].isalpha():
                rev =rev+ str(S[index[loc_index]])
                loc_index+=1
            else:
                rev = rev+S[i]
        return rev
