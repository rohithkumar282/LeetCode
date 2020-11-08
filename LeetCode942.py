'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/di-string-match/
'''
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        i=0
        j = len(S)
        for ele in S:
            if ele=='I':
                result.append(i)
                i = i+1
            else:
                result.append(j)
                j = j-1
        if S[-1]=='I':
            result.append(i)
        else:
            result.append(j)
        return result
