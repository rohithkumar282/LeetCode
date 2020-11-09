'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/three-consecutive-odds/
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)-2):
            temp = arr[i:i+3]
            if temp[0]%2!=0 and temp[1]%2!=0 and temp[2]%2!=0:
                return True
        return False
