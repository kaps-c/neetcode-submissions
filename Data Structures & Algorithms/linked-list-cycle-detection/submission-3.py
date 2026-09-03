# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # edge cases (either length of 0 or 1)
        if not head: 
            return False

        if not head.next: 
            return False

        # hashmap (brute force solution)

        # initialise pointer and hashmap
        pointer = head
        counter = 0
        hashmap = {}

        # loop
        while pointer:
            if pointer in hashmap:
                return True
            else: 
                counter += 1
                hashmap[pointer] = counter
                pointer = pointer.next
        
        return False




        
        