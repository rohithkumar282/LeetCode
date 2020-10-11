'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/number-complement/
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result=""
        if num==1 or num==0:
            if num==1:
                return 0
            else:
                return 1
        else:
            n = str(bin(num)[2:])
            for i in range(len(n)):
                if n[i]=='1':
                    result=result+'0'
                else:
                    result=result+'1'
            return(int(result,2))
