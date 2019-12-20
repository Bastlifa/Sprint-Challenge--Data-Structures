from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() < self.capacity:
            self.current = self.storage.head
            self.storage.add_to_tail(item)
        else:
            self.current.value = item
            if self.current is not self.storage.tail:
                self.current = self.current.next
            else:
                self.current = self.storage.head
            
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        cur = self.storage.head
        for _ in range(self.storage.__len__()):
            if cur.value is not None:
                list_buffer_contents.append(cur.value)
            cur = cur.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for _ in range(capacity)]
        self.cur = 0

    def append(self, item):
        self.storage[self.cur] = item
        if self.cur < len(self.storage) - 1:
            self.cur += 1
        else:
            self.cur = 0

    def get(self):
        return [a for a in self.storage if a is not None]
