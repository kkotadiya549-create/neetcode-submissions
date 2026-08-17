class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            speed = (left + right) // 2

            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile / speed)

            if totalTime <= h:
                right = speed - 1
            else:
                left = speed + 1

        return left