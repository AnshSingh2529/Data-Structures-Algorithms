# Create a Linked List and perform CRUD operations

class Node:
   """Node class represents a single node in the linked list"""
   def __init__(self, data):
      self.data = data
      self.next = None


class LinkedList:
   """LinkedList class to manage linked list operations"""
   def __init__(self):
      self.head = None

   def traverse(self):
      """Traverse and print all nodes in the linked list"""
      current = self.head
      while current is not None:
         print(current.data, end=" -> ")
         current = current.next
      print("None")

   def insert_at_beginning(self, data):
      """Insert a node at the beginning of the linked list"""
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

   def insert_at_end(self, data):
      """Insert a node at the end of the linked list"""
      new_node = Node(data)
      
      if self.head is None:
         self.head = new_node
         return
      
      current = self.head
      while current.next is not None:
         current = current.next
      current.next = new_node

   def insert_at_position(self, data, position):
      """Insert a node at a specific position (1-indexed)"""
      if position == 1:
         self.insert_at_beginning(data)
         return
      
      new_node = Node(data)
      current = self.head
      
      for i in range(position - 2):
         if current is None:
            print("Position out of range")
            return
         current = current.next
      
      if current is None:
         print("Position out of range")
         return
      
      new_node.next = current.next
      current.next = new_node

   def delete_head(self):
      """Delete the head node"""
      if self.head is None:
         print("Linked list is empty")
         return
      
      self.head = self.head.next

   def delete_last(self):
      """Delete the last node"""
      if self.head is None:
         print("Linked list is empty")
         return
      
      if self.head.next is None:
         self.head = None
         return
      
      current = self.head
      while current.next.next is not None:
         current = current.next
      current.next = None

   def delete_at_position(self, position):
      """Delete a node at a specific position (1-indexed)"""
      if self.head is None:
         print("Linked list is empty")
         return
      
      if position == 1:
         self.delete_head()
         return
      
      current = self.head
      for i in range(position - 2):
         if current is None or current.next is None:
            print("Position out of range")
            return
         current = current.next
      
      if current.next is None:
         print("Position out of range")
         return
      
      current.next = current.next.next

   def get_node_at_position(self, position):
      """Get the node data at a specific position (1-indexed)"""
      current = self.head
      for i in range(position - 1):
         if current is None:
            return None
         current = current.next
      return current.data if current is not None else None


# Demonstration of LinkedList operations
if __name__ == "__main__":
   # Create a new linked list
   linked_list = LinkedList()
   
   # Insert nodes at the end to build initial list: 1 -> 2 -> 3
   linked_list.insert_at_end(1)
   linked_list.insert_at_end(2)
   linked_list.insert_at_end(3)
   
   print("Initial Linked List:")
   linked_list.traverse()
   
   # Insert at the beginning
   print("\nInserting 0 at the beginning:")
   linked_list.insert_at_beginning(0)
   linked_list.traverse()
   
   # Insert at the end
   print("\nInserting 5 at the end:")
   linked_list.insert_at_end(5)
   linked_list.traverse()
   
   # Insert at a specific position (position 3)
   print("\nInserting 6 at position 3:")
   print(f"Node at position 3 before insertion: {linked_list.get_node_at_position(3)}")
   linked_list.insert_at_position(6, 3)
   linked_list.traverse()
   
   # Delete head node
   print("\nDeleting head node:")
   linked_list.delete_head()
   linked_list.traverse()
   
   # Delete last node
   print("\nDeleting last node:")
   linked_list.delete_last()
   linked_list.traverse()
   
   # Delete node at a specific position
   print("\nDeleting node at position 1:")
   linked_list.delete_at_position(1)
   linked_list.traverse()