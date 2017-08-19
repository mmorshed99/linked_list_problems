#Given a sorted linked list, delete all duplicates such that each element appear only once.
#
#For example,
#Given 1->1->2, return 1->2.
#Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
       my_curr = A
       #my_curr_val = A.val
       while(True):
           my_next = my_curr.next
           if my_next == None:
               break
           my_curr_val = my_curr.val
           if my_curr_val == my_next.val:
               my_curr.next = my_next.next
           else:
               my_curr = my_next
       return A    
