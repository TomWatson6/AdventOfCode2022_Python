import re

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

F = {}
M = {}

for line in lines:
    p = re.findall("[A-Z]{2}|(?<=\=)\d+", line)
    M[p[0]] = p[2:]
    F[p[0]] = int(p[1])

DP = {}

def find(pos, visited, time):
    if time == 0:
        return 0
    
    key = (pos, tuple(sorted(visited)), time)
    if key in DP:
        return DP[key]

    ans = 0

    if time > 0 and pos not in visited and F[pos]>0:
        visited_ = set(visited)
        visited_.add(pos)
        ans = max(ans, sum(F[x] for x in visited) + find(pos, visited_, time-1))

    if time > 0:
        for n in M[pos]:
            ans = max(ans, sum(F[x] for x in visited) + find(n, visited, time-1))

    DP[key] = ans
    return ans

print(find('AA', set(), 30))
