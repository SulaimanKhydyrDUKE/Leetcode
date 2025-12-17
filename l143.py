# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        map = {}
        p = head
        i = 0
        while p:
            map[i] = p
            p = p.next
            i+=1
        count = 0
        arr = list(map.values())
        l, r = 0, len(arr)-1
        dummy = head
        while count<i and l<r:
            arr[l].next = arr[r]
            arr[r].next = arr[l+1]
            dummy = arr[r]
            
            count+=2
            if r-1== l+1:
                dummy = dummy.next
            l+=1
            r-=1
        dummy.next = None
            
        
