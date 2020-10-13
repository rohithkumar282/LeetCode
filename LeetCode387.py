'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/first-unique-character-in-a-string/
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = collections.Counter(s)

        for pos,char in enumerate(s):
            if count_dict[char] == 1:
                return pos
        return -1
