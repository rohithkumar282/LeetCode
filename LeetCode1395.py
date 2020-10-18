'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/count-number-of-teams/
'''


import itertools
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result=[]
        temp = itertools.combinations(rating, 3)
        for ele in temp:
            ele1,ele2,ele3 = list(ele),list(ele),list(ele)
            ele2.sort()
            ele3.sort(reverse=True)
            if ele1==ele2 or ele1==ele3:
                result.append(ele1)
        return len(result)
