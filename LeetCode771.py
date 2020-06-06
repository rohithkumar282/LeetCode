'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/jewels-and-stones/
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for ele in S:
            if ele in J:
                count=count+1
        return count
