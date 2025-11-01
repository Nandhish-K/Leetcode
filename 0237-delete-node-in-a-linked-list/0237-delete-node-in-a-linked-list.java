/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // ListNode temp = node;
        // ListNode prev = temp;
        // while (temp != null && temp.next != null){
        //     temp.val = temp.next.val;
        //     temp = temp.next;
        //     prev = temp;
        // }
        // prev.next = null;
        node.val = node.next.val;
        node.next = node.next.next;
    }
}