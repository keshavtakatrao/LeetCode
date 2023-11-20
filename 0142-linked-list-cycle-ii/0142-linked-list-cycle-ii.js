/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
     let ref = new Set()
     let current = head
    while(current && current.next){
        if(ref.has(current)){
            return current
        }
        ref.add(current)
        current = current.next
    }
    
    return null
};