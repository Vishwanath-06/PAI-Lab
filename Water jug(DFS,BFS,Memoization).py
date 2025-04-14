.#WATERJUG-DFS
def wj_dfs(cap1,cap2,goal):
  visited=set()
  path=[]
  def dfs(jg1,jg2):
    if (jg1,jg2) in visited:
      return False
    visited.add((jg1,jg2))
    path.append((jg1,jg2))
    if jg1==goal or jg2==goal :
      return True
    if dfs(cap1,jg2):
      return True
    if dfs(jg1,cap2):
      return True
    if dfs(0,jg2):
      return True
    if dfs(jg1,0):
      return True
    if dfs(max(0, jg1 - (cap2 - jg2)),min(cap2,jg1+jg2)):
      return True
    if dfs(min(cap1,jg1+jg2),max(0,jg2-(cap1-jg1))):
      return True
    path.pop()
    return False
  dfs(0,0)
  return path

jug1 =int(input("Enter Capacity of the 1st jug;"))
jug2 =int(input("Enter Capacity of the 2nd jug:"))
goal=int(input("Enter Target amount to measure:"))
solution = wj_dfs(jug1,jug2,goal)
if solution:
    print("Solution steps:")
    for step in solution:
      print(f"Jug-1:{step[0]},Jug-2:{step[1]}")
else:
    print("No solution found.")

#Waterjug-bfs
from collections import deque
def water_jug_bfs(capacity1, capacity2, target):
    initial_state = (0, 0)
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        (jug1, jug2), path = queue.popleft()
        if jug1 == target or jug2 == target:
            print("Solution steps:")
            for state in path + [(jug1, jug2)]:
                print(f"Jug-1:{state[0]},Jug-2:{state[1]}")
            return
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        if jug1 < capacity1:
            queue.append(((capacity1, jug2), path + [(jug1, jug2)]))
        if jug2 < capacity2:
            queue.append(((jug1, capacity2), path + [(jug1, jug2)]))
        if jug1 > 0:
            queue.append(((0, jug2), path + [(jug1, jug2)]))
        if jug2 > 0:
            queue.append(((jug1, 0), path + [(jug1, jug2)]))
        pour_to_jug2 = min(jug1, capacity2 - jug2)
        if pour_to_jug2 > 0:
            queue.append(((jug1 - pour_to_jug2, jug2 + pour_to_jug2), path + [(jug1, jug2)]))
        pour_to_jug1 = min(jug2, capacity1 - jug1)
        if pour_to_jug1 > 0:
            queue.append(((jug1 + pour_to_jug1, jug2 - pour_to_jug1), path + [(jug1, jug2)]))
    print("No solution found")
capacity1 = int(input("Enter Capacity of the 1st jug: "))
capacity2 = int(input("Enter Capacity of the 2nd jug: "))
target = int(input("Enter Target amount to measure: "))
water_jug_bfs(capacity1, capacity2, target)

# Water jug using memorization
from collections import defaultdict
jug1 =int(input("Enter Capacity of the 1st jug:"))
jug2 =int(input("Enter Capacity of the 2nd jug:"))
aim=int(input("Enter Target amount to measure:"))
visited=defaultdict(lambda: False)
def wj_solver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (wj_solver(0, amt2) or
                wj_solver(amt1, 0) or
                wj_solver(jug1, amt2) or
                wj_solver(amt1, jug2) or
                wj_solver(amt1 + min(amt2, (jug1-amt1)),
                amt2 - min(amt2, (jug1-amt1))) or
                wj_solver(amt1 - min(amt1, (jug2-amtuu2)),
                amt2 + min(amt1, (jug2-amt2))))
    else:
        return False

print("Steps: ")
wj_solver(0, 0)