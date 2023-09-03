class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

'''
The only information you need to store for a linked list is where the list starts (the head of the list).
'''

class Node:
    def __init__(self,data) -> None:
         self.data = data
         self.next = None
    
    def __repr__(self) -> str:
        return self.data
    
llist = LinkedList()
first_node = Node("a")
llist.head = first_node
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)
