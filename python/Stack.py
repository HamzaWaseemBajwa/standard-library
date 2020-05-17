class Stack:
    """

    Implementation of the Stack interface
    using Python's built-in list
    
    ...

    Attributes
    ----------
    int_list : list
        list object to store stack elements
    size : int
        count of items in stack

    Methods
    -------
    push(value)
        Add an item to the top of the stack

    pop()
        Remove and return the item at the top of the stack

    top()
        Return the item at the top of the stack

    size()
        get the number of items in the stack

    """

    def __init__(self):
        self._int_list = []
        self._size = 0

    def __str__(self):
        if (self._size == 0):
            return "None"
        
        _str = ""
        for elem in reversed(self._int_list):
            _str += elem + " "
        return _str

    def __repr__(self):
        return self.__str__()

    def push(self, value):
        self._int_list.append(value)
        self._size += 1

    def pop(self):
        if (self._size == 0):
            return None

        self._size -= 1
        return self._int_list.pop()

    def top(self):
        if (self._size == 0):
            return None

        return self._int_list[-1]

    def size(self):
        return self._size