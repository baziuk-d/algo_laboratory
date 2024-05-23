class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.head:
            self.head = new_node

        elif self.head.priority < priority:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next

            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    def remove_highest_priority(self):
        if not self.head:
            return None
        else:
            highest = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None

            return highest.value

    def view_queue(self):
        current = self.head
        while current:
            print(f" value: {current.value}, priority: {current.priority}")
            current = current.next


list = PriorityQueue()

list.insert("a",15)
list.insert("b",5)
list.insert("c",10)
list.insert("d",20)

print("all list:")
list.view_queue()

list.insert("g",30)
print("list after insert new element:")
list.view_queue()