# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

#User function Template for python3

from typing import List
# from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        qu = deque([0])
        visited = [0]*V
        visited[0] = 1
        traversal = []
        while qu:
            node = qu.pop()
            traversal.append(node)
            for neigh in adj[node]: 
                if not visited[neigh]: qu.appendleft(neigh); visited[neigh] = 1
        return traversal
        

#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)): print(ans[i], end = " ")
        print()
        

# } Driver Code Ends
