# https://codeforces.com/contest/1535/problem/A

def GetGreater(twinList: list) -> int:
    if twinList[0] > twinList[1]:
        return twinList[0]
    else:
        return twinList[1]


test_case = int(input())

for _ in range(test_case):
    inputs = list(map(int, input().split()))
    first_pair = inputs[:2]
    second_pair = inputs[2:]
    inputs = sorted(inputs)
    first_winner = GetGreater(first_pair)
    second_winner = GetGreater(second_pair)
    final = sorted([first_winner, second_winner])
    if final == inputs[2:]:
        print("Yes")
    else:
        print("No")
