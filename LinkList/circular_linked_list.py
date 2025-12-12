# Circular Linked List in Data structure


class Node:
    """Node class represents a single node in the circular linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    """CircularLinkedList class to manage circular linked list operations"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        """Insert a node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        #   Insertion
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail.next = new_node
        self.tail = new_node

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return

        #  Insertion
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail.next = new_node
        self.head = new_node

    def traverse_forward(self):
        """Traverse and print the list in forward direction"""
        if not self.head:
            print("None")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")

    def traverse_backward(self):
        """Traverse and print the circular list in backward direction"""
        if not self.tail:
            print("None")
            return
        current = self.tail
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.tail:
                break
        print("HEAD")

    def delete(self, data):
        if not self.head:
            print("Sorry! No node present.")
            return

        current = self.head
        while True:
            if current.data == data:

                #  Case1: single element
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    print("successfully deleted single node!!")
                    return

                #  Case2: head node
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                    self.head.prev = self.tail

                # Case3: tail node
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

                # Case4: Delete middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return
            current = current.next
            if current == self.head:
                break

    def search(self, data):
        """Search for a node by its data value"""
        current = self.head
        while True:
            if current.data == data:
                print("Element Found")
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get_list_lenght(self):
        """Get the length of the circular linked list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def get_element_at_position(self, position):
        """Get the element at a specific position (1-indexed)"""
        current = self.head
        for i in range(position - 1):
            if current is None:
                return None
            current = current.next
            if current == self.head:
                break
        return current.data if current else None


if __name__ == "__main__":
    cll = CircularLinkedList()

    # Append elements
    print("=== Insert at the End Elements ===")
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_end(40)
    cll.insert_at_end(50)
    print("List after appending node")
    cll.traverse_forward()
    print("\n")
    #  Prepend elements
    print("=== Prepending Elements === ")
    cll.insert_at_beginning(0)
    print("List after prepending node")
    cll.traverse_forward()
    print("\n")
    #   Traverse Backward
    cll.traverse_backward()
    print("\n")

    #  Delete a Node
    cll.delete(8)  # Delete by Value
    cll.traverse_forward()
    print("\n")

   # Search operation
    print("\n=== Search Operation ===")
    print(f"Search for 30: {cll.search(30)}")
    print(f"Search for 100: {cll.search(100)}")

   # Get length
    print("\n=== List Length ===")
    print(f"Length of list: {cll.get_list_lenght()}")

   # Get element at position
    print("\n=== Get Element at Position ===")
    print(f"Element at position 3: {cll.get_element_at_position(3)}")