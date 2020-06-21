'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
'''
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and queryTime<=endTime[i]:
                count=count+1
        return count
