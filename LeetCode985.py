'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
'''

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        total = sum([i for i in A if i % 2 == 0])
        answers = []
        for ele in queries:
            if A[ele[1]] % 2 == 0:
                total-= A[ele[1]]
            A[ele[1]]+= ele[0]
            if A[ele[1]] % 2 == 0:
                total+= A[ele[1]]
            answers.append(total)
        return answers
