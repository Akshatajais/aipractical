from collections import deque
def is_safe(state, row, col):
   for r, c in enumerate(state):
       if c == col or abs(r - row) == abs(c - col):

           return False

   return True

# Breadth-First Search

def bfs(n):

   q = deque([()])

   nodes = 0
   while q:

       state = q.popleft()

       nodes += 1
       if len(state) == n:

           return state, nodes
       row = len(state)

       for col in range(n):

           if is_safe(state, row, col):

               q.append(state + (col,))
   return None, nodes

# Depth-First Search
def dfs(n):

   nodes = 0
   def solve(state):

       nonlocal nodes

       nodes += 1

       if len(state) == n:

           return state

       row = len(state)

       for col in range(n):

           if is_safe(state, row, col):

               result = solve(state + (col,))

               if result is not None:

                   return result

       return None

   return solve(()), nodes

def display(solution, n):

   if solution is None:

       print("No solution exists.")

       return
   for row in range(n):

       print(" ".join("Q" if solution[row] == col else "."

                      for col in range(n)))
#user input

n = int(input("Enter N: "))

if n <= 0:

   print("Enter a positive integer.")

else:

   print("\nBFS Solution:")
   b_sol, b_nodes = bfs(n)
   display(b_sol, n)
   print("Nodes explored:", b_nodes)

   print("\nDFS Solution:")
   d_sol, d_nodes = dfs(n)
   display(d_sol, n)
   print("Nodes explored:", d_nodes)

   print("\nComparison:")
   print("BFS nodes explored:", b_nodes)
   print("DFS nodes explored:", d_nodes)







