from collections import deque
d = deque()
t = int(input())
for _ in range(t):
    command = str(input()).split()
    if command[0] == "append":
        d.append(command[1])
    elif command[0] == "appendleft":
        d.appendleft(command[1])
    elif command[0] == "pop":
        d.pop()
    else:
        d.popleft()
print(" ".join(map(str, list(d))))
