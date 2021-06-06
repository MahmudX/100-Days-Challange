# https://codeforces.com/contest/1535/problem/B

import math

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    inputs = list(map(int, input().split()))
    inputs.sort(key=lambda x: (x % 2 == 1))
    good_index = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            print((inputs[i], inputs[j]))
            if math.gcd(inputs[i], 2*inputs[j]) > 1:
                good_index += 1
            print(math.gcd(inputs[i], 2*inputs[j]))
            print("="*5)
    print(good_index)
