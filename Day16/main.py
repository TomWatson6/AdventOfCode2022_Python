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
VALVES = len(M.keys())
MAX_DEPTH = 30
T = []
DP = {}











# def explore(curr, depth, total, visited, path):
#     path.append(curr)
#     is_open = False

#     if curr not in visited and depth <= MAX_DEPTH:
#         visited.add(curr)
#         total += (MAX_DEPTH - depth) * F[curr]
#     else:
#         is_open = True

#     if (curr, depth, tuple(list(visited))) in DP:
#         print("holy shit bruh")
#         T.append(DP[(curr, depth, tuple(sorted(list(visited))))] + total)

#     if depth >= MAX_DEPTH:
#         # DP[(curr, depth, tuple(sorted(list(visited))))] = total
#         # print((curr, depth, tuple(sorted(list(visited)))))
#         T.append((total, path))
#         return total

#     for next in M[curr]:
#         dd = 1 if is_open else 2
#         outcome = explore(next, deepcopy(depth) + dd, deepcopy(total), deepcopy(visited), deepcopy(path))
#         if outcome is not None:
#             DP[(curr, depth, tuple(sorted(list(visited))))] = outcome
#             print((curr, depth, tuple(sorted(list(visited)))))
# P = []

# def explore(curr, depth, total, visited, path):
#     # if len(visited) == VALVES:
#     #     P.append((path, sum([x[1] for x in path])))
#     #     return total

#     cost = 1

#     if curr not in visited and F[curr] != 0:
#         cost = 2

#     visited.add(curr)
#     path.append((curr, sum([F[x] for x in visited])))

#     if (curr, depth, tuple(sorted(list(visited)))) in DP:
#         return DP[(curr, depth, tuple(sorted(list(visited))))]

#     if depth >= MAX_DEPTH:
#         P.append((path, sum([x[1] for x in path])))
#         # print(path)
#         return total

#     # O = []

#     dest = M[curr]
#     dest = sorted(dest, key=lambda k: F[k])
#     dest = dest[-1]


#     # for next in M[curr]:
#     #     if cost == 2:
#     #         O.append(explore(next, deepcopy(depth) + cost, deepcopy(total) + ((MAX_DEPTH - depth) * F[curr]), deepcopy(visited), deepcopy(path)))
#     #     else:
#     #         O.append(explore(next, deepcopy(depth) + cost, deepcopy(total), deepcopy(visited), deepcopy(path)))
#     # print(O)
#     o = max(O)
#     DP[(curr, depth, tuple(sorted(list(visited))))] = o
#     return o

# output = explore(start, 0, 0, set(), [])

# P = sorted(P, key=lambda p: p[1])
# print(P[-1])
# print(output)











