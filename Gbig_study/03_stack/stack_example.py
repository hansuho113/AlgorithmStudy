class Stack(list):
    def __init__(self):
        self.stack_list = []

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        else: return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def clear(self):
        return self.stack_list.clear()

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        return False

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.clear())
    print(s.pop)
