"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Runtime: 32 ms, faster than 95.84% of Python3 online submissions for Merge Two Sorted Lists.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
    def mergeTwoLists(self, l1, l2):
        # l1: ListNode
        # l2: ListNode
        # return: ListNode

        # Mark the origin and a traversal node
        place = cur = ListNode(0)

        # While there are elements in both:
        # point the traversal node's next to the 
        # smallest of both, and move that node one
        # forward. Then set our traversal's value
        # to its next.
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # When we finish with either list, since the
        # remaining are sorted we set the traversal's 
        # next pointing to the remaining list.
        cur.next = l1 or l2

        # Finally return the origin incremented by 1
        return place.next

if __name__ == '__main__':
    solution = Solution()

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    g = solution.mergeTwoLists(l1, l2)
    while g:
        print("Value",g.val)
        print("Next", g.next)
        g = g.next
    

