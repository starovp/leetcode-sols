"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Runtime: 44 ms, faster than 97.55% of Python online submissions for Add Two Numbers.
    # Memory Usage: 11.9 MB, less than 49.26% of Python online submissions for Add Two Numbers.
    def addTwoNumbers(self, l1, l2):
        # l1: ListNode
        # l2: ListNode
        # return: ListNode
        
        init = x = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            x.next = ListNode(carry%10)
            x = x.next
            carry //= 10
        return init.next

if __name__ == '__main__':
    solution = Solution()

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    g = solution.addTwoNumbers(l1, l2)
    while g:
        print("Value",g.val)
        print("Next", g.next)
        g = g.next
        
    #------
        
    l1 = ListNode(5)
    l2 = ListNode(5)
    g = solution.addTwoNumbers(l1, l2)
    while g:
        print("Value",g.val)
        print("Next", g.next)
        g = g.next
    
            
        
