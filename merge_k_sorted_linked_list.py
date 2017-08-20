#Merge k sorted linked lists and return it as one sorted list.
#
#Example :
#
#1 -> 10 -> 20
#4 -> 11 -> 13
#3 -> 8 -> 9
#will result in
#
#1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        #B = ListNode()
        count = 0
        for i in range(0,len(A)):
            current_node = A[i]
            count += 1
            while (current_node.next != None):
                count += 1
                current_node = current_node.next
        curr_nodes = []
        for i in range(0,len(A)):
            curr_nodes.append(A[i])
        curr_max = 9999999
        curr_id = -1
        for i in range(0,len(A)):
            if curr_nodes[i].val < curr_max:
              curr_max = curr_nodes[i].val
              curr_id = i
        my_return_node = curr_nodes[curr_id]
        my_current_node = my_return_node
        curr_nodes[curr_id] = curr_nodes[curr_id].next
        count = count-1
        while(count>0):
            curr_max = 9999999
            curr_id = -1
            for i in range(0,len(A)):
                if curr_nodes[i] != None and curr_nodes[i].val < curr_max:
                    curr_max = curr_nodes[i].val
                    curr_id = i
            if my_current_node != None:        
               my_current_node.next = curr_nodes[curr_id]
            my_current_node = curr_nodes[curr_id]
            if curr_nodes[curr_id] != None:
              curr_nodes[curr_id] = curr_nodes[curr_id].next
            #my_current_node = curr_nodes[curr_id]    
            count = count-1
        return my_return_node
