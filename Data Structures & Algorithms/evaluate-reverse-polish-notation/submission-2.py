class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opList=['+', '-', '*', '/']
        stackList=[]
        for t in tokens:
            if t in opList:
                val2 = stackList.pop()
                val1 = stackList.pop()
                if t == '+': 
                    stackList.append(val1+val2)
                elif t=='-':
                    stackList.append(val1-val2)
                elif t=='*':
                    stackList.append(val1*val2)
                else:
                    stackList.append(int(val1/val2))
            else:
                stackList.append(int(t))
        
        return stackList[-1]
        