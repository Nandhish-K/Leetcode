# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next :
            if current.next.val in s :
                current.next = current.next.next
            else :
                current = current.next
        return dummy.next
        # l = []
        # current = head 
        # while current :
        #     l.append(current.val)
        #     current = current.next
        # res = []
        # for i in range(len(l)) :
        #     if l[i] not in set(nums) :
        #         res.append(l[i])
        # new_head = ListNode(res[0])
        # current = new_head 
        # for i in range(1,len(res)) :
        #     current.next = ListNode(res[i])
        #     current = current.next
        # return new_head