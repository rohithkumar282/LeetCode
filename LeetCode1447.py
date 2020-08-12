'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/simplified-fractions/
'''


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result=[]
        temp=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if (j/i>0 and j/i<1 and j/i not in temp):
                    result.append(str(j)+str('/')+str(i))
                    temp.append(j/i)
        return(result)
