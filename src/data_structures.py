
# ------------------------------------------ STACK -----------------------------------------------------


class Stack:
    """
    This class implements the Stack Abstract Data Type.

    Attributes
    ----------
    stack (list):  The stack data structure

    Methods
    -------
    push(e): Adds element to stack

    pop(): Removes and returns element at top of stack

    size(): Returns size of stack

    is_empty(): Returns true if stack empty, false otherwise

    print(): Prints the stack
    """

    def __init__(self):
        """Stack constructor."""
        self.stack = []

    def push(self, element):
        """Adds an element to the top of the stack and prints the stack.

        args:
        element - the element to be added to the stack
        """
        self.stack.append(element)
        self.print()

    def pop(self):
        """Returns and removes the element at the top of the stack and prints stack.

        returns: the element at the top of the stack
        """
        rear = len(self.stack) - 1
        if not self.is_empty():
            result = self.stack[rear]
            del self.stack[rear]
            print("\n{} POPPED.".format(result))
            self.print()
            return result

    def is_empty(self):
        """Determines whether stack is empty.

        returns: true if stack is empty, false if it is not
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

        returns: the number of elements in stack, or 0 if stack is empty
        """
        if self.is_empty():
            return 0
        else:
            return len(self.stack)

# ------------------------------------------ QUEUE -----------------------------------------------------


