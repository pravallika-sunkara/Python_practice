class Node(self,data):
  self.data = data
  self.next_node = None
class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def inserttotail(self,new_data):
    new_node=Node(new_data)
    head=self.head
    tail=self.tail
    
