class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x: int) -> None:
        currMin = self.getMin()
        if currMin == None:
            currMin = x
        else:
            currMin = min(currMin, x)
        self.q.append((x, currMin))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if not self.q:
            return None
        return self.q[-1][0] 

    def getMin(self) -> int:
        if not self.q:
            return None
        return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__== '__main__':
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   # return -3
    minStack.pop()
    print(minStack.top())      # return 0
    print(minStack.getMin())   # return -2