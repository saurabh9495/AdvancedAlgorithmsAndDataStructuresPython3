# push(element)
# pop()
# peek()
# is_empty()
# size()

class Stack:
    def __init__(self) -> None:
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, data):
        self.stack_list.append(data)
        return True

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


stk = Stack()
print(stk.is_empty())
print(stk.peek())
print(stk.size())
for i in range(0, 5):
    print(i)
    stk.push(i)
print(stk.pop())
