class MyStack:

    def __init__(self):
        self.Q1 = []
        self.Q2 = []
        

    def push(self, x: int) -> None:
        self.Q1.append(x)
        

    def pop(self) -> int:
        while self.Q1:
            X = self.Q1.pop(0)
            if not self.Q1:
                break
            self.Q2.append(X)
        while self.Q2:
            M = self.Q2.pop(0)
            self.Q1.append(M)
        return X
        

    def top(self) -> int:
        while self.Q1:
            X = self.Q1.pop(0)
            self.Q2.append(X)
        while self.Q2:
            M = self.Q2.pop(0)
            self.Q1.append(M)
        return X
        

    def empty(self) -> bool:
        if self.Q1:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()