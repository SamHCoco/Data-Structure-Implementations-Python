# Data Structures: Python Implementations

## Content Overview:
Below is an overview of some Abstract Data Types (ADTs) and my implementations of them using Python, including a summary of their worst case Time Complexities.

## Introduction:
Data structures provide ways of storing and organizing data in computer memory and fall into two broad categories: Linear and Non-Linear.

## Linear Data Structures:

* ## Queue
Queues are a collection (or sequence) type data structure, meaning they hold collections of objects, organized along the **First-In-First-Out (F.I.F.O)** principle. The element at the front of the queue is the one that is returned. This happens successively until the last element is extracted from the back of the queue, similar to how human queues for customer service operate.
**Queues have 2 defining methods**:  

 * **enqueue(e)** - Adds element e the back of the queue.
 * **dequeue()** - Returns and removes the element currently at the front of the queue.

This implementation of a Queue uses Python's built in *list* data structure.
 ```Python
 class Queue:

     def __init__(self):
         self.queue = []

     def enqueue(self, element):
         """Adds an element to the rear of the queue.

         args:
         element - the element to be added to the back of the queue
         """
         self.queue.append(element)
         self.print()

     def dequeue(self):
         """Removes and returns the element at the front of the queue."""
         result = self.queue[0]
         print("{} REMOVED FROM QUEUE".format(result))
         del self.queue[0]
         self.print()
         return result
 ```

 ### Time Complexity (Worst Case)
 * **Access (dequeue)**:
    * **O(1)** - Constant time if the element being accessed is at the front of the queue.
    * **O(n)** - It takes linear time to access an arbitrary element in the queue that is not at the front of the queue. For example, in the worst case, to access the last element in a queue of *n* elements, the deque operation would have to be applied *n* times.

* **Insertion (enqueue):**
   * **O(1)** - Constant time. A strength of Queues: no matter how large the elements in the queue, inserting any element into a queue will take constant time.  


* ## Stack
Stacks are another collection type data structure but are organized along the **Last-In-First-Out (L.I.F.O)** principle. Akin to a stack of plates, the last element added is the first to be removed from the stack. **Stacks have 2 defining methods**:

 * **push(e)** - Adds element e to the top of the stack.
 * **pop()** - Returns and removes the element at the top of the stack.  

 ```Python
 class Stack:

     def __init__(self):
         self.stack = []

     def push(self, element):
         """Adds an element to the top of the stack and prints the stack.

         args:
         element - The element to be added to stack
         """
         self.stack.append(element)
         self.print()

     def pop(self):
         """Returns and removes the element at the top of the stack and prints stack.

         returns: The element at the top of the stack"""
         rear = len(self.stack) - 1
         if not self.is_empty():
             result = self.stack[rear]
             del self.stack[rear]
             print("\n{} POPPED.".format(result))
             self.print()
             return result
 ```
 ### Time Complexity (Worst Case)
* **Access (pop)**:
    * **O(1)** - Constant time if the element being accessed is at the top of the stack.
    * **O(n)** - It takes linear time to access an arbitrary element not at the top of the stack. For example, in the worst case, to access the last element in a stack of *n* elements, the pop operation would have to be applied *n* times.
* **Insertion (push):**
 * **O(1)** - Constant time. A strength of stacks: no matter how large the stack, adding an element to the top of a stack will always take constant time.  

* ## LinkedList
LinkedLists are data structures made up of **nodes** which contain data and pointers which point to the next node in the data structure. The first node, called the **head-node**, contains the first element while the last node is None (or null) indicating to end of list. **LinkedLists have 4 key methods:**
 * **add(e)** - Adds element *e* to the linkedlist.
 * **get(index)** - Returns the element of the linkedlist at specified index.
 * **search(e)** - Searches the linkedlist for element *e*.
 * **remove(index)** - Removes the element at the specified index from the linkedlist.


 My implementation of the **Singly LinkedList** data structure in Python:
 ```Python
 class LinkedList:

     class Node:

         def __init__(self, data=None):
             self.data = data
             self.node = None

     def __init__(self):
         self.head = self.Node()
         self.size = 0

     def add(self, element):
         """Adds an element to the linkedlist.

         args:
         element - the element to be added to linkedlist"""
         # adding first element to the list
         if self.head.data is None:
             self.head.data = element
             self.size += 1
         else:
             # when head node already has data
             current_node = self.head
             while current_node is not None:
                 if current_node.node is None:
                     current_node.node = self.Node()
                     current_node.node.data = element
                     self.size += 1
                     break
                 else:
                     current_node = current_node.node

     def get(self, index):
         """Returns the element of linkedlist at the specified index.

         returns: element at specified index, or null if list empty or index is invalid
         """
         if self.is_index_valid(index):
             if not self.is_empty():
                 position = 0
                 current_node = self.head
                 while position != index:
                     current_node = current_node.node
                     position += 1
                 print("LinkedList[{}] = {}".format(index, current_node.data))
                 return current_node.data
             else:
                 print("LinkedList Empty")
                 return None
         else:
             print("LinkedList Error: index [{}] invalid".format(index))
             return None

     def remove(self, index):
         """Removes an element of linkedlist at a selected index.

         args:
         index - the position of the element to be removed
         """
         if self.is_empty():
             print("Cannot remove index[{}]: LinkedList empty".format(index))
         elif not self.is_index_valid(index):
             print("ERROR: Index[{}] does not exist".format(index))
         else:
             position = 0
             #  deletes node at start of linkedlist
             if index == 0:
                 self.head = self.head.node
                 self.size -= 1
             #  deletes node at end of linkedlist
             elif index == self.size - 1:
                 current_node = self.head
                 while position < self.size - 2:
                     current_node = current_node.node
                     position += 1
                 current_node.node = None  # deletes the last node
                 self.size -= 1
             else:
                 #  deletes any nodes between start and end
                 current_node = self.head
                 while position != index - 1:
                     current_node = current_node.node
                     position += 1
                 new_node = current_node.node.node
                 del current_node.node
                 current_node.node = new_node
                 self.size -= 1

     def search(self, element):
         """Searches for specified element in linkedlist.

         returns: the index of first element that matches search,
         or null if element not found
         """
         if not self.is_empty():
             current_node = self.head
             index = 0
             found = False
             while not found:
                 if current_node.data == element:
                     print("{} found at index[{}]".format(element, index))
                     found = True
                 else:
                     if current_node.node is not None:
                         current_node = current_node.node
                         index += 1
                     else:
                         print("{} not found".format(element))
                         return None
 ```   
 ### Time Complexity (Worst Case)
* **Access**:
    * **O(n)** - In the worst case, it takes linear time to access an arbitrary element a linkedlist because the nodes have to be traversed to get to the desired element. To reach the last node in a linkedlist of *n* nodes, *n* nodes have to be traversed.
* **Insertion (add):**
   * **O(n)** -  Inserting an element into a linkedlist takes linear time in the time worst case. The insertion itself takes *O(1)* constant time but having to traverse nodes to access the node required to complete the insertion takes *O(n)* linear time.
