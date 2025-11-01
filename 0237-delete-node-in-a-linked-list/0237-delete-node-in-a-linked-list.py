# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # temp = node
        # prev = temp
        # while temp and temp.next:
        #     temp.val=temp.next.val
        #     prev = temp
        #     temp=temp.next
        # prev.next = None
        # # while node.next:
        # #     node.val=node.next.val
        # #     node=node.next
        # # node.next=None
        node.val = node.next.val
        node.next = node.next.next
        