'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/distribute-candies-to-people/
'''
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0]*num_people
        n = candies
        i = 0
        count = 0
        while n>=0 and i<len(result):
            result[i] = result[i]+count*len(result)+i+1
            n = n - (count*len(result)+i+1)
            if n<0:
                result[i] = result[i]+n
            i = i+1
            if i==len(result) and n>=0:
                count = count+1
                i = 0
        return result

