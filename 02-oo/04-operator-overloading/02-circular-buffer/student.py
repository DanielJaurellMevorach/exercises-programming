class CircularBuffer:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.inventory = []
        
    def add(self, value):
        if len(self.inventory) == self.buffer_size:
            for i in enumerate(self.inventory.copy()):
                self.inventory[i[0] - 1] = i[1]
            self.inventory.pop()
            self.inventory.append(value)
        else:
            self.inventory.append(value)
            
    def __len__(self):
        return len(self.inventory)
    
    def __getitem__(self, index):
        return self.inventory[index]
    
    def inventory(self):
        return self.inventory
        
    
    
# We are only interested in the last 3 items
buffer = CircularBuffer(3)

# Initially the buffer is empty
print(len(buffer))

# Let's add a few items
buffer.add('a')
buffer.add('b')
buffer.add('c')
buffer.add('XYZ')
print(buffer.inventory)