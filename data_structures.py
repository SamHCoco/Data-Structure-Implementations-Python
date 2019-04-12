
# ------------------------------------------ STACK -----------------------------------------------------


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

    def is_empty(self):
        """Determines whether stack is empty.

        returns: True if stack is empty, false if it is not
        """
        if len(self.stack) == 0:
            print("THIS STACK IS EMPTY")
            return True
        else:
            return False

    def print(self):
        """Displays the stack to the user."""
        print("STACK: {}".format(self.stack))

    def size(self):
        """Returns the number of element in the stack.

        returns: The number of elements in stack, or 0 if stack is empty.
        """
        if self.is_empty():
            return 0
        else:
            return len(self.stack)

# ------------------------------------------ QUEUE -----------------------------------------------------


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

    def is_empty(self):
        """Determines whether the queue is empty (0 elements).

        returns: True if queue has elements, false otherwise"""
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the number of elements in the queue.

        returns: The number of elements in the queue
        """
        return len(self.queue)

    def print(self):
        """Displays the queue to the user"""
        print("QUEUE: {}".format(self.queue))

# ------------------------------------------ LINKEDLIST -----------------------------------------------------


class LinkedList:

    class Node:

        def __init__(self, data=None):
            self.data = data
            self.node = None

    def __init__(self):
        self.head = self.Node()

    def add(self, element):
        """Adds an element to the linkedlist.

        args:
        element - the element to be added to linkedlist"""
        # adding first element to the list
        if self.head.data is None:
            self.head.data = element
            self.head.node = self.Node()
        else:
            # when head node already has data
            current_node = self.head.node
            while current_node is not None:
                if current_node.node is None:
                    current_node.data = element
                    current_node.node = self.Node()
                    break
                else:
                    current_node = current_node.node

    def print(self):
        """Displays the values of the linkedlist to the user."""
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                print("{}| ".format(current_node.data), end='')
                current_node = current_node.node


