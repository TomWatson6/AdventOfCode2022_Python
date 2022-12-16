import re
from copy import deepcopy
import sys

sys.setrecursionlimit(99999999)

    

with open("simple_input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

F = {}
M = {}

for line in lines:
    p = re.findall("[A-Z]{2}|(?<=\=)\d+", line)
    M[p[0]] = p[2:]
    F[p[0]] = int(p[1])

start = 'AA'
MAX_DEPTH = 30
T = (0, [])
DP = {}

def explore(curr, depth, total, visited, path):
    global T
    path.append(curr)

    if len(path) > 16:
        for i in range(8, len(path), 2):
            if path[len(path)-i*2:][:i] == path[len(path)-i*2:][i:] or path[len(path)-i*2:][:i] == path[len(path)-i*2:][:i][::-1]:
                return

    is_open = False

    if depth == 4:
        print("At depth 4")

    if curr not in visited:
        visited.add(curr)
        total += (MAX_DEPTH - depth) * F[curr]
    else:
        is_open = True

    # if (curr, depth, tuple(list(visited))) in DP:
    #     T.append(DP[(curr, depth, tuple(sorted(list(visited))))] + total)

    if depth >= MAX_DEPTH:
        # DP[(curr, depth, tuple(sorted(list(visited))))] = total
        # T.append((total, path))
        T = max(T, (total, path), key=lambda k: k[0])
        return

    for next in M[curr]:
        dd = 1 if is_open else 2
        explore(next, depth + dd, deepcopy(total), deepcopy(visited), deepcopy(path))

explore(start, 0, 0, set(), [])

print(T)











