import collections
import sys

class MyQueue:
    def __init__(self):
        self.queue=collections.deque()
        self.command_map = {
            'push': self.push,
            'pop': self.pop,
            'size': self.size,
            'empty': self.empty,
            'front': self.front,
            'back': self.back,
            }

    def start(self):
        command_nums=int(sys.stdin.readline())
        self.get_command(command_nums)

    def get_command(self, command_nums):
        for i in range(command_nums):
            parts=sys.stdin.readline().strip().split()
            command=parts[0]


            if command=='push':
                self.command_map[command](parts)
            else:
                result=self.command_map[command]()
                print(result)

    def push(self,parts):
        value=parts[1]
        self.queue.append(value)
    
    def pop(self):
        if not self.queue:
            return -1
        else:
            return(self.queue.popleft())
    
    def size(self):
        return(len(self.queue))
    
    def empty(self):
        if not self.queue:
            return 1
        else:
            return 0
    
    def front(self):
        if not self.queue:
            return -1
        else:
            return self.queue[0]
        
    def back(self):
        if not self.queue:
            return -1
        else:
            return self.queue[-1]

def main():
    build_queue=MyQueue()
    build_queue.start()

if __name__ == "__main__":
    main()
    