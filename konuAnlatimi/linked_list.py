class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=str(nodes.pop(0)))  # Veriyi str() ile dizeye dönüştürün
            self.head = node
            for elem in nodes:
                node.next = Node(data=str(elem))  # Veriyi str() ile dizeye dönüştürün
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self) -> None:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node

                return
        raise Exception("Node with data '%s' not found" %target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            
            previous_node = node

        raise Exception("Node with data '%s' not found" %target_node_data)


class Node:
    def __init__(self, data) -> None:
         self.data = data
         self.next = None
    
    def __repr__(self) -> str:
        return self.data # Veriyi str() ile dizeye dönüştürün

data_list = [1,23,45]
my_linked_list = LinkedList(data_list)
print(my_linked_list)  # Çıktı: 1 -> 2 -> 3 -> 4 -> 5 -> None
my_linked_list.add_first(Node("9"))
print(my_linked_list)
my_linked_list.add_last(Node("9"))
my_linked_list.add_after("23" , Node("2"))
print(my_linked_list)
my_linked_list.remove_node("45")
print(my_linked_list)