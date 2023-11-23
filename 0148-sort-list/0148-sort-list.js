/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    if (!head || !head.next) {
        return head;
    }

    let valArr = [];
    let current = head;
    while (current) {
        valArr.push(current.val);
        current = current.next;
    }

    valArr.sort((a, b) => a - b);

    current = head;
    for (let i = 0; i < valArr.length; i++) {
        current.val = valArr[i];
        current = current.next;
    }

    return head;
};