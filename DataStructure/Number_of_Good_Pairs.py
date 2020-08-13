# Leet code problem - https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_n = {}
        for x in nums:
            try:
                dict_n[x] += 1
            except:
                dict_n[x] = 1
        res = 0
        for k,v in dict_n.items():            
            res += (v * (v - 1)) // 2
        return res
