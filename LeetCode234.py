'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/palindrome-linked-list/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        result = []
        temp = head
        while temp:
            result.append(temp.val)
            temp = temp.next
        result1 = result.copy()
        result1.reverse()
        return result==result1
