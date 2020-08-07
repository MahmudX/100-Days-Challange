for _ in range(int(input())):
    l = list(map(str, input().split()))
    try:
        print(int(int(l[0])/int(l[1])))
    except Exception as e:
        if str(e) == "division by zero":
            print("Error Code: integer division or modulo by zero")
        else:
            print("Error Code:", e)
