class Solution:
    def isSafe(self,node,colors,graph,c):
        for neighbour in graph[node]:
            if colors[neighbour] == c:
                return False
        return True

    def solve(self,node,colors,graph,m,v):
        if node == v:
            return True
        for c in range(1,m+1):
            if self.isSafe(node,colors,graph,c):
                colors[node]=c
                if self.solve(node+1,colors,graph,m,v):
                    return True
                colors[node]=0
        return False


    def graphColoring(self, v, edges, m):
        graph = [[] for _ in range(v)]
        for u,w in edges:
            graph[u].append(w)
            graph[w].append(u)

        colors = [0]*v
        return self.solve(0,colors,graph,m,v)




v = 3
edges = [[0, 1], [1, 2], [0, 2]]
m = 2
sol = Solution()
print(sol.graphColoring(v,edges,m))


