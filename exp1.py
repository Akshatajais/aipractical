from collections import deque
def canMeasureWater(x, y, target):
    if target == 0:
        return True
    if target > x + y:
        return False
    q = deque([(0, 0)])

    visited = {(0, 0)}

    while q:

        a, b = q.popleft()

        if a == target or b == target or a + b == target:

            return True

        t = min(a, y - b)

        next_states = [

            (x, b), (a, y),

            (0, b), (a, 0),

            (a - t, b + t)

        ]

        t = min(b, x - a)

        next_states.append((a + t, b - t))

        for state in next_states:

            if state not in visited:

                visited.add(state)

                q.append(state)

    return False

# User input

x = int(input("Enter capacity of Jug 1: "))

y = int(input("Enter capacity of Jug 2: "))

target = int(input("Enter target quantity: "))


if canMeasureWater(x, y, target):

    print("Target quantity can be measured.")

else:

    print("Target quantity cannot be measured.")





