'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
'''
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        hash_tab = {}
        for j in range(len(A)):
            for i in range(len(A[j])):
                if A[j][i] not in hash_tab:
                    hash_tab[A[j][i]] = [0]*len(A)
                    hash_tab[A[j][i]][j]+= 1
                else:
                    hash_tab[A[j][i]][j]+=1
        for key,val in hash_tab.items():
            if min(val)!=0:
                result.extend([key]*min(val))
        return result
