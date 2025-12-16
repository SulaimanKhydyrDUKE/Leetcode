## Swapping pairs in a list - done in linear time and bears 100% by speed
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        pointer = head
        ret = pointer
        if pointer!=None and pointer.next != None:
            ret = pointer.next
        while pointer!=None and pointer.next != None:
            one = pointer
            two = pointer.next
            one.next = two.next
            two.next = one
            if one.next != None and one.next.next != None:
                pointer = one.next
                one.next = one.next.next
            else: 
                break
        return ret

        
