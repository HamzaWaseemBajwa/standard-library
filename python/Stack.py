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
        """
        Returns a string representation of the stack

        """
        if (self._size == 0):
            return "None"
        
        _str = ""
        top = True
        for elem in reversed(self._int_list):
            _str += str(elem) + " "
            if top:
                _str += "| "
                top = False
        return _str

    def __repr__(self):
        """
        See __str__()

        """
        return self.__str__()

    def push(self, value):
        """
        Add an item to the top of the stack
        Increments size by 1

        """
        self._int_list.append(value)
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the top of the stack
        Decreases size by 1
        Returns None if empty

        """
        if (self._size == 0):
            return None

        self._size -= 1
        return self._int_list.pop()

    def top(self):
        """
        Returns the item at the top of the stack
        Returns None if empty
        """
        if (self._size == 0):
            return None

        return self._int_list[-1]

    def size(self):
        """
        Returns the size of the stack

        """
        return self._size