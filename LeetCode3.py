'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=[]
        sublength=[0]
        char=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in char:
                    char=char+s[j]
                else:
                    break
            if char not in substring:
                substring.append(char)
                sublength.append(len(char))
            char=""
        return max(sublength)
