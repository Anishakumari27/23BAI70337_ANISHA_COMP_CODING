class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent=list(range(n))
        size=[1]*n
        def find(i):
            if parent[i]==i:
                return i
            parent[i]=find(parent[i])
            return parent[i]
        def union(i,j):
            root_i=find(i)
            root_j=find(j)
            if root_i!=root_j:
                if size[root_i]<size[root_j]:
                    parent[root_i]=root_j
                    size[root_j]+=size[root_i]
                else:
                    parent[root_j]=root_i
                    size[root_i]+=size[root_j]
                return True
            return False
        comp=n
        for u,v in connections:
            if union(u,v):
                comp-=1
        return comp-1