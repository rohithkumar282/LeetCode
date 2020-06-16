'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for i in range(len(candies)):
            temp=candies[i]+extraCandies
            max_value=max(candies)
            if temp>=max_value:
                result.append(True)
            else:
                result.append(False)
        return result
