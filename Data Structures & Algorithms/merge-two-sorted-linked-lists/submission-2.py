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

        # get head first
        nxt = ListNode()

        if l.val <= r.val:
            nxt.val = l.val
            l = l.next

        else:
            nxt.val = r.val
            r = r.next
            
        head = ListNode(nxt.val, None)
        curr = head

        # while loop while they're both not empty
        while l and r:
            nxt = ListNode()

            if l.val <= r.val:
                nxt.val = l.val
                l = l.next

            else:
                nxt.val = r.val
                r = r.next
                
            curr.next = nxt
            curr = nxt

        while l:
            nxt = ListNode()
            nxt.val = l.val
            l = l.next
            curr.next = nxt
            curr = nxt

        while r:
            nxt = ListNode()
            nxt.val = r.val
            r = r.next
            curr.next = nxt
            curr = nxt

        return head

            














        