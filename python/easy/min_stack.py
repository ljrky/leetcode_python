class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,x):
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        item = self.stack.pop()
        if item == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

test = MinStack()
print(test.push(0))
print(test.push(1))
print(test.push(0))


print(test.getMin())
print(test.pop())
print(test.getMin())
print(test.stack)
print(test.minStack)


