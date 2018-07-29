# Python program to reverse a linked list 
# Time Complexity : O(n)
# Space Complexity : O(1)
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
         
    # Function to insert a new node at the beginning
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print ("Value: " ,temp.data)
            temp = temp.next
            
    def search(self,data):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == data:
                found = True
            else:
                current = current.next
        return found
    
    def size(self):
        count = 0
        current= self.head
        while current:
            count+=1
            current=current.next
        print ("Size of linked list: ",count)

    def delete(self):
        current=self.head
        self.head = current.next
        print("Deleted Value: ",current.data)
 
 
# Driver program to test above functions
arr=[1,3,6,4,5]
print("Initial array:",arr)
llist = LinkedList()
for i in range(0,len(arr)):
    llist.insert(arr[i])
 
print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()

llist.size()
llist.delete()
llist.size()

#print("Result of Search: ",llist.search(4))
