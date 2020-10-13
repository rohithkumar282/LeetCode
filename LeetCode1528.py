'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/shuffle-string/
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result =""
        for i in range(len(s)):
            result = result+s[indices.index(i)]
        return result
