'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/string-matching-in-an-array/
'''

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]
        temp =[]
        for i in range(len(words)):
            temp = words[:i]+words[i+1:]
            for ele in temp:
                if words[i] in ele:
                    result.append(words[i])
        result = list(set(result))
        return result
