def is_leap(leap):
    if leap % 4 == 0: 
        if leap % 100 == 0 and leap % 400 != 0:
            return False
        return True

    return False


year = int(input())
print(is_leap(year))
