class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return not self.items

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()


def reverse_string(mystr):

    my_stack = Stack()

    for char in mystr:
        my_stack.push(char)

    reverse_str = ""
    while not my_stack.is_empty():
        reverse_str = reverse_str + my_stack.pop()

    return reverse_str


output = reverse_string("apple")
print(output)