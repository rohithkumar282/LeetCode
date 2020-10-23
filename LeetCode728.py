'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/self-dividing-numbers/
'''
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right+1):
            key=0
            num = i
            while(num):
                j = num%10
                if j==0 or i%j!=0:
                    key=1
                    break
                num = int(num/10)
            if key==0:
                result.append(i)
        return result
