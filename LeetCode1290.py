'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = ""
        temp = head
        while(temp!=None):
            result = result+str(temp.val)
            temp = temp.next
        return int(result,2)
