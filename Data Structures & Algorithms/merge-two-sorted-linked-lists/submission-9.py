# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Case 1: if both are empty
        if (list1 is None) and (list2 is None):
            return None
        
        # Case 2: if one of the lists is empty
        if (list1 is None):
            return list2

        if (list2 is None):
            return list1

        # Case 3: both lists are not empty - use 2 pointer

        # initialise merged list and pointers
        l, r = list1, list2

        # dummy head
        dummy = ListNode()
        curr = dummy

        # while loop while they're both not empty
        while l and r:

            if l.val <= r.val:
                curr.next = l
                l = l.next

            else:
                curr.next = r
                r = r.next
                
            curr = curr.next

        while l:
            curr.next = l
            l = l.next
            curr = curr.next

        while r:
            curr.next = r
            r = r.next
            curr = curr.next

        return dummy.next
