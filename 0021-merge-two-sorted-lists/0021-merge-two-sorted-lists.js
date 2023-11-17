/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let head = new ListNode()
    let p1 = list1
    let p2 = list2
    let headTemp = head
    while(p1!=null || p2!=null){
        if(p1==null){
            head.next = new ListNode(p2.val,null)
            head = head.next
            p2 = p2.next
            continue
        }
        else if(p2==null){
            head.next = new ListNode(p1.val,null)
            head = head.next
            p1 = p1.next 
            continue
        }
        
        if(p1.val >= p2.val){
            head.next = new ListNode(p2.val,null)
            head = head.next
            p2 = p2.next
        }
        else{
            head.next = new ListNode(p1.val,null)
            head = head.next
            p1 = p1.next
        }
    }
    
    return headTemp.next
};