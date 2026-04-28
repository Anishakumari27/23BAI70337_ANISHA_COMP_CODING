
from collections import defaultdict,deque
class Solution:
    def isCyclic(self, V, edges):
        graph=defaultdict(list)
        indegree=[0]*(V)
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        topo=0
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            topo+=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return topo!=V
            
