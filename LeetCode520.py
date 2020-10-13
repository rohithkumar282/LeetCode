'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/detect-capital/
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif (word[0].isupper() and word[1:].islower()) or word.islower():
            return True
        else:
            return False

