
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = bob = 0
    for x in range(len(a)):
        if a[x] > b[x]:
            alice += 1
        elif a[x] < b[x]:
            bob += 1
    return str(alice + " " + bob)


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
