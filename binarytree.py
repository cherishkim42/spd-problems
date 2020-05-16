#!python
from queue import LinkedQueue


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None #returns T/F

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return False if self.is_leaf() else True

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        #Distance from ground - distance from this node to its furthest leaf
        TODO: Best and worst case running time: O(n) based on number of nodes"""
        left_height = 0
        right_height = 0

        if self.is_leaf():
            return 0

        if self.left is not None and self.right is not None:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left is not None: #and self.right is None
            return 1 + self.left.height()
        elif self.right is not None: #and self.left is None
            return 1 + self.right.height()


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: O(n) based on number of nodes"""
        # TODO: Check if root node has a value and if so calculate its height
        if self.root is not None:
            return self.root.height()
        else:
            return 0

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: O(logn) if tree is balanced, use binary search
        TODO: Worst case running time: O(n) if tree is a linked list"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: O(logn) if tree is balanced, use binary search
        TODO: Worst case running time: O(n) if tree is a linked list"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: O(logn) if tree is balanced, use binary search
        TODO: Worst case running time: O(n) if tree is a linked list"""

        if self.is_empty(): #Handle the case where the tree is empty
            self.root = BinaryTreeNode(item) #Create a new root node
            self.size += 1 #Increase the tree size
            return #ends ENTIRE FUNCTION, not just the loop (the way 'break' would)

        parent = self._find_parent_node_recursive(item, self.root)

        if item > parent.data:
            parent.right = BinaryTreeNode(item)
        else:
            parent.left = BinaryTreeNode(item)
        
        self.size += 1 #increment size counter

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: O(logn) b/c half is removed every time, resulting in logarithmic runtime
        TODO: Worst case running time: O(n) if tree is severely unbalanced (or like a linked list)"""
        node = self.root #Start with the root node
        while node is not None: #Loop til we descend past the closest leaf node
            if item == node.data: #Check if given item matches node's data
                return node #Return the found node
            elif item < node.data: #Check if given item is less than node's data
                node = node.left #Descend to the node's left child
                continue
            elif item > node.data: #Check if given item is greater than node's data
                node = node.right #Descend to the node's right child
                continue
        return None #Not found

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: O(logn) b/c half is removed every time, resulting in logarithmic runtime
        TODO: Worst case running time: O(n) if tree is severely unbalanced (or like a linked list)"""
        if node is None: #Check if starting node exists
            return None #Not found (base case)
        elif item == node.data: #If item matches node's data,
            return node #return the found node
        elif item < node.data: #If item is less than node's data,
            return self._find_node_recursive(item, node.left) #descend to node's left child
        elif item > node.data: #If item is greater than node's data,
            return self._find_node_recursive(item, node.right) #descend to node's right child

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: O(logn) b/c half is removed every time, resulting in logarithmic runtime
        TODO: Worst case running time: O(n) if tree is severely unbalanced (or like a linked list)"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        while node is not None: #Loop til we descend past the closest leaf node
            if item == node.data: #If item matches node's data,
                return parent #return parent of the found node
            elif item < node.data: #If item is less than node's data,
                parent = node #update the parent
                node = node.left #and descend to the node's left child
                continue
            elif item > node.data: #If item is greater than node's data,
                parent = node #update the parent
                node = node.right #and descend to the node's right child
                continue
        return parent #Not found

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        if node is None: #Check if starting node exists
            return parent #Not found (base case)
        # elif node.left is None or node.right is None:
        #     return None
        if item == node.data: #If item matches node's data,
            return parent #return parent of the found node
        elif item < node.data: #If item is less than node's data,
            return self._find_parent_node_recursive(item, node.left, node) #descend to node's left child
        elif item > node.data: #If item is greater than node's data,
            return self._find_parent_node_recursive(item, node.right, node) #descend to node's right child

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        return items #return in-order list of all items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) where n = # nodes. Every node is visited
        TODO: Memory usage: O(logn), making a stack whose number of nodes will be a max of the tree's height"""
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit) #traverse left subtree, if it exists
            visit(node.data) #visit this node's data w/ given visit fxn
            self._traverse_in_order_recursive(node.right, visit) #traverse right subtree, if it exists

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        return items #return pre-order list of all items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n), every node is visited
        TODO: Memory usage: O(n), making a stack"""
        if node is not None:
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit) #traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit) #traverse right subtree, if it exists

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        return items #return post-order list of all items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n), every node is visited
        TODO: Memory usage: O(logn), making stack whose # nodes <= tree's height"""
        if node is not None:
            self._traverse_post_order_recursive(node.left, visit) #traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit) #traverse right subtree, if it exists
            visit(node.data) #visit this node's data with given fxn

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        return items #return level-order list of all items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n), every node is visited
        TODO: Memory usage: O(n), max # nodes in queue dependent on max depth of tree, reduces from (n+1)/2 to O(n)"""
        queue = LinkedQueue() #create queue to store nodes not yet traversed in level-order
        queue.enqueue(start_node) #enqueue start_node
        while not queue.is_empty(): #loop until queue is empty
            node = queue.dequeue() #dequeue node @ front of queue b/c fifo
            visit(node.data) #visit this node's data using given fxn
            if node.left is not None: #if this node's left child exists,
                queue.enqueue(node.left) #enqueue it
            if node.right is not None: #if this node's right child exists,
                queue.enqueue(node.right) #enqueue it

def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
