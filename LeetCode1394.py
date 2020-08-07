'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-lucky-integer-in-an-array/
'''


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count=0
        lucky=0
        new_list = []
        for ele in arr:
            if ele not in new_list:
                new_list.append(ele)
        for ele in new_list:
            count  = arr.count(ele)
            if count==ele:
                if ele >=lucky:
                    lucky = ele
            count=0
        if not lucky:
            return -1
        else:
            return lucky
