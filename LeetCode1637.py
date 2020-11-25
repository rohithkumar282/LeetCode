'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
'''

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        result = sorted(x for x, y in points)
        dist = []
        for i in range(len(result)-1):
            dist.append(result[i+1]-result[i])
        return max(dist)
