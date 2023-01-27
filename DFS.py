#!/usr/bin/env python
# coding: utf-8

# In[4]:


graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }

#keep track of visited nodes
visited=set()

#create a function for BFS
def dfs(visited, graph, node):
    if node not in visited:
        print("visited : ",node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)        

#driver code
print("Following is the Depth-First Search")

#call function for BFS
dfs(visited,graph,'5')
    



# In[ ]:




