# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if A == None and B!= None:
            return B
        if B == None and A != None:
            return A
        curr_a = A
        curr_b = B
        tot = ListNode(0)
        curr_t = tot
        carry = 0
        while(curr_a != None and curr_b != None):
            curr_t.val = (curr_a.val + curr_b.val + carry) % 10
            carry = (curr_a.val + curr_b.val + carry) / 10
            curr_a = curr_a.next
            curr_b = curr_b.next
            temp = ListNode(0)
            curr_t.next = temp
            prev = curr_t
            curr_t = curr_t.next
            if curr_a == None and curr_b == None:
                if carry != 0:
                    curr_t.val = carry
                    break
                else:
                    prev.next = None
                    break
            if curr_a == None:
                while(curr_b != None):
                    curr_t.val = (curr_b.val + carry) % 10
                    carry = (curr_b.val + carry) / 10
                    curr_b = curr_b.next
                    temp = ListNode(0)
                    curr_t.next = temp
                    prev = curr_t
                    curr_t = curr_t.next
                if carry == 0:
                    prev.next = None
                else:
                    curr_t.val = carry
                break
            elif curr_b == None:
                while(curr_a != None):
                    curr_t.val = (curr_a.val + carry) % 10
                    carry = (curr_a.val + carry) / 10
                    curr_a = curr_a.next
                    temp = ListNode(0)
                    curr_t.next = temp
                    prev = curr_t
                    curr_t = curr_t.next
                if carry == 0:
                    prev.next = None
                else:
                    curr_t.val = carry
                break
        return tot
