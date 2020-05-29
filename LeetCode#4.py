'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist=[]
        newlist=nums1+nums2
        newlist.sort()
        n=len(newlist)
        l=(int)(n/2)
        if n%2==0:
            return((newlist[l-1]+newlist[l])/2)
        else:
            return(newlist[l])


