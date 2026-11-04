from collections import deque

def is_valid(m, c, total_m, total_c):
    if not (0 <= m <= total_m and 0 <= c <= total_c):
        return False

    if m > 0 and c > m:
        return False

    rm, rc = total_m - m, total_c - c
    if rm > 0 and rc > rm:
        return False

    return True


def missionaries_cannibals():
    total_m = int(input("Enter number of missionaries: "))
    total_c = int(input("Enter number of cannibals: "))
    capacity = int(input("Enter boat capacity: "))

    start = (total_m, total_c, 0)
    goal = (0, 0, 1)

    moves = [(m, c)
             for m in range(capacity + 1)
             for c in range(capacity + 1)
             if 1 <= m + c <= capacity]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("\nSolution found:")
            for step, s in enumerate(path + [state]):
                print(f"Step {step}: {s}")
            return

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            nm, nc, nb = new_state

            # Check passengers available on departure bank
            if boat == 0 and (dm > m or dc > c):
                continue
            if boat == 1 and (dm > total_m - m or dc > total_c - c):
                continue

            if is_valid(nm, nc, total_m, total_c) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    print("No solution exists.")


missionaries_cannibals()