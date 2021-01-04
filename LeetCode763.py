'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/partition-labels/
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos = {c:i for i,c in enumerate(S)}
        pos = 0
        j = 0
        ans= []
        for i ,c in enumerate(S):
            j = max(j,last_pos[c])
            if i==j:
                ans.append(i-pos+1)
                pos = i+1
        return ans
