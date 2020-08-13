'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
'''

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        import re
        key=-1
        list_compare=sentence.split(" ")
        for ele in list_compare:
            if re.match(searchWord,ele):
                key = list_compare.index(ele)+1
                break
        return key
