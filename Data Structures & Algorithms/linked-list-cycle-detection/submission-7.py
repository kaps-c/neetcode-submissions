# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # edge cases (either length of 0 or 1) -> NOT NEEDED loop handles it

        # hashmap (brute force solution)
        # initialise pointer and hashmap -> CLEANER VERSION, COUNT REDUNDANT
        pointer = head
        hashmap = set()

        # loop
        while pointer:
            if pointer in hashmap:
                return True
            else: 
                hashmap.add(pointer)
                pointer = pointer.next
        
        return False
        