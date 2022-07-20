#225. Implement Stack using Queues

class MyStack(object):

    def __init__(self):
        self.empty_queue=[]
        self.data_queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data_queue.append(x)

        
    def pop(self):
        """
        :rtype: int
        """
        while len(self.data_queue)>1:
            self.empty_queue.append(self.data_queue[0])
            del self.data_queue[0]

        self.empty_queue, self.data_queue=self.data_queue, self.empty_queue
        
        return self.empty_queue.pop()
    
    def top(self):
        """
        :rtype: int
        """
        num=self.pop()
        self.data_queue.append(num)
        return num

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data_queue)==0 and len(self.empty_queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
