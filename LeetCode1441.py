'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/build-an-array-with-stack-operations/
'''
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        return_list = []
        list1 = [i for i in range(1,n+1)]
        for i in range(n):
            if result==target:
                break
            else:
                result.append(list1[i])
                return_list.append('Push')
                if list1[i] in target:
                    continue
                else:
                    result.pop()
                    return_list.append('Pop')
        return return_list
