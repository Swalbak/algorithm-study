#232. Implement Queue using Stacks

class MyQueue(object):

    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.pop_stack)==0:
            while len(self.push_stack)!=0:
                self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        num=self.pop()
        self.pop_stack.append(num)
        return num

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.pop_stack)==0 and len(self.push_stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
