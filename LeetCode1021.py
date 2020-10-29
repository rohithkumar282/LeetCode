'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/remove-outermost-parentheses/
'''
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        result = []
        for ele in S:
            if ele==')':
                count-=1
            if count>0:
                result.append(ele)
            if ele=='(':
                count+=1
        return (''.join(result))
