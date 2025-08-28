import heapq
import sys

class My_heap:
    def __init__(self):
        self.max_heap=[]
    
    def pop(self):
        if self.max_heap:
            biggest=(heapq.heappop(self.max_heap))
            return -biggest
        else:
            return 0
        
    def push(self, number):
        heapq.heappush(self.max_heap, -number)
        

def main():
    my_heap=My_heap()
    command_nums=int(sys.stdin.readline())
    for i in range(command_nums):
        number=(int(sys.stdin.readline()))
        if number==0:
            print(my_heap.pop())
        else:
            my_heap.push(number)


if __name__=='__main__':
    main()