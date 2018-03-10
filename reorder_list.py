# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A == None or A.next == None:
            return A
        i = ListNode(1)
        i = A
        while(True):
            if i == None or i.next == None:
                break
            j = ListNode(1)
            j = i.next
            if j.next == None:
                break
            while(True):
                k = j.next
                if k.next == None:
                    break
                j = k
                k = k.next
            k.next = i.next
            i.next = k
            j.next = None
            i=i.next
            i = i.next
        return A
