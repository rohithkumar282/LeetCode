'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/flipping-an-image/
'''
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for ele in A:
            ele.reverse()
            for i in range(len(ele)):
                if ele[i]==0:
                    ele[i]=1
                else:
                    ele[i]=0
            result.append(ele)
        return result
