'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/longest-word-in-dictionary/
'''
class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word
        return ans
