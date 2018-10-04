#Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
#For example:
#Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
#return 1->4->3->2->5->NULL.
#
# Note:
#Given m, n satisfy the following condition:
#1 ≤ m ≤ n ≤ length of list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if A == None:
            return A
        if A.next == None:
            return A
        prev = None
        curr = A
        nxt = ListNode(1)
        count = 1
        while(count != B):
            count += 1
            prev = curr
            curr = curr.next
        start = curr
        prev_start = prev
        while(curr != None and count != C+1):
            count += 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        start.next = curr
        if prev_start != None:
            prev_start.next = prev
        if B == 1:
            return prev
        return A
