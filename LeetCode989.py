'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/add-to-array-form-of-integer/
'''
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        number = 0
        for ele in A:
            number = number*10 + ele
        number = number + K
        result = [int(i) for i in str(number)]
        return result
