# ["Sloved","Time Limit Exceeded"]

#
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. STRING s
# 2. INTEGER k
#

def findSubstring(s, k):
    v = ['a', 'e', 'i', 'o', 'u']

    # Model 2
    res = [-1, 0]
    # Model 2 END

    subdict = {}
    for x in range(len(s)):
        sub = s[x:x+k]
        if len(sub) < k:
            break
        else:
            for y in sub:
                if y in v:
                    try:
                        subdict[sub] += 1
                        # Model 2
                        if subdict[sub] > res[1]:
                            res[0] = sub
                            res[1] = subdict[sub]
                        # Model 2 END
                    except:
                        subdict[sub] = 1
    # Model 1
    # subdict = dict(sorted(subdict.items(), key=lambda x: x[1],reverse=True))
    # try:
    #     res = list(subdict.keys())[0]
    # except:
    #     res = "Not found!"
    # return res
    # Model 1 END

    # Model 2
    if res[0] == -1:
        return "Not found!"
    else:
        return res[0]
    # Model 2 END

if __name__ == '__main__':
    s = input()

    k = int(input().strip())
    result = findSubstring(s, k)

    print(result + '\n')
