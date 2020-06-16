'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        total=0
        while(n!=0):
            pro*=int(n%10)
            total+=int(n%10)
            n=int(n/10)
        return pro-total
