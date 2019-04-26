
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

    def is_index_valid(self, index):
        """Checks whether an index is valid.

        returns: true if index valid, false otherwise
        """
        if 0 <= index <= self.size - 1:
            return True
        else:
            return False

    def is_empty(self):
        """Checks whether linkedlist is empty.

        returns: true if linkedlist is empty, false otherwise
        """
        if self.size == 0:
            return True
        else:
            return False

    def __str__(self):
        """Displays the linkedlist to the user.

        returns: the linkedlist as a string list
        """
        linked_list = ""
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                linked_list = linked_list + str(current_node.data) + ", "
                current_node = current_node.node
            linked_list = linked_list[:len(linked_list) - 2]
            return "LINKEDLIST: " + "[" + linked_list + "]"


class BinarySearchTree:

    class Node:

        def __init__(self, data=None):
            self.left_child = None
            self.data = data
            self.right_child = None

    def __init__(self, data):
        # creates initial root node and sets root node value
        if type(data) in (int, float):
            self.root = self.Node(data)
        else:
            print("BST INSERTION ERROR: {} is non-numeric".format(data))

    def insert(self, data):
        """Inserts data value into the Binary Search Tree.

        args:
        data - the number to be inserted into the tree
        """
        current_node = self.root
        inserted = False
        while not inserted:
            if data > current_node.data and current_node.right_child is None:
                current_node.right_child = self.Node(data)
                inserted = True
            elif data < current_node.data and current_node.left_child is None:
                current_node.left_child = self.Node(data)
                inserted = True
            elif data == current_node.data and current_node.left_child is None:
                current_node.left_child = self.Node(data)
                inserted = True
            elif data > current_node.data and current_node.right_child is not None:
                current_node = current_node.right_child
            elif data < current_node.data and current_node.left_child is not None:
                current_node = current_node.left_child

