class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:
   def __init__(self):
      self.head = None
	
   def push(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

nt		
   def insert(self, prev_node, NewVal):
      if prev_node is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
         NewNode.next.prev = NewNode


   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

dllist = doubly_linked_list()
dllist.push("APPLE")
dllist.push("BANANA")
dllist.push("ORANGE")
dllist.insert(dllist.head.next, "GRAPES")
dllist.listprint(dllist.head)