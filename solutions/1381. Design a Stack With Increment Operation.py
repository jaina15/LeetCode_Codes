class CustomStack:
​
    def __init__(self, maxSize: int):
        self.stack=[]
        self.n=maxSize
        self.temp=[]
        #print(len(self.stack))
​
    def push(self, x: int) -> None:
        if len(self.stack)<self.n:
            self.stack.append(x)
        #print(self.stack)
​
    def pop(self) -> int:
        if not self.stack:
            #print(self.stack)
            return -1
        else:
            #self.n-=1
            #print(self.stack)
            return self.stack.pop()
​
    def increment(self, k: int, val: int) -> None:
        if len(self.stack)<k:
            while self.stack:
                self.temp.append(self.stack.pop()+val)
            while self.temp:
                self.stack.append(self.temp.pop())
        else:
            n=len(self.stack)-k
            while n>0:
                self.temp.append(self.stack.pop())
                n-=1
            while k>0:
                self.temp.append(self.stack.pop()+val)
                k-=1
            while self.temp:
                self.stack.append(self.temp.pop())
        
​
​
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
