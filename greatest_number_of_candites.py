class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c = candies.copy()
        c.sort()
        res = []
        for x in candies:
            if(x+extraCandies>=c[-1]):
                res.append(True)
            else:
                res.append(False)
        return res