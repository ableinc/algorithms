# Given Node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insertBefore(self, val):
        # create new Node
        # Time complexity: O(1)
        # Space complexity: O(1)
        new_node = Node(val)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node
    
    def insertAfter(self, prev_node, val):
        # Check if the given previous node exists
        # Time complexity: O(1)
        # Space complexity: O(1)
        if prev_node is None:
            raise AttributeError("The given previous node must not be None")
        # Create new node
        new_Node = Node(val)
        # Make next of new node as next of previous node
        new_node.next = prev_node.next
        # Make next of previous node as new node
        prev_node.next = new_node

    def insert(self, val):
        # Create new Node
        # Time complexity: O(N)
        # Space complexity: O(1)
        new_node = Node(val)
        # If linked list is empty, then make the new node head
        if self.head is None:
            self.head = new_node
            return
        # Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        # Change the next of last node
        last.next = new_node
    
    def search(self, val):
        # Traverse Linked List
        # Time complexity: O(N)
        # Space complexity: O(1)
        curr = self.head
        while curr:
            # If value found return node
            if curr.val == val:
                return curr
            curr = curr.next
        # If value not found return None
        return None
    
    def rSearch(self, LL, val):
        # Search recursively
        # Time complexity: O(N)
        # Space complexity: O(N)
        if not LL:
            return None
        if LL.val == val:
            return LL
        return self.rSearch(LL.next, key)

    def getAtPosition(self, position):
        # Time complexity: O(n)
        # Space complexity: O(1)
        curr = self.head
        count = 0
        while curr:
            if count == index:
                # Return Node is found
                return curr
            count += 1
            curr = curr.next
        return None
    
    def deleteAtPosition(self, position):
        # Time complexity: O(1) or O(N)
        # Space complexity: O(1)
        if self.head is None:
            return
        index = 0
        curr = self.head
        while curr.next and index < position:
            previous = curr
            curr = curr.next
            index += 1
        if index < position:
            raise AttributeError("Index out of range")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = curr.next

    
    @classmethod
    def deleteNode(cls, head, val):
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Check if list is empty or we reach at the end of the list.
        if (head == None):
            print("Element not present in the list")
            return -1
        # If current node is the
        # node to be deleted
        if (head.val == val):
            # If it's start of the node head
            # node points to second node
            if head.next: 
                head.val = head.next.val
                head.next = head.next.next
                return 1
            else: return 0
        if cls.deleteNode(head.next, val) == 0:
            head.next = None
            return 1
    
    def flush(self):
        curr = self.head
        while curr:
            _next = curr.next
            del curr.data
            curr = _next
    
    def size(self):
        # Time complexity: O(N)
        # Space complexity: O(1)
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def _rSizeCount(self, node, count=0):
        if not node:
            return count
        else:
            return self._rSizeCount(node.next, count+1)
    
    def rSize(self, node):
        # Time complexity: O(N)
        # Space complexity: O(N)
        return self._rSizeCount(self.head)
    
    def reverse(self):
        # Time complexity: O(N)
        # Space complexity: O(1)
        prev = None
        curr = self.head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        self.head = prev
    
    def rReverse(self):
        # Time complexity: O(N)
        # Space complexity: O(N)
        if head is None or head.next is None:
            return head
        # Reverse the rest list
        rest = self.reverse(head.next)
        # Put first element at the end
        head.next.next = head
        head.next = None
        # Fix the header pointer
        return rest
    
    def reverseUsingStack(self):
        # Time complexity: O(N)
        # Space complexity: O(N)
        stack, temp = [], head
        while temp:
            stack.append(temp)
            temp = temp.next
        head = temp = stack.pop()
        
        # Until stack is not empty
        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None
        return head
    
    def display(self):
        curr = self.head
        count = 0
        while curr:
            print(f'Node at position {count} has value: {curr.val}')
            curr = curr.next
            count+=1


if __name__ == '__main__':
  LL = LinkedList()
  # Insert value
  LL.insert(50)
  # Insert value
  LL.insert(60)
  # Insert value
  LL.insert(70)
  # Get size
  print('Size: ', LL.size())
  # Print LinkedList
  LL.display()
  # Search for value
  print('Found during search: ', LL.search(60).val)
  # Delete node
  LL.deleteNode(60)
  # Get size
  print('Size: ', LL.size())
  # Print LinkedList
  LL.display()
  
