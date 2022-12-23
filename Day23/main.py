from collections import defaultdict

with open("input.txt") as f:
    input = [list(x.strip()) for x in f.readlines()]

grid = {}

for r, row in enumerate(input):
    for c, col in enumerate(row):
        grid[(r, c)] = col

def get_adjacents(coord):
    adj = []

    r, c = coord

    for rr in range(-1, 2):
        for cc in range(-1, 2):
            if rr == 0 and cc == 0:
                continue
            adj.append((r + rr, c + cc))

    return adj

funcs = {
    0: lambda k, adj: all([grid.get(x) is None or grid.get(x) == '.' for x in adj if x[0] < k[0]]),
    1: lambda k, adj: all([grid.get(x) is None or grid.get(x) == '.' for x in adj if x[0] > k[0]]),
    2: lambda k, adj: all([grid.get(x) is None or grid.get(x) == '.' for x in adj if x[1] < k[1]]),
    3: lambda k, adj: all([grid.get(x) is None or grid.get(x) == '.' for x in adj if x[1] > k[1]]),
}

outcomes = {
    0: lambda k: (k[0] - 1, k[1]),
    1: lambda k: (k[0] + 1, k[1]),
    2: lambda k: (k[0], k[1] - 1),
    3: lambda k: (k[0], k[1] + 1),
}

func_pointer = 0

def evolve(rounds):
    global func_pointer
    M = defaultdict(lambda: [])
    for k, v in grid.items():
        if v == '#':
            adj = get_adjacents(k)
            if any([grid.get(x) is not None and grid.get(x) == '#' for x in adj]):
                if funcs[func_pointer % len(funcs)](k, adj):
                    M[outcomes[func_pointer % len(funcs)](k)].append(k)
                elif funcs[(func_pointer + 1) % len(funcs)](k, adj):
                    M[outcomes[(func_pointer + 1) % len(funcs)](k)].append(k)
                elif funcs[(func_pointer + 2) % len(funcs)](k, adj):
                    M[outcomes[(func_pointer + 2) % len(funcs)](k)].append(k)
                elif funcs[(func_pointer + 3) % len(funcs)](k, adj):
                    M[outcomes[(func_pointer + 3) % len(funcs)](k)].append(k)

    new_grid = {}
    moved = set()

    for k, v in M.items():
        if len(v) > 1:
            continue

        new_grid[k] = grid[v[0]]
        moved.add(v[0])

    RS = max([x[0] for x, y in grid.items() if y == '#'])
    CS = max([x[1] for x, y in grid.items() if y == '#'])

    for r in range(-rounds, RS + 1 + rounds):
        for c in range(-rounds, CS + 1 + rounds):
            if (r, c) in moved:
                new_grid[(r, c)] = '.'
            elif new_grid.get((r, c)) is None:
                if grid.get((r, c)) is not None:
                    new_grid[(r, c)] = grid[(r, c)]
                else:
                    new_grid[(r, c)] = '.'

    func_pointer += 1
    
    return new_grid, len(M) == 0

def count_empty():
    count = 0

    YM = min([x[0] for x, y in grid.items() if y == '#'])
    XM = min([x[1] for x, y in grid.items() if y == '#'])
    YS = max([x[0] for x, y in grid.items() if y == '#'])
    XS = max([x[1] for x, y in grid.items() if y == '#'])

    for r in range(YM, YS + 1):
        for c in range(XM, XS + 1):
            if grid.get((r, c)) is not None and grid.get((r, c)) == '.':
                count += 1

    return count

def print_grid():
    YM = min([x[0] for x, y in grid.items() if y == '#'])
    XM = min([x[1] for x, y in grid.items() if y == '#'])
    YS = max([x[0] for x, y in grid.items() if y == '#'])
    XS = max([x[1] for x, y in grid.items() if y == '#'])

    for r in range(YM, YS + 1):
        for c in range(XM, XS + 1):
            if grid.get((r, c)) is not None:
                print(grid[(r, c)], end="")
            else:
                print("X", end = "")
        print()

    print()

def trim_grid():
    YM = min([x[0] for x, y in grid.items() if y == '#'])
    XM = min([x[1] for x, y in grid.items() if y == '#'])
    YS = max([x[0] for x, y in grid.items() if y == '#'])
    XS = max([x[1] for x, y in grid.items() if y == '#'])

    new_grid = {}

    for r in range(YM, YS + 1):
        for c in range(XM, XS + 1):
            if grid.get((r, c)) is not None:
                new_grid[(r, c)] = grid[(r, c)]

    return new_grid

# print_grid()

for i in range(1000):
    grid, same = evolve(i)
    if same:
        print(i + 1)
        break
    grid = trim_grid()
    print(i, len(grid))
    if i == 9:
        print(count_empty())








