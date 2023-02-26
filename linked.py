class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
llist = LinkedList()

first_node = node("a")
llist.head = first_node
second_node = node("b")
third_node = node("c")

first_node.next = second_node
second_node.next = third_node
print(llist)
