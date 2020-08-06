
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = str(input())
    s = sorted(s)
    currentchar = s[0]
    counter = 1
    chardict = {}
    for c in s:
        try:
            chardict[c] += 1
        except:
            chardict[c] = 1
    chardict = dict(sorted(chardict.items(), key=lambda x: x[0]))
    chardict = dict(sorted(chardict.items(), key=lambda x: x[1],reverse=True))
    count = 0
    for k,v in chardict.items():        
        if count == 3:
            break
        else:
            count += 1
            print(k,v)
