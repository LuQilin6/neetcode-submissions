class MinStack:

    def __init__(self):
        self.stack=[]
        self.min = math.inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val-self.min)
            if val<self.min: self.min = val
    # [1, 2, -2, -1, -2, 3]
    # [0, 1, -3, 1, 0, 5]
    def pop(self) -> None:
        p = self.stack.pop()
        if p<0:
            self.min = self.min-p
            

    def top(self) -> int:
        print("min: " + str(self.min))
        print(self.stack)
        last = self.stack[-1]
        if last < 0: 
            return self.min
        else:
            return self.min+self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
