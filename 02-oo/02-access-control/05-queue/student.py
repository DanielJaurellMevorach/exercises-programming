class Queue:
    def __init__(self):
        self.__items = []
    
    def add(self, item):
        self.__items.append(item)
    
    def next(self):
        temp = self.__items[0]
        self.__items.remove(self.__items[0])
        return temp
    
    def is_empty(self):
        return len(self.__items) == 0