'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/sort-array-by-parity-ii/
'''
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        result =[]
        for ele in A:
            if ele%2==0:
                even.append(ele)
            else:
                odd.append(ele)
        evn = 0
        od = 0
        for i in range(len(A)):
            if i%2==0:
                result.append(even[evn])
                evn+=1
            else:
                result.append(odd[od])
                od = od+1
        return result
