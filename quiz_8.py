# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
    
    
    
    def rearrange(self, step):
        
        length = len(self)
        
        self_node = self.head
        
        for _ in range(length - 1):
            self_node = self_node.next_node
        self_node.next_node = self.head
        
        
        current_node = self.head
        for _ in range(step - 2):
            current_node = current_node.next_node
        
        A_node = LinkedList('A')
        
        A_next_node = A_node.head
        
        x = length
        
        while x > 0:
            
            new_node = current_node.next_node
            
            current_node.next_node = Node('aaa')
            
            current_node.next_node.next_node = new_node.next_node
            
            new_node.next_node = None
            #new_node.value
            #type(new_node)
            #new_node.next_node
            
            A_next_node.next_node = new_node
            
            A_next_node = A_next_node.next_node
            
            for _ in range(step):
                current_node = current_node.next_node
        
            x -= 1
    
        A_node.head = A_node.head.next_node
        
        
        #        self_node = self.head
        
        #        for _ in range(length - 1):
        #            self_node = self_node.next_node
        
        #        self_node.next_node = None
        
                self.head = A_node.head



#        self.head = new_node.head


















# pass
# Replace pass above with your code

