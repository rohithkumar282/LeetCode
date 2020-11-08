'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/robot-return-to-origin/
'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for ele in moves:
            if ele =='U':
                pos[0] = pos[0]+1
            elif ele =='D':
                pos[0] = pos[0]-1
            elif ele =='L':
                pos[1] = pos[1]-1
            elif ele =='R':
                pos[1] = pos[1]+1
        return pos==[0,0]
