import sys
input_file = 'input15'

with open(input_file) as f:
    lines = f.readlines()
cave = [[int(i) for i in l.strip()] for l in lines]

max_x = len(cave[0])
max_y = len(cave)
start = [0,0]
end = [max_y, max_x]
large_number = sys.maxsize
def neighbours(y, x, unvisited_nodes, max_x, max_y):
    n = []
    if y - 1 >= 0 and unvisited_nodes[y-1][x] == 0:
        n.append([y-1, x])
    if x - 1 >= 0 and unvisited_nodes[y][x-1] == 0:        
        n.append([y, x-1])
    if x + 1 < max_x and unvisited_nodes[y][x+1] == 0:
        n.append([y, x+1])
    if y + 1 < max_y and unvisited_nodes[y+1][x] == 0:
        n.append([y+1, x])
    return n

def get_next_node(unvisited_nodes, dist, max_x, max_y):
    min_dist = large_number
    node = [0, 0]
    for i in range(0, max_y):
        for j in range(0, max_x):
            if unvisited_nodes[i][j] == 0: #if unvisited
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    node = [i, j]
    return node
def dijkstra(board, max_x, max_y):
    dist =[[large_number]*max_x for i in range(0, max_y)]
    dist[0][0] = 0
    current_node = [0,0]  
    end_node_unvisited = True
    unvisited_nodes = [[0]*max_x for i in range(0, max_y)]
    unvisited_nodes[0][0] = 1
    end_node = [max_y - 1, max_x - 1] 
    while end_node_unvisited:
        Q = neighbours(current_node[0], current_node[1], unvisited_nodes, max_x, max_y)
        for n in Q:
            if dist[n[0]][n[1]] > dist[current_node[0]][current_node[1]] + board[n[0]][n[1]]:
                dist[n[0]][n[1]] = dist[current_node[0]][current_node[1]] + board[n[0]][n[1]]
            if n == end_node:
                end_node_unvisited = False
        unvisited_nodes[current_node[0]][current_node[1]] = 1 
        current_node = get_next_node(unvisited_nodes, dist, max_x, max_y)     
        print(current_node) 
    print('lowest total risk: ', dist[max_y - 1][max_x - 1])
dijkstra(cave, max_x, max_y)

#part 2 modify the cave

new_cave = [[0]*(max_x*5) for i in range(0, max_y*5)]
for i in range(0, max_y*5):
    for j in range(0, max_x*5):
        to_add = int(i/max_y) + int(j/max_x)
        tmp = cave[i % max_y][j % max_x] + to_add
        if tmp > 9:
            tmp = tmp - 9
        new_cave[i][j] = tmp
dijkstra(new_cave, max_x*5, max_y*5)
