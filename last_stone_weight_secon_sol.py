class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if(first == second):
                continue
            else:
                heapq.heappush(stones, -abs(first-second))

        return -stones[0] if stones else 0
