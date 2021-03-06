"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage
   structure. Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure. Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement
         the Queue? What would that look like? How many Stacks would you need?
         Try it!
"""

from sys import path

path.append("../")
from singly_linked_list.singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.__storage = LinkedList()

    def __len__(self):
        return self.length

    @property
    def length(self):
        return len(self.__storage)

    def enqueue(self, value):
        # print(f"Q: enqueueing value '{value}' to queue")
        self.__storage.add_to_tail(value)

    def dequeue(self):
        output = self.__storage.remove_head()
        # print(f"Q: dequeueing value '{output}' from queue")
        return output
