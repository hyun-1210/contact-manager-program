from collections import deque
import sys

class Algorithm:
    def __init__(self,N,V):
        self.graph=[[] for i in range(N+1)]
    

    def build_graph(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    
    def dfs(self,N, V):
        visited=[False]*(N+1)
        dfs_answer=[]

        def recursive_dfs(V):
            visited[V]=True
            dfs_answer.append(V)
            for i in self.graph[V]:
                if not visited[i]:
                    recursive_dfs(i)

            return(dfs_answer)
        
    def bfs(self, N, V):
        queue=deque([V])
        bfs_visited=[False]*(N+1)
        bfs_answer=[]
        bfs_visited[V]=True
        while queue:
            connect_node=queue.popleft()
            bfs_answer.append(connect_node)
            for i in self.graph[connect_node]:
                if not bfs_visited[i]:
                    queue.append(i)
                    bfs_visited[i]=True
        return(bfs_answer)

def main():
    N, M, V= map(int, sys.stdin.readline().strip().split())
    alg=Algorithm(N, V)

    for i in range(M):
        node1, node2= map(int, sys.stdin.readline().strip().split())
        alg.build_graph(node1, node2)
    # connections = [list(map(int, input().split())) for _ in range(m)]
    
    for i in range(N+1):
        alg.graph[i].sort()

    dfs_result=alg.dfs(V)
    print(*dfs_result)

    bfs_result=alg.bfs(V)
    print(*bfs_result)

if __name__=='__main__':
    main()