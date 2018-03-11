#Sort a linked list using insertion sort.
#
#We have explained Insertion Sort at Slide 7 of Arrays
#
#Insertion Sort Wiki has some details on Insertion Sort as well.
#
#Example :
#
#Input : 1 -> 3 -> 2
#
#Return 1 -> 2 -> 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        length = 0
        curr = A
        while(curr != None):
            curr = curr.next
            length += 1
        save_len = length
        global_curr = A
        curr = A
        mymin = sys.maxint
        temp = ListNode(sys.maxint)
        tempprev = None
        currprev = None
        append = A
        appendprev = None
        while(length != 0):
            while(curr != None):
                #print(curr.val)
                if curr.val < mymin:
                    temp = curr
                    mymin = curr.val
                    tempprev = currprev
                currprev = curr
                curr = curr.next
            if temp != append:
                tempprev.next = temp.next
                temp.next = append
                if length != save_len:
                    appendprev.next = temp
                #append.next = temp
            append = temp.next
            tempprev = temp
            currprev = temp
            appendprev = temp
            curr = temp.next
            mymin = sys.maxint
            if length == save_len:
                return_node = temp
            length -= 1
        return return_node
