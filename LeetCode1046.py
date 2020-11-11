'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/last-stone-weight/
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = stones.copy()
        temp.sort(reverse=True)
        result = []
        while len(temp)!=1:
            x = temp[1]
            y = temp[0]
            if x<=y:
                if len(temp)==2:
                    return y-x
                elif x==y and len(temp)!=2:
                    temp = temp[2:]
                else:
                    res = y-x
                    temp = temp[2:]+[res]
                    temp.sort(reverse=True)
        return temp[0]
