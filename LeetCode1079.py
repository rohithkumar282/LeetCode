'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/letter-tile-possibilities/
'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []
        for i in range(1,len(tiles)+1):
            temp = list(itertools.permutations(list(tiles),i))
            result.extend(temp)
        return len(set(result))
