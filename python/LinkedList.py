class LinkedList:
    """
    Linked list implementation of the List interface
    
    ...
    
    Attributes
    ----------
    head : Node
        a pointer to the frontmost node in the list
    tail : Node
        a pointer to the rearmost node in the list
    size : int
        count of nodes in the list

    Methods
    -------
    push_front(value)
        Adds the passed value to the front of the list
    
    push_back(value)
        Adds the passed value to end of the list

    insert(value, index=0)
        Adds the passed value at the given index in the list

    pop_front()
        Removes and returns the values at the front of the list

    pop_back()
        Removes and returns the values at the end of the list

    remove(index=0)
        Removes and retuns the value at the given index

    peek_front()
        Gets the value at the front of the list

    peek_back()
        Gets the value at the end of the list
    
    get(index=0)
        Gets the value at the given index in the list

    set(value, index=0)
        Sets the node at the given index to the passed value

    size()
        Gets the size of the list

    clear()
        Removes all nodes in the list

    toList()
        Returns the elements as a standard python List    


    """
    def __init__(self):
        self.head = None
        self.tail = None       