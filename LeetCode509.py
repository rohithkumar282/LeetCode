'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/fibonacci-number/
'''

class Solution:
    def fib(self, N: int) -> int:
        fn = 1
        fn1 = 0
        i=1
        fnt = 0
        if N==1:
            return 1
        else:
            while(i<=N-1 and N>1):
                fnt = fn+fn1
                fn1 = fn
                fn = fnt
                i = i+1
            return fnt
