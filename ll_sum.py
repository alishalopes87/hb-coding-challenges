# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse order and 
# each of their nodes contain a single digit. Add the two numbers and 
# return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp 


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


ll1 = LinkedList()
ll2 = LinkedList()

ll1.add(2)
ll1.add(4)
ll1.add(3)

ll2.add(5)
ll2.add(6)
ll2.add(4)

def addTwoNumbers(ll1, ll2):
    result = LinkedList()

    current1 = ll1.head
    current2 = ll2.head

    while current1 and current2:
        item = current1.data + current2.data 
        result.add(item)
        current1 = current1.next
        current2 = current2.next 

    current = result.head
    while current:
        print(current.data)
        current = current.next
     
print(addTwoNumbers(ll1,ll2))
