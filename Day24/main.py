from collections import defaultdict, deque
from copy import deepcopy

with open("input.txt") as f:
    input = [list(x.strip()) for x in f.readlines()]

D = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

grid = set()
start = (0, 0)
end = (0, 0)
W = defaultdict(lambda: [])
R = len(input) - 1
C = len(input[0]) - 1

for r, row in enumerate(input):
    for c, val in enumerate(row):
        if r == 0 and val == '.':
            start = (r, c)
        if r == len(input) - 1 and val == '.':
            end = (r, c)
        if val == '#':
            grid.add((r, c))
        elif val in ['^', 'v', '<', '>']:
            W[(r, c)].append(val)

def evolve(W):
    W_ = defaultdict(lambda: [])
    for k, v in W.items():
        while v:
            w = v.pop()

            r = k[0] + D[w][0]
            r = 1 if r >= R else r
            r = R - 1 if r < 1 else r

            c = k[1] + D[w][1]
            c = 1 if c >= C else c
            c = C - 1 if c < 1 else c

            pos = (r, c)
            W_[pos].append(w)

    return W_

def print_grid():
    for r in range(R + 1):
        for c in range(C + 1):
            if (r, c) in W:
                if len(W[(r, c)]) > 1:
                    print(len(W[(r, c)]), end="")
                else:
                    print(W[(r, c)][0], end="")
            else:
                if (r, c) in grid:
                    print("#", end="")
                else:
                    print(".", end="")
        print()
    print()

def reconstruct_path(r, c, d, CF):
    path = [(r, c)]

    while (r, c) != start:
        r, c, d = CF[(r, c, d)]
        path.append((r, c))

    return path[::-1]

def bfs(start, end):
    moves = 0
    Q = deque()
    Q.append((start, W, 0))
    S = set()
    print(start, end)
    CF = {}

    while Q:
        (r, c), w, d = Q.popleft()

        # if abs(r - end[0]) + abs(c - end[1]) + d >= 500:
        #     continue

        if (r, c, d) in S:
            continue
        S.add((r, c, d))

        if d + 1 > moves:
            moves = d + 1
            print(moves, r, c)

        if (r, c) == end:
            print(reconstruct_path(r, c, d, CF))
            return d, w

        W_ = evolve(w)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            rr = r + dr
            cc = c + dc

            if 0 <= rr <= R and 0 <= cc <= C and (rr, cc) not in grid and len(W_[(rr, cc)]) == 0: 
                Q.append(((rr, cc), deepcopy(W_), d + 1))
                CF[(rr, cc, d + 1)] = (r, c, d)

total = 0
d, W = bfs(start, end)
print(d)
total += d
d, W = bfs(end, start)
print(d)
total += d
d, W = bfs(start, end)
print(d)
total += d
print("Part 2:", total)



# for _ in range(30):
#     print_grid()
#     W = evolve(W)










