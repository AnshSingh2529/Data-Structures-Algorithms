# Doubly Linked List Implementation in Python

class Node:
   """Node class represents a single node in the doubly linked list"""
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


class DoublyLinkedList:
   """DoublyLinkedList class to manage doubly linked list operations"""
   def __init__(self):
       self.head = None

   def append(self, data):
       """Insert a node at the end of the list"""
       new_node = Node(data)
       if not self.head:
           self.head = new_node
           return
       last = self.head
       while last.next:
           last = last.next
       last.next = new_node
       new_node.prev = last

   def prepend(self, data):
       """Insert a node at the beginning of the list"""
       new_node = Node(data)
       if not self.head:
           self.head = new_node
           return
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node

   def insert_at_position(self, data, position):
       """Insert a node at a specific position (1-indexed)"""
       if position == 1:
           self.prepend(data)
           return
       
       new_node = Node(data)
       current = self.head
       
       for i in range(position - 2):
           if current is None or current.next is None:
               print("Position out of range")
               return
           current = current.next
       
       if current is None:
           print("Position out of range")
           return
       
       new_node.next = current.next
       new_node.prev = current
       
       if current.next:
           current.next.prev = new_node
       current.next = new_node

   def delete(self, key):
       """Delete a node by its data value"""
       current = self.head
       while current:
           if current.data == key:
               if current.prev:
                   current.prev.next = current.next
               if current.next:
                   current.next.prev = current.prev
               if current == self.head:  # Move head if needed
                   self.head = current.next
               return True
           current = current.next
       return False

   def delete_at_position(self, position):
       """Delete a node at a specific position (1-indexed)"""
       if position == 1:
           if self.head:
               self.head = self.head.next
               if self.head:
                   self.head.prev = None
               return True
           return False
       
       current = self.head
       for i in range(position - 1):
           if current is None:
               return False
           current = current.next
       
       if current is None:
           return False
       
       if current.prev:
           current.prev.next = current.next
       if current.next:
           current.next.prev = current.prev
       
       return True

   def search(self, key):
       """Search for a node by its data value"""
       current = self.head
       while current:
           if current.data == key:
               return True
           current = current.next
       return False

   def get_length(self):
       """Get the length of the doubly linked list"""
       count = 0
       current = self.head
       while current:
           count += 1
           current = current.next
       return count

   def get_element_at_position(self, position):
       """Get the element at a specific position (1-indexed)"""
       current = self.head
       for i in range(position - 1):
           if current is None:
               return None
           current = current.next
       return current.data if current else None

   def display(self):
       """Display the list in forward direction"""
       elements = []
       current = self.head
       while current:
           elements.append(current.data)
           current = current.next
       return elements

   def display_reverse(self):
       """Display the list in reverse direction"""
       elements = []
       current = self.head
       if not current:
           return elements
       while current.next:
           current = current.next
       while current:
           elements.append(current.data)
           current = current.prev
       return elements

   def traverse_forward(self):
       """Traverse and print the list in forward direction"""
       current = self.head
       while current:
           print(current.data, end=" <-> ")
           current = current.next
       print("None")

   def traverse_backward(self):
       """Traverse and print the list in backward direction"""
       current = self.head
       if not current:
           print("None")
           return
       while current.next:
           current = current.next
       while current:
           print(current.data, end=" <-> ")
           current = current.prev
       print("None")

   def clear(self):
       """Clear the entire doubly linked list"""
       self.head = None

   def reverse_list(self):
       """Reverse the doubly linked list"""
       if not self.head or not self.head.next:
           return
       
       current = self.head
       while current:
           current.prev, current.next = current.next, current.prev
           current = current.prev
       self.head = self.head.next if self.head else None


# Example usage:
if __name__ == "__main__":
   # Create a new doubly linked list
   dll = DoublyLinkedList()
   
   # Append elements
   print("=== Appending Elements ===")
   dll.append(10)
   dll.append(20)
   dll.append(30)
   print("List after appending 10, 20, 30:")
   dll.traverse_forward()
   
   # Prepend elements
   print("\n=== Prepending Elements ===")
   dll.prepend(5)
   dll.prepend(1)
   print("List after prepending 5, 1:")
   dll.traverse_forward()
   
   # Insert at position
   print("\n=== Inserting at Position ===")
   dll.insert_at_position(15, 3)
   print("List after inserting 15 at position 3:")
   dll.traverse_forward()
   
   # Display list
   print("\n=== Display Methods ===")
   print("Forward:", dll.display())
   print("Reverse:", dll.display_reverse())
   
   # Search operation
   print("\n=== Search Operation ===")
   print(f"Search for 15: {dll.search(15)}")
   print(f"Search for 100: {dll.search(100)}")
   
   # Get length
   print("\n=== List Length ===")
   print(f"Length of list: {dll.get_length()}")
   
   # Get element at position
   print("\n=== Get Element at Position ===")
   print(f"Element at position 3: {dll.get_element_at_position(3)}")
   
   # Delete by value
   print("\n=== Delete by Value ===")
   dll.delete(15)
   print("List after deleting 15:")
   dll.traverse_forward()
   
   # Delete at position
   print("\n=== Delete at Position ===")
   dll.delete_at_position(2)
   print("List after deleting at position 2:")
   dll.traverse_forward()
   
   # Traverse backward
   print("\n=== Backward Traversal ===")
   dll.traverse_backward()
   
   # Reverse the list
   print("\n=== Reverse the List ===")
   dll.reverse_list()
   print("List after reversing:")
   dll.traverse_forward()
   
   # Clear the list
   print("\n=== Clear the List ===")
   dll.clear()
   print("List after clearing:")
   print("Forward:", dll.display())
   print("List is empty:", dll.get_length() == 0)   
