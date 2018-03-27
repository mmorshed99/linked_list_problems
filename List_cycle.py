#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
#Try solving it using constant additional space.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Input : 
#
#                  ______
#                 |     |
#                 \/    |
#        1 -> 2 -> 3 -> 4
#
#Return the node corresponding to node 3. 
class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A == None or A.next == None:
            return None
        x = ListNode(1)
        x = A
        x_adv = ListNode(1)
        x_adv = A
        while(x != None and x_adv != None):
            x = x.next
            if x_adv.next != None:
                x_adv = x_adv.next
                x_adv = x_adv.next
            else:
                return None
            if x == x_adv:
                break
        if x == None or x_adv == None:
            return None
        x_find = ListNode(1)
        x_find = A
        while(x_find != x): # x_adv didn't travel non-loop distance 2nd time, that would be the difference
            x = x.next
            x_find = x_find.next
        return x_find
