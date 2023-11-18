/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let ref = new Set()
     let current = head
    while(current && current.next){
        if(ref.has(current)){
            return true
        }
        ref.add(current)
        current = current.next
    }
    
    return false
};