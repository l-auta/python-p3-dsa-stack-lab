class Stack:

    def __init__(self, items = [], limit = 100):
       self.items = []
       self.limit = limit
       for item in items:
           if (self.full()):
               raise ValueError('Initial stack size exceeds limit.')
           else:
               self.items.append(item)
        
    def isEmpty(self):
        return len(self.items) == 0
        
        pass

    def push(self, item):
       if self.full():
           return('Stack is full.')
       else:
           self.items.append(item)
           return True

    def pop(self):
        if self.isEmpty():
           return None
        else:
           return self.items.pop()
        

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False
    

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1
           
