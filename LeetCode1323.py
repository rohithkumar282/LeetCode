'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/maximum-69-number/
'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        list1=[]
        result=""
        n = str(num)
        list1[:] = n
        for i in range(len(list1)):
            if list1[i]=='6':
                list1[i] = '9'
                break
        for ele in list1:
            result+=ele
        return int(result)
