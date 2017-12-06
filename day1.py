with open("day1_input") as infile:
    instructions = [ (x[0],x[1:]) for x in infile.read().strip().split(", ") ]

def get_intersect(v1, v2):
    if v1[0] == v1[2]:
        if (min([v1[1], v1[3]]) < v2[1] < max([v1[1], v1[3]])
            and min([v2[0], v2[2]]) < v1[0] < max([v2[0], v2[2]])):
            return [v1[0], v2[1]]
    if v1[1] == v1[3]:
        if (min([v1[0], v1[2]]) < v2[0] < max([v1[0], v1[2]])
            and min([v2[1], v2[3]]) < v1[1] < max([v2[1], v2[3]])):
            return [v2[0], v1[1]]
    return None

def find_intersect(vectors):
    for v1 in vectors:
        for v2 in vectors[vectors.index(v1)+1:]:
            if get_intersect(v1, v2) is not None:
                return get_intersect(v1, v2)



vectors = []
direction = 0
x = 0
y = 0
for ins in instructions:
    vectors.append([x, y])
    if ins[0] == 'R':
        direction = (direction + 1) % 4
    elif ins[0] == 'L':
        direction = (direction - 1) % 4
    if direction == 0:
        y += int(ins[1])
    elif direction == 1:
        x += int(ins[1])
    elif direction == 2:
        y -= int(ins[1])
    else: 
        x -= int(ins[1])
    vectors[-1] += [x, y]

intersect = find_intersect(vectors)
print(abs(x) + abs(y))
print(abs(intersect[0]) + abs(intersect[1]))
