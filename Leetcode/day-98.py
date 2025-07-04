

#! 706. Design HashMap
class MyHashMap:

    def __init__(self):
        self.size = 10**6 + 1
        self.map = [-1] * self.size

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

myHashMap = MyHashMap()
myHashMap.put(1, 1)      
myHashMap.put(2, 2)      
myHashMap.get(1)        
myHashMap.get(3)         
myHashMap.put(2, 1)      
myHashMap.get(2)         
myHashMap.remove(2)      
myHashMap.get(2)         
