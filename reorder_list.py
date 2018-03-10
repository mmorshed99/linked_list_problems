# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Method 1: Simplest one
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
    #Method 2: Better one
    def reorderList(self, A):
        if A == None or A.next == None:
            return A
        temp = A.next
        if temp == None or temp.next == None:
            return A
        mylist = []
        p = A
        while(True):
            mylist.append(p)
            p = p.next
            if p == None:
                break
        t = 0
        q = mylist[t]
        n = len(mylist) - 1
        while(True):
            q = mylist[t]
            mylist[n].next = q.next
            q.next = mylist[n]
            n = n-1
            t = t + 1
            if t == n:
                mylist[t].next = None
                break
            if t + 1 == n:
                mylist[t+1].next = None
                break
        return A
    #Method 3: Best one: https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/
