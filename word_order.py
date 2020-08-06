wcoll = {}
for _ in range(int(input())):
    word = str(input())
    try:
        wcoll[word] += 1
    except:
        wcoll[word] = 1
#wcoll = dict(sorted(wcoll.items(), key=lambda x: x[0], reverse=True))
print(len(wcoll))
print(" ".join(map(str, list(wcoll.values()))))
