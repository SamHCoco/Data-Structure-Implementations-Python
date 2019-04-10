class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        """Adds an element to the top of the stack and prints the stack.

        :arg
            element - The element to be added to stack
        """
        self.stack.append(element)
        self.print()

    def pop(self):
        """Returns and removes the element at the top of the stack and prints stack.

        :return The element at the top of the stack"""
        rear = len(self.stack) - 1
        if not self.is_empty():
            result = self.stack[rear]
            del self.stack[rear]
            print("\n{} POPPED.".format(result))
            self.print()
            return result

    def is_empty(self):
        """Determines whether stack is empty.

        :returns - True if stack is empty, false if it is not
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

        :returns - The number of elements in stack, or 0 if stack is empty.
        """
        if self.is_empty():
            return 0
        else:
            return len(self.stack)

