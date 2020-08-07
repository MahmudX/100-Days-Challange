# Vowel Substring

[![Hacker Rank](https://img.shields.io/badge/%20-Hacker%20Rank-2EC866?color=14171A&labelColor=2EC866&logo=HackerRank&logoColor=ffffff&style=flat-square)](https://www.hackerrank.com/mahmudx) ![](https://img.shields.io/badge/Solved-Time%20Limit%20Exceeded-red?style=flat-square&logo=HackerRank) ![Python](https://img.shields.io/badge/-Python%203-Black?labelColor=EEED09&style=flat-square&logo=Python)

Given a string of lowercase English letters and an integer of the substring length, determine the substring of that length that contains the most vowels. Vowels are in the set **{a, e, i, o, u}**. 

If there is more than one substring with the maximum number of vowels, return the one that starts at the lowest index. If there are no vowels in the input string, return the string **'Not found!'** without quotes.

## Example 1
````
s = 'caberqiitefg'

k = 5
````
The substring of length k = 5 that contains the maximum number of vowels is 'erqii' with 3 vowels.

The final answer is 'erqii'.

## Example 2
````
s = 'aeiouia'

k = 3
````
All of the characters are vowels, so any substring of length 3 will have 3 vowels. The lowest index substring is at index 0, 'aei'.

Function Description

Complete the function findSubstring in the editor below.

findSubstring has the following parameters:

- **s**:  a string  
- **k**: an integer

#### Returns:

> string: a string containing the final answer

#### Constraints

*   1 ≤ length(s) ≤ 2 * 10<sup>5</sup>
*   1 ≤ k ≤ length(s)

## Input Format For Custom Testing

> The first line contains a string, s.

> The second line contains an integer, k.

### Sample Case 0

#### Sample Input

````
STDIN      Function
-----      -----
azerdii →  s = 'azerdii'
5       →  k = 5
````

#### Sample Output

`erdii`

#### Explanation

> s = 'azerdii'

> k = 5

The possible 5 character substrings are:

    `azerd` which contains 2 vowels

    `zerdi` which contains 2 vowels

    `erdii` which contains 3 vowels

The final answer is `erdii`.
### Sample Case 1

#### Sample Input

````
STDIN     Function
-----     -----
qwdftr →  s = 'qwdftr'
2      →  k = 2
````

#### Sample Output

````
Not found!
````

#### Explanation

The given string does not contain any vowels, so 'Not Found!' is returned.