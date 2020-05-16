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

    # Begin Node implementation

    class Node:
        """ 
        Node class for Linked List

        ...

        Attributes
        ----------
        next : Node
            ptr to next node in list
        prev : Node
            ptr to previous node in list
        value : (any type)
            value stored by the node
        
        """

        def __init(self, value=None):
            self.value = value
            self.next = None
            self.prev = None

    # End Node implementation

    def __init__(self):
        """
        Parameters
        ----------
        No parameters

        """

        self._head = None
        self._tail = None
        self._size = 0

    def push_front(self, value):
        """
        Creates a new node at the front of the list
        and assigns to it the passed value
        Increments the list size by 1 

        Parameters
        ----------
        value : the value to be added

        """
        new_node = self.Node(value)

        # Edge Case : List is empty
        if self._size == 0:          
            self._tail = new_node

        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node
        self._size += 1
        
    def push_back(self, value):
        """
        Creates a new node at the end of the list
        and assigns to it the passed value 
        Increments the list size by 1 
        
        Parameters
        ----------
        value : the value to be added

        """

        # Edge Case : List is empty
        # Behave just like push_front()
        if self._size == 0:
            self.push_front(value)
            return

        new_node = self.Node(value)
        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node
        self._size += 1