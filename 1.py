class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
        print(f"Item '{item}' pushed to stack.")

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Item '{item}' popped from stack.")
            return item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            item = self.stack[-1]
            print(f"Item '{item}' is on the top of the stack.")
            return item
        else:
            print("Stack is empty. No item to peek.")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack: {self.stack}"


# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    s.pop()
    print(s)
    s.peek()
    print(f"Is stack empty? {s.is_empty()}")
    print(f"Size of stack: {s.size()}")
