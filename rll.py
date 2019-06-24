class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    if not head:
        return head
    cur = head
    while cur.next:
        head, cur.next.next, cur.next = cur.next, head, cur.next.next
    return head

reverseList([1,2,3,4,5])