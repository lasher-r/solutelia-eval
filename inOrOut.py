map = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def fill(a_map, point):
    if a_map[point[1]][point[0]] == 0:
        try:
            a_map[point[1]][point[0]] = -1
            # up
            fill(a_map, [point[0], point[1]-1])
            # down
            fill(a_map, [point[0], point[1]+1])
            # left
            fill(a_map, [point[0]-1, point[1]])
            # right
            fill(a_map, [point[0]+1, point[1]])
        except IndexError:
            # if the point is out of the map it's fine, just ignore
            pass
    return a_map

def pad(a_map):
    for row in a_map:
        row.insert(0, 0)
        row.insert(len(row), 0)
    a_map.insert(0, [0]*len(a_map[1]))
    a_map.insert(len(a_map), [0]*len(a_map[1]))
    return a_map
    
newmap = fill(pad(map), [0,0])

def inOrOut(point):
    if newmap[point[1]+1][point[0]+1] != -1:
        return 1
    return 0

print(inOrOut([3,2])) #1
print(inOrOut([3,1])) #1
print(inOrOut([6,2])) #0