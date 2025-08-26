from collections import deque
import sys

class FindVirus:
    def __init__(self):
        self.queue=deque([])
        self.graph=[]

    def graph_build(self, computer_num, connect_num):
        self.graph=[[] for i in range(computer_num+1)]

        for i in range(connect_num):
            a, b= map(int, sys.stdin.readline().split())
            self.graph[a].append(b)
            self.graph[b].append(a)

    def find(self, computer_num):
        visited=[False]*(computer_num+1)
        self.queue.append(1)
        visited[1]=True
        while self.queue:
            v=self.queue.popleft()
            for i in self.graph[v]:
                if not visited[i]:
                    self.queue.append(i)
                    visited[i]=True
        return visited
            
            
def main():
    findvirus=FindVirus()
    computer_num= int(sys.stdin.readline())
    connect_num=int(sys.stdin.readline())
    
    findvirus.graph_build(computer_num, connect_num)

    answer=findvirus.find(computer_num)
    print(answer.count(True)-1)


if __name__=='__main__':
    main()