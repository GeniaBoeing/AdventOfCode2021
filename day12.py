input_file = 'input12'

with open(input_file) as f:
    lines = f.readlines()

lines = [l.strip().split('-') for l in lines]
nodes = []
for i in range(0, len(lines)):
    for j in range(0, 2):
        if lines[i][j] not in nodes:
            nodes.append(lines[i][j])
print(nodes)
print(lines)
nr_nodes = len(nodes)
node_idx = {}
for i in range(0, nr_nodes):
    node_idx[nodes[i]] = i
print(node_idx)
A = [0] * nr_nodes
A = [[0] * nr_nodes for i in range(0, nr_nodes)]

for i in range(0, len(lines)):
    A[node_idx[lines[i][0]]][node_idx[lines[i][1]]] = 1
    A[node_idx[lines[i][1]]][node_idx[lines[i][0]]] = 1

def print_A(A):
    for i in range(0, len(A)):
        print(A[i])

start_node = node_idx['start']
end_node = node_idx['end']
nr_paths = 0
nodes_visited = [0] * nr_nodes

path_str = []
def traversal(node, nodes_visited, path_str):
    global nr_paths
    edges = [i for i in range(0, len(A[node])) if A[node][i] == 1 if (nodes[i].islower() and nodes_visited[i] == 0) or nodes[i].isupper() and i != start_node]
    new_nodes_visited = nodes_visited.copy()
    loc_path_str = path_str.copy()
    if edges:
        loc_path_str += [nodes[node]]
        new_nodes_visited[node] += 1
    for i in edges:
        if i == node_idx['end']:
            nr_paths += 1
            print(loc_path_str + ['end'])
        else:
            traversal(i, new_nodes_visited, loc_path_str)

traversal(start_node, nodes_visited, path_str)
print('nr_paths ', nr_paths )

nr_paths = 0
path_str = []         
lower_nodes = [i for i in nodes if i.islower()]
def traversal_part2(node, nodes_visited, path_str, small_visited_twice):
    global nr_paths
    if not small_visited_twice:
        edges = [i for i in range(0, len(A[node])) if A[node][i] == 1 if (nodes[i].islower() and nodes_visited[i] < 2) or nodes[i].isupper() if i != start_node]
    elif small_visited_twice:
        edges = [i for i in range(0, len(A[node])) if A[node][i] == 1 if (nodes[i].islower() and nodes_visited[i] == 0) or nodes[i].isupper() if i != start_node]
    new_nodes_visited = nodes_visited.copy()
    loc_path_str = path_str.copy()
    loc_small_visited_twice = small_visited_twice
    if edges:
        loc_path_str += [nodes[node]]
        new_nodes_visited[node] += 1
        for ln in lower_nodes:
            if new_nodes_visited[node_idx[ln]] == 2:
                loc_small_visited_twice = True
        if loc_small_visited_twice:
            edges = [i for i in range(0, len(A[node])) if A[node][i] == 1 if (nodes[i].islower() and nodes_visited[i] == 0) or nodes[i].isupper() if i != start_node]
    for i in edges:
        if i == node_idx['end']:
            nr_paths += 1
            print(loc_path_str + ['end'])
        else:
            traversal_part2(i, new_nodes_visited, loc_path_str, loc_small_visited_twice)

traversal_part2(start_node, nodes_visited, path_str, False)
print('nr_paths ', nr_paths )

        

