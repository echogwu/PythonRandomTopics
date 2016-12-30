#!/usr/bin/python
#
#Implement a queue using 2 stacks. Specifically, implement the enqueue and dequeue methods.
#This question is good because it shows how well the candidate knows their data structures. It also forces them to write a class with some internal state.
#Solution
#In the constructor, initialize 2 stacks, entryStack and exitStack. The enqueue method pushes the value onto entryStack, the dequeue method pops from exitStack if it's not empty,
#otherwise pop all items from entryStack onto exitStack. If they're both empty throw an exception

class TwoStackAsAQueue:
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def size(self):
            return len(self.items)

        def isEmpty(self):
            return self.size() == 0

        def traverse(self):
            print(self.items)

    def __init__(self):
        self.entryStack = self.Stack()
        self.exitStack = self.Stack()

    def transferFromEntryToExit(self):
        if self.entryStack.size() > 0:
            size = self.entryStack.size()
            for i in range(size):
                self.exitStack.push(self.entryStack.pop())
            return True
        else:
            return False

    def enqueue(self, item):
        self.entryStack.push(item)

    def dequeue(self):
        if not self.exitStack.isEmpty():
            return self.exitStack.pop()
        else:
            if self.transferFromEntryToExit():
                return self.exitStack.pop()
            else:
                raise Exception("empty queue")

    def traverse(self):
        # need to hard copy the exitStack list, otherwise changes on tmp will affect self.exitStack.items itself
        tmp = list(self.exitStack.items)
        tmp.reverse()
        print(tmp+self.entryStack.items)

queue = TwoStackAsAQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.traverse()

queue.dequeue()
queue.traverse()

queue.enqueue(4)
queue.traverse()

queue.dequeue()
queue.traverse()

