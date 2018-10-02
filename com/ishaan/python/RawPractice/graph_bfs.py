graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



def BFS(mygraph):
    queue = ['A']
    seen = set()
    while queue != []:
        current = queue.pop(0) ## Make it pop() from pop (0) to convert into BFS
        if current in seen:
            continue
        seen.add(current)
        print(current)
        for item in mygraph[current]:
            if item not in seen:
                queue.append(item)

#BFS(graph)


## BFS to get all possible routes.
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def BFS_path(mygraph,source,destination):
    queue = []
    queue.append((source,[source]))
    seen = set()
    while queue != []:
        (current,path) = queue.pop()  ## Make it pop() from pop (0) to convert into BFS
        if current in seen:
            continue
        seen.add(current)
        for next in mygraph[current] - set(path):
            if next == destination:
                path.append(next)
                print("Below")
                print(path)
        for item in mygraph[current]:
            if item not in seen:
                queue.append((item,path + [item]))



BFS_path(graph,'A','E')