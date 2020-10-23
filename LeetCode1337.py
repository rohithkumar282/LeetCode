'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        dict_res = {}
        for ele in mat:
            result.append(ele.count(1))
        for ele1,ele2 in enumerate(result):
            dict_res[ele1] = ele2
        dict_res = sorted(dict_res.items(),key = lambda x:x[1])
        result=[]
        j = 0
        for ele in dict_res:
            if j<k:
                result.append(ele[0])
                j = j+1
        return result