class Queue:
    """
    This class implements the Queue Abstract Data Type.

    Attributes
    ----------
    queue (list): The queue data structure

    Methods
    -------
    enqueue(e): Adds an element to the rear of the queue

    dequeue(): Returns and removes element at front of queue

    is_empty(): Determines whether queue is empty

    size(): Returns number of elements in queue

    print(): Prints the queue
    """

    def __init__(self):
        """Queue constructor."""
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

        returns: true if queue has elements, false otherwise
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the number of elements in the queue.

        returns: the number of elements in the queue
        """
        return len(self.queue)

    def print(self):
        """Displays the queue to the user."""
        print("QUEUE: {}".format(self.queue))

# ------------------------------------------ LINKEDLIST -----------------------------------------------------


class LinkedList:
    """
    This class implements the singly LinkedList Abstract Data Type.

    Attributes
    ----------
    head (Node): The head node of LinkedList
    size (int): The size of the LinkedList

    Methods
    -------
    add(e): Adds node containing element e to LinkedList

    get(i): Returns value of node at index i in LinkedList

    remove(i): Removes node at index i from LinkedList

    search(e): Searches LinkedList for element e

    is_empty(): Checks if the LinkedList is empty

    __str__(): Prints the LinkedList
    """

    class Node:
        """This class implements a node.

        Attributes
        ----------
        data: The data of the node
        node: Pointer to the next node
        """

        def __init__(self, data=None):
            """Node constructor.

            args:
            data: The data of the node
            """
            self.data = data
            self.node = None

    def __init__(self):
        """LinkedList constructor."""
        self.head = self.Node()
        self.size = 0

    def add(self, element):
        """Adds an element to the linkedlist.

        args:
        element - the element to be added to linkedlist
        """
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

        args:
        index (int) - the index of the element to be found

        returns: element at specified index, or null if list empty or index is invalid
        """
        if self._is_index_valid(index):
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
        index (int) - the position of the element to be removed
        """
        if self.is_empty():
            print("Cannot remove index[{}]: LinkedList empty".format(index))
        elif not self._is_index_valid(index):
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

        args:
        element - the element to be found

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

    def _is_index_valid(self, index):
        """Checks whether an index is valid.

        args:
        index (int) - the index value to be validated

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
    """This class implements the Binary Search Tree Abstract Data Type.

    Attributes
    ----------
    data (float/int): The value of a node
    left_child (Node): The left child of a node
    right_child (Node): The right child of a node

    Methods
    -------
    insert(number): Adds number to Binary Search Tree

    search(number): Searches for number in Binary Search Tree

    size(): Determines the number of nodes (size) of the Binary Search Tree.

    preorder_traversal(): Preorder traverses Binary Search Tree and returns result

    inorder_traversal(): Inorder traverses Binary Search Tree and returns result

    postorder_traversal(): Postorder traverses Binary Search Tree and returns result
    """

    class Node:
        """This class implements a node for a BST."""
        def __init__(self, data=None):
            """Node constructor.

            args:
            data (float/int) - the data of the node
            """
            self.left_child = None
            self.data = data
            self.right_child = None

    def __init__(self, data):
        """Binary Search Tree constructor.

        args:
        data (float/int) - root node value
        """
        if BinarySearchTree._is_valid_input(data):
            self.root = self.Node(data)
            self.size = 0
        else:
            print("BST INSERTION ERROR: {} is non-numeric".format(data))

    def insert(self, data):
        """Inserts data value into the Binary Search Tree.

        args:
        data - the number to be inserted into the tree
        """
        if not BinarySearchTree._is_valid_input(data):
            return None

        current_node = self.root
        inserted = False
        while not inserted:
            if data > current_node.data and current_node.right_child is None:
                current_node.right_child = self.Node(data)
                inserted = True
                self.size += 1
            elif data < current_node.data and current_node.left_child is None:
                current_node.left_child = self.Node(data)
                inserted = True
                self.size += 1
            elif data == current_node.data and current_node.left_child is None:
                current_node.left_child = self.Node(data)
                inserted = True
                self.size += 1
            elif data > current_node.data and current_node.right_child is not None:
                current_node = current_node.right_child
            elif data < current_node.data and current_node.left_child is not None:
                current_node = current_node.left_child

    def search(self, search_value):
        """Searches for specified value in the Binary Search Tree.

        args:
        search_value - the value to be found in the Binary Search Tree

        returns: true if the value found, false otherwise, or None if user input invalid
        """
        if not BinarySearchTree._is_valid_input(search_value):
            return None

        current_node = self.root
        found = False
        while not found:
            if current_node.data == search_value:
                found = True
            elif search_value > current_node.data:
                current_node = current_node.right_child
            elif search_value < current_node.data:
                current_node = current_node.left_child
            if current_node is None:
                print("'{}' not found in Binary Search Tree".format(search_value))
                return False
        print("'{}' found in Binary Search Tree".format(search_value))
        return True

    def preorder_traversal(self):
        """Traverses BST in preorder fashion (Root, left, right).

        returns: a list of preorder traversal values
        """
        current_node = self.root
        traverse_values = []  # the values that are read from the traversal
        binary_nodes = []  # 'binary_nodes' are nodes with 2 children
        traversed = False
        counter = 0
        while not traversed:
            if current_node.left_child is not None and current_node.right_child is not None:
                if current_node not in binary_nodes:
                    binary_nodes.append(current_node)
                    traverse_values.append(current_node.data)
                    counter += 1
                    current_node = current_node.left_child
                else:
                    current_node = current_node.right_child
                    binary_nodes.pop()

            elif current_node.right_child is None and current_node.left_child is not None:
                traverse_values.append(current_node.data)
                counter += 1
                current_node = current_node.left_child

            elif current_node.left_child is None and current_node.right_child is not None:
                traverse_values.append(current_node.data)
                counter += 1
                current_node = current_node.right_child

            elif current_node.left_child is None and current_node.right_child is None:
                traverse_values.append(current_node.data)
                counter += 1
                if len(binary_nodes) != 0:
                    current_node = binary_nodes[-1]
            if counter == self.size + 1:
                traversed = True
        print("BST PREORDER TRAVERSAL: {}".format(traverse_values))
        return traverse_values

    def inorder_traversal(self):
        """Traverses the BST in inorder fashion(left, root, right).

        returns: a list of values from inorder traversal
        """
        current_node = self.root
        traverse_values = []  # the values that are read from the traversal
        binary_nodes = []  # 'binary_nodes' are nodes with 2 children
        pop_counter = 0  # counts the nodes which only have one or no children (to be popped)
        pop_counter_array = []  # stores 'pop_counter' values
        traversed_nodes = []  # stores the traversed nodes
        traversed = False
        counter = 0
        while not traversed:
            if current_node.left_child is not None and current_node.right_child is not None:
                if pop_counter != 0:
                    pop_counter_array.append(pop_counter)
                    pop_counter = 0

                if current_node not in binary_nodes:
                    binary_nodes.append(current_node)
                    current_node = current_node.left_child
                else:
                    traverse_values.append(current_node.data)
                    counter += 1
                    current_node = current_node.right_child
                    binary_nodes.pop()

            elif current_node.left_child is not None and current_node.right_child is None:
                traversed_nodes.append(current_node)
                pop_counter += 1
                current_node = current_node.left_child

            elif current_node.left_child is None and current_node.right_child is not None:
                traversed_nodes.append(current_node)
                pop_counter += 1
                current_node = current_node.right_child

            elif current_node.left_child is None and current_node.right_child is None:
                traversed_nodes.append(current_node)
                pop_counter += 1
                pop_counter_array.append(pop_counter)
                pop_counter = 0

                if len(binary_nodes) != 0:
                    current_node = binary_nodes[-1]
                    for i in range(0, pop_counter_array.pop()):
                        traverse_values.append(traversed_nodes.pop().data)
                        counter += 1
                else:
                    # prints final values for inorder traversal
                    while len(pop_counter_array) != 0:
                        for i in range(0, pop_counter_array.pop()):
                            traverse_values.append(traversed_nodes.pop().data)
                            counter += 1
            if counter == self.size + 1:
                traversed = True
        print("BST INORDER TRAVERSAL: {}".format(traverse_values))
        return traverse_values

    def postorder_traversal(self):
        """Traverses Binary Search Tree in postorder fashion.

        returns: a list of values form postorder traversal
        """
        current_node = self.root
        traverse_values = []  # the values that are read from the traversal
        binary_nodes = []  # 'binary_nodes' are nodes with 2 children
        pop_counter = 0  # counts number of subtree nodes to be popped from traversed_nodes
        pop_counter_array = []
        traversed_nodes = []
        traversed = False
        counter = 0
        while not traversed:
            if current_node.left_child is not None and current_node.right_child is not None:
                if pop_counter != 0:
                    pop_counter_array.append(pop_counter)
                    pop_counter = 0

                if current_node not in binary_nodes:
                    binary_nodes.append(current_node)
                    current_node = current_node.left_child
                else:
                    traversed_nodes.append(current_node)
                    pop_counter += 1
                    current_node = current_node.right_child
                    binary_nodes.pop()

            elif current_node.left_child is not None and current_node.right_child is None:
                traversed_nodes.append(current_node)
                pop_counter += 1
                current_node = current_node.left_child

            elif current_node.left_child is None and current_node.right_child is not None:
                traversed_nodes.append(current_node)
                pop_counter += 1
                current_node = current_node.right_child

            elif current_node.left_child is None and current_node.right_child is None:
                traversed_nodes.append(current_node)
                pop_counter += 1
                pop_counter_array.append(pop_counter)
                pop_counter = 0

                if len(binary_nodes) != 0:
                    current_node = binary_nodes[-1]
                    for i in range(0, pop_counter_array.pop()):
                        traverse_values.append(traversed_nodes.pop().data)
                        counter += 1
                else:
                    while len(pop_counter_array) != 0:
                        for i in range(0, pop_counter_array.pop()):
                            traverse_values.append(traversed_nodes.pop().data)
                            counter += 1
            if counter == self.size + 1:
                traversed = True
        print("BST POSTORDER TRAVERSAL: {}".format(traverse_values))
        return traverse_values

    def size(self):
        """Determines the number of nodes (size) of the Binary Search Tree.

        returns: the size of the binary search tree (int)
        """
        print("BST SIZE:{} nodes".format(self.size))
        return self.size

    @staticmethod
    def _is_valid_input(data):
        """Checks whether user input is a number.

        args:
        data - the user input to be validated

        returns: true if user input is valid (a number), false otherwise
        """
        if type(data) in (int, float):
            return True
        else:
            print("BST ERROR: Input '{}' invalid. Input must be numerical.".format(data))
            return False
