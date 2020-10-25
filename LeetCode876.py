'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/middle-of-the-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        temp = head
        while temp!=None:
            length = length+1
            temp = temp.next
        i = 0
        temp = head
        while i<length//2 and temp:
            temp = temp.next
            i = i+1
        return temp
