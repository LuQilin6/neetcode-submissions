class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array=[]
        


    def get(self, i: int) -> int:
        # if i > self.getSize(): return null
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i]=n
        return


    def pushback(self, n: int) -> None:
        curSize=self.getSize()
        curCapacity=self.getCapacity()
        if curSize == curCapacity: self.resize()
        self.array.append(n)
        return


    def popback(self) -> int:
        lastEle = self.array.pop()
        return lastEle
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
