class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        """
        minstack we basically track at every point what is the min val
        at this point
        ex:
        stack [-1,0,-3,5]
        minstack = [-1,-1,-3,-3]
        """
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            if self.minstack:
                val = min(val, self.minstack[-1])
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
