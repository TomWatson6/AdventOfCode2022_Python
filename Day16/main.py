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
T = []
DP = {}

def explore(curr, depth, total, visited, path):
    path.append(curr)
    is_open = False

    if curr not in visited:
        visited.add(curr)
        total += (MAX_DEPTH - depth) * F[curr]
    else:
        is_open = True

    # if (curr, depth, tuple(list(visited))) in DP:
    #     T.append(DP[(curr, depth, tuple(sorted(list(visited))))] + total)

    if depth >= MAX_DEPTH:
        # DP[(curr, depth, tuple(sorted(list(visited))))] = total
        T.append((total, path))
        return

    for next in M[curr]:
        dd = 1 if is_open else 2
        explore(next, depth + dd, deepcopy(total), deepcopy(visited), deepcopy(path))

explore(start, 0, 0, set(), [])

print(max(T, key=lambda t: t[0]))











