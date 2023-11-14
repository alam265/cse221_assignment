class Node:
    def __init__(self,elem,loc):
        self.elem = elem 
        self.next = loc 

class Queue:
    def __init__(self):
        self.front = None
        self.back = None 
    def enqueue(self,elem):
        if self.front is None:
            self.front = Node(elem,None)
            self.back = self.front 
        else:
            newNode = Node(elem,None)
            self.back.next = newNode 
            self.back = newNode 
    
    def dequeue(self):
        if self.front is not None:
            x = self.front 
            self.front = self.front.next 
            return x.elem  
        else:
            print("Empty Queue")
    
    
    def isEmpty(self):
        if self.front is None :
            return True 
        return False 
    def printQueue(self):
        p = self.front
        while p != None:
            print(p.elem,end=' ')
            p = p.next