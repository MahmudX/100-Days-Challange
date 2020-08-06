t = int(input())
for _ in range(t):
    n = input()
    sideLength = list(map(int, input().split()))
    start, end = 0, len(sideLength) - 1
    peak = 0
    possible = True
    while start < len(sideLength)-1:
        if sideLength[start] < sideLength[start+1]:
            peak = start
            break
        else:
            start += 1
    while peak < len(sideLength)-1:
        if sideLength[peak] > sideLength[peak+1]:
            possible = False
            break
        else:
            peak += 1

    if possible:
        print("Yes")
    else:
        print("No")
