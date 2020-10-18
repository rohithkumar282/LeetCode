'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result=[0]
        if n==1:
            return result
        else:
            if n%2!=0:
                for i in range(1,n+1):
                    result.extend([i,-i])
                    if sum(result)==0 and len(result)==n:
                        return result
            else:
                result=[]
                for i in range(1,n+1):
                    result.extend([i,-i])
                    if sum(result)==0 and len(result)==n:
                        return result
