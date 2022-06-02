class Node:
   def __init__(self, datavalue=None):
      self.datavalue = datavalue
      self.nextvalue = None

class SLinkedList:
   def __init__(self):
      self.headvalue = None

   def listprint(self):
      printvalue = self.headvalue
      while printvalue is not None:
         print (printvalue.datavalue)
         printvalue = printvalue.nextvalue

list = SLinkedList()
list.headvalue = Node("APPLE")
F2 = Node("BANANA")
F3 = Node("GRAPES")


list.headvalue.nextvalue = F2


F2.nextvalue = F3

list.listprint()