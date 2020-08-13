'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/sort-characters-by-frequency/
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        dict_val={}
        result=''

        for key in set(s):
            dict_val[key] = s.count(key)

        sort_orders = sorted(dict_val.items(), key=lambda x: x[1], reverse=True)

        for i in sort_orders:
            result=result+i[0]*i[1]
        return(result)
