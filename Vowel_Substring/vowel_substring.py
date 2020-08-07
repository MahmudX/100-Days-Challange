["Unsloved","Time Limit Exceeded"]

#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    v = ['a', 'e', 'i', 'o', 'u']
    res = [-1, 0]
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
                        if subdict[sub] > res[1]:
                            res[0] = sub
                            res[1] = subdict[sub]
                    except:
                        subdict[sub] = 1
    #subdict = dict(sorted(subdict.items(), key=lambda x: x[1],reverse=True))
    # try:
    #     res = list(subdict.keys())[0]
    # except:
    #     res = "Not found!"
    if res[0] == -1:
        return "Not found!"
    else:
        return res[0]


if __name__ == '__main__':
    s = input()

    k = int(input().strip())
    result = findSubstring(s, k)

    print(result + '\n')



"""
Given a string of lowercase English letters and an integer of the substring length, determine the substring of that length that contains the most vowels. Vowels are in the set {a, e, i, o, u}. If there is more than one substring with the maximum number of vowels, return the one that starts at the lowest index. If there are no vowels in the input string, return the string 'Not found!' without quotes.

Example 1

s = 'caberqiitefg'

k = 5

The substring of length k = 5 that contains the maximum number of vowels is 'erqii' with 3 vowels.

The final answer is 'erqii'.

 

Example 2

s = 'aeiouia'

k = 3

 

All of the characters are vowels, so any substring of length 3 will have 3 vowels. The lowest index substring is at index 0, 'aei'.

 

Function Description

Complete the function findSubstring in the editor below.

 

findSubstring has the following parameters:

    s:  a string
    k: an integer

 

Returns:

    string: a string containing the final answer

 

Constraints

1 ≤ length(s) ≤ 2 * 105
1 ≤ k ≤ length(s)
Input Format For Custom Testing
Sample Case 0
Sample Input

STDIN      Function
-----      -----
azerdii →  s = 'azerdii'
5       →  k = 5
 

Sample Output

erdii
 

Explanation

s = 'azerdii'

k = 5

 

The possible 5 character substrings are:

    'azerd' which contains 2 vowels

    'zerdi' which contains 2 vowels

    'erdii' which contains 3 vowels

 

The final answer is 'erdii'.
"""
