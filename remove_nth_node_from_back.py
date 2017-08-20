#Given a linked list, remove the nth node from the end of list and return its head.
#
#For example,
#Given linked list: 1->2->3->4->5, and n = 2.
#After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
#* If n is greater than the size of the list, remove the first node of the list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        numnodes = 1
        curr_node = A
        index_remove = 1
        while(True):
            if curr_node.next == None:
                break
            else:
                numnodes += 1
                curr_node = curr_node.next
        elem_index = numnodes - B + 1
        if elem_index > 0:
            index_remove = elem_index
        curr_node = A
        index_count = 1
        if index_remove == 1:
            return A.next
        index_count += 1    
        while(True):
            if index_count == index_remove:
                node_to_remove = curr_node.next
                node_to_append = node_to_remove.next
                curr_node.next = node_to_append
                break
            curr_node = curr_node.next
            index_count += 1
        return A
