'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        final_res = ""
        list_str = s.split()
        for ele in list_str:
            result.append(ele[::-1])
        for ele in result:
            final_res+=ele
            final_res+=" "
        return final_res[:-1]
