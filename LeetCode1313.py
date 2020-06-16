'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/decompress-run-length-encoded-list/
'''

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums),2):
            result+=[nums[i+1]]*nums[i]
        return result
