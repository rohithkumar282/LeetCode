'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        result = []
        for ele in salary:
            if ele!=min(salary) and ele!=max(salary):
                result.append(ele)
        return(sum(result)/len(result))
