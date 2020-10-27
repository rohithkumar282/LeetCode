'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/unique-number-of-occurrences/
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = []
        list_new = list(set(arr))
        for ele in list_new:
            result.append(arr.count(ele))
        int_list = list(set(result))
        return len(result) == len(int_list)
