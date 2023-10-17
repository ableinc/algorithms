# Given Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to insert a new node with given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
    
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    # Return the node pointer
    return node


# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present a root
    if root is None or root.key == key:
        return root
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
    # Key is smaller than root's key
    return search(root.left, key)


# Given a BST and key, this function deletes the key and returns the new root
def delete(root, key):
    # Base case
    if root is None:
        return root
    # Recursive calls for ancestors of node to be deleted
    if root.key > key:
        root.left = delete(root.left, key)
        return root
    elif root.key < key:
        root.right = delete(root.right, key)
        return root
    # if both children exist
    else:
        succParent = root
        
        # Find successor
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
 
        # Copy Successor Data to root
        root.key = succ.key
 
        # Delete Successor and return root
        del succ
        return root


# Function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end='\t')
        inorder(root.right)


if __name__ == '__main__':
  """ 
  Let us create following BST 
        50 
     /     \ 
    30      70 
   /  \    /  \ 
  20  40  60   80 
  """
  root = None
  
  # Inserting value 50 
  root = insert(root, 50) 
  
  # Inserting value 30 
  insert(root, 30) 
  
  # Inserting value 20 
  insert(root, 20) 
  
  # Inserting value 40 
  insert(root, 40) 
  
  # Inserting value 70 
  insert(root, 70) 
  
  # Inserting value 60 
  insert(root, 60) 
  
  # Inserting value 80 
  insert(root, 80) 
  
  # Print the BST 
  inorder(root) 
  
  # Seach for key
  print('search: ', search(root, 70).key)
  
  # Delete key
  delete(root, 70)
  
  # Print the BST
  inorder(root)
