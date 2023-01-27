

graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8']
    
    }

# the tree looks like this

#      5
#    3   7
#  2   4   8


visited=[]
queue=[]

#create a function for BFS
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)


#create a loop to visit each node
    while queue:
        print("queue: ",queue)
        print("visited: ",visited)
        m=queue.pop(0)
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            
print("Following is the Breath-First Search")

bfs(visited,graph,'5')





