class Solution:
    def isValid(self, s: str) -> bool:
        rs=[]
        for c in s:
            # print(rs)
            if c == '(' or c == '[' or c == '{':
                rs.append(c)
                continue
            if rs==[]: return False
            last=rs.pop()
            # print(rs)
            if c == ')' and last != '(': return False
            if c == ']' and last != '[': return False
            if c == '}' and last != '{': return False
            

        if rs==[]: return True
        return False


        