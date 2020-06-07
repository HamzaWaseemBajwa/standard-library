import random
import timeit

# Nodes to be used in trees.


class TreeNode:
    '''A node in a binary tree.'''

    def __init__(self, n):
        self.data = n
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

    def num_children(self):
        '''N.num_children() -> int

        Returns the number of children of N that are not None.
        '''
        return sum([1 for child in [self.left, self.right] if child])

# Trees utilizing above nodes.  Use helper functions defined outside
# the class to achieve functionality.


class BinarySearchTree:
    '''A BST. Does not contain duplicates. Nodes are of type TreeNode.'''

    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return tree_string(self.root)

    def __repr__(self):
        return self.__str__()

    def add(self, n):
        self.root, added = bst_add(self.root, n)
        if added:
            self.size += 1
        return added

    def find(self, n):
        return bst_find(self.root, n)

    def remove(self, n):
        self.root, removed = bst_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed

    def clear(self):
        self.__init__()

    def inorder(self):
        return inorder(self.root)

    def preorder(self):
        return preorder(self.root)

    def postorder(self):
        return postorder(self.root)

########## Tree helper functions.  ##########

def tree_string(node, level=0):
    '''tree_string(node) -> str

        Returns a string representation of the subtree rooted at node.

        credit: https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    '''
    if not node:
        return '\n'
    prefix = '   ' * level
    str = repr(node) + '\n'
    if node.num_children():
        str += prefix + '|_ ' + tree_string(node.left, level + 1)
        str += prefix + '|_ ' + tree_string(node.right, level + 1)
    return str


def tree_height(self, node):
    '''tree_height(node) -> int

    Returns the height of the subtree rooted at node. Returns -1 if
    node is None.

    '''
    if (node != None):
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))
    return -1


def inorder(n):
    '''inorder(node) -> [node content]

    Returns an inorder traversal of the subtree rooted at node; empty
    list if n is None.
    '''
    if n == None:
        return []
    else:
        returnList = []
        returnList.extend(inorder(n.left))
        returnList.append(str(n))
        returnList.extend(inorder(n.right))
        return returnList


def preorder(n):
    '''preorder(node) -> [node content]

    Returns an preorder traversal of the subtree rooted at node; empty
    list if n is None.
    '''
    if n == None:
        return []
    else:
        returnList = []
        returnList.append(str(n))
        returnList.extend(preorder(n.left))
        returnList.extend(preorder(n.right))
        return returnList


def postorder(n):
    '''postorder(node) -> [node content]

    Returns an postorder traversal of the subtree rooted at node;
    empty list if n is None.
    '''
    if n == None:
        return []
    else:
        returnList = []
        returnList.extend(postorder(n.left))
        returnList.extend(postorder(n.right))
        returnList.append(str(n))
        return returnList


def bst_find(node, n):
    '''bst_find(node, int) -> bool

    Returns whether n is contained in the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.
    '''
    currentNode = node
    while True:
        if (n == currentNode.data):
            return True
        elif (n < currentNode.data and currentNode.left != None):
            currentNode = currentNode.left
        elif (n > currentNode.data and currentNode.right != None):
            currentNode = currentNode.right
        else:
            return False


def bst_find_min(node):
    '''bst_find_min(node) -> int

    node. Assumes the subtree to be a BST with no duplicates.
    '''
    currentNode = node
    while True:
        if (currentNode.left == None):
            return currentNode.data
        currentNode = currentNode.left


def bst_add(node, n):
    '''bst_add(node, int) -> (node, bool)

    Returns the result of adding n to the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.

    The first returned value is the root of the tree obtained as a
    result of the addition. The second value indicates whether
    addition succeeded. Addition fails if n is already present in the
    subtree.
    '''
    root = node
    if (node == None):
        node = TreeNode(n)
        return (node, True)
    else:
        while True:
            if (n < node.data):
                if (node.left == None):
                    node.left = TreeNode(n)
                    return (root, True)
                else:
                    node = node.left
            elif (n > node.data):
                if (node.right == None):
                    node.right = TreeNode(n)
                    return (root, True)
                else:
                    node = node.right
            else:
                return (root, False)


def findSuccessor(root, parent):  # additional helper function
    """ return the minimum node in the current tree and its parent """
    if root.left:
        return findSuccessor(root.left, root)
    else:
        return (parent, root)


def bst_remove(node, n):
    '''bst_remove(node, int) -> (node, bool)

    Returns the result of removing n from the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.

    The first returned value is the root of the tree obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    '''
    bool = False
    if node:
        if node.data == n:
            if node.right and node.left:
                (p_succ, succ) = findSuccessor(node.right, node)
                if p_succ.left == succ:
                    p_succ.left = succ.right
                else:
                    p_succ.right = succ.right
                succ.left = node.left
                succ.right = node.right
                return (succ, True)
            else:
                if node.left:
                    return (node.left, True)
                else:
                    return (node.right, True)
        else:
            if node.data > n:
                if node.left:
                    (node.left, bool) = bst_remove(node.left, n)
            else:
                if node.right:
                    (node.right, bool) = bst_remove(node.right, n)
    return (node, bool)
