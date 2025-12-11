# LinkedList Data Structure - User defined Data Structure

## Overview

- DEFINITION
  - A linked list is a linear data structure where elements, called nodes, are stored in a sequence.
  - Each node contains data and a reference (or link) to the next node in the sequence.
  - Unlike arrays, linked lists do not require contiguous memory allocation.

### Agenda of Linked List

- Introduction
- Perform CRUD operations
- Types of Linked List - Singly, Doubly, Circular
- Fast and slow pointer approach
- practise problems

#### Introduction

- What is Linked List?
  - A linked list is basically chains of nodes where each node contains data and a pointer to the next node in the sequence.

- Why Linked List?
  - Dynamic Size: Linked lists can grow and shrink in size as needed, making them more flexible than arrays.

  - Efficient Insertions/Deletions: Adding or removing elements from a linked list is generally more efficient than in an array, especially for large datasets.

#### Perform CRUD operations

- Create a Linked List
  - To create a linked list, we define a node structure and initialize the head pointer to null.  

   please see the file: `{LinkList/crud.py/}`

#### Types of Linked List

- Singly Linked List

  - In a singly linked list, each node contains data and a pointer to the next node. Traversal is done in one direction, from the head to the tail.

   please see the file: `{LinkList/crud.py/}`

- Doubly Linked List
  - In a doubly linked list, each node contains data, a pointer to the next node, and a pointer to the previous node. This allows for traversal in both directions.

    please see the file: `{LinkList/doubly_linked_list.py/}`

- Circular Linked List
  - In a circular linked list, the last node points back to the first node, forming a circular structure. This can be implemented in both singly and doubly linked lists.

    please see the file: `{LinkList/circular_linked_list.py/}`
