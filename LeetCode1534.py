'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/count-good-triplets/
'''

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        results = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            results += 1
        return results
