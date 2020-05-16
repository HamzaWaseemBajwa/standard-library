from Exceptions import RangeError

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

    def insert(self, value, index=0):
        """
        Creates a new node at the specified index in the list
        and assigns to it the passed value 
        Increments the list size by 1 
    
        Parameters
        ----------
        value : the value to be added

        Raises
        -------
        RangeError
            If given index is less than 0 or
            greater than the list size

        """
        # Error case: Index out of acceptable range
        if index < 0 or index > self._size:
            raise RangeError("index out of range.")

        # Edge case 1: index == 0
        # Behave like push_front()
        if index == 0:
            self.push_front(value)

        # Edge case 2: index == size
        # Behave like push_back()
        if index == self._size:
            self.push_back(value)

        new_node = self.Node(value)
        i = 1
        current_node = self._head.next
        
        while(i < index):
            current_node = current_node.next
            i += 1

        new_node.next = current_node
        new_node.prev = current_node.prev
        current_node.prev.next = new_node
        current_node.prev = new_node
        self._size += 1

    def pop_front(self):
        """
        Removes and returns the values at the front of the list
        Returns None if empty

        """
        if (self._size == 0):
            return None

        output_value = self._head.value

        self._head = self._head.next
        self._size -= 1

        # Edge case, list is now empty
        if (self._size == 0):
            self._tail = None

        return output_value

    def pop_back(self):
        """
        Removes and returns the values at the end of the list
        Returns None if empty

        """
        if (self._size == 0):
            return None

        # Edge case, list has only one element
        # Behave same as pop_front()
        if (self._size == 1):
            return self.pop_front()

        output_value = self._tail.value

        self._tail = self._tail.prev
        self._size -= 1

        return output_value

    def remove(self, index=0):
        """
        Removes and returns the value at the given index

        Parameters
        ----------
        index : int
            list index of the node to be removed

        Raises
        -------
        RangeError
            If given index is less than 0 or
            greater than or equal to the list size

        """
        # Error case: Index out of acceptable range
        if index < 0 or index >= self._size:
            raise RangeError("index out of range.")
        
        # Edge case: Remove from front of list
        # Behave list pop_front()
        if (index == 0):
            return self.pop_front()

        # Edge case: Remove from end of list
        # Behave list pop_back()
        if (index == self._size - 1):
            return self.pop_back()

        i = 1
        current_node = self._head.next
        
        while(i < index):
            current_node = current_node.next
            i += 1

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        return current_node.value


    def peek_front(self):
        """
        Retuns the value stored by the node at the front of the list
        Returns None if list is empty

        """

        if (self._size == 0):
            return None
        
        return self._head.value

    def peek_back(self):
        """
        Retuns the value stored by the node at the end of the list
        Returns None if list is empty
        
        """
        if (self._size == 0):
            return None
        
        return self._tail.value
    
    def get(self, index=0):
        """
        Get the value of the node at the given index
        
        Parameters
        ----------
        index : int
            list index of the node

        Raises
        -------
        RangeError
            If given index is less than 0 or
            greater than or equal to the list size

        """

        # Error case: Index out of acceptable range
        if index < 0 or index >= self._size:
            raise RangeError("index out of range.")

        i = 0
        current_node = self._head
        
        while(i < index):
            current_node = current_node.next
            i += 1
        
        return current_node.value

    def set(self, value, index=0):
        """
        Sets the node at the given index to the passed value
        
        Parameters
        ----------
        value : (any type)
            the new value of the node to be set
        index : int
            list index of the node to be set

        Raises
        -------
        RangeError
            If given index is less than 0 or
            greater than or equal to the list size

        """

        # Error case: Index out of acceptable range
        if index < 0 or index >= self._size:
            raise RangeError("index out of range.")

        i = 0
        current_node = self._head
        
        while(i < index):
            current_node = current_node.next
            i += 1
        
        current_node.value = value

    def size(self):
        """
        Gets the size of the list
        
        """
        return self._size

    def clear(self):
        """
        Removes all nodes in the list

        """
        self._head = None
        self._tail = None
        self._size = 0

    def toList(self):
        """
        Returns the list values as a standard python List

        """
        if (self._size == 0):
            return []

        output_list = []
        current_node = self._head

        while(current_node != None):
            output_list.append(current_node.value)

        return output_list