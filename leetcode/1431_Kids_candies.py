class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        for idx,i in enumerate(candies):
            if i + extraCandies >= max_candy:
                candies[idx] = True
            else :
                candies[idx] = False
        return candies