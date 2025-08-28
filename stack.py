import sys

class BuildStack:
    def __init__(self):
        self.list_stack=[]
    
    def start(self):
        order_nums=int(sys.stdin.readline())
        self.execute_order(order_nums)
    
    def execute_order(self, order_nums):
        for i in range(order_nums):
            parts=sys.stdin.readline().strip().split()
            order=parts[0]

            if order=='push':
                self.order_push(parts)
            elif order=='top':
                print(self.order_top())
            elif order=='size':
                print(self.order_size())
            elif order=='empty':
                print(self.order_empty())
            elif order=='pop':
                print(self.order_pop())

    def order_push(self, parts):
        value=parts[1]
        self.list_stack.append(value)

    def order_top(self):
        if len(self.list_stack)==0:
            return -1
        else:
            return self.list_stack[-1]

    def order_size(self):
        return len(self.list_stack)
    
    def order_empty(self):
        if len(self.list_stack)==0:
            return 1
        else:
            return 0

    def order_pop(self):
        if len(self.list_stack)==0:
            return -1
        else:
            return self.list_stack.pop()

def main():
    Build_stack= BuildStack()
    Build_stack.start()

if __name__ == "__main__":
    main()


            
