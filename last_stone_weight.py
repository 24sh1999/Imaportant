class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            x = stones.pop()
            y = stones.pop()
            if x == y:
                continue
            ret = abs(x - y)
            pos = -1
            for i in range(len(stones)):
                if ret <= stones[i]:
                    pos = i
                    break
            if pos == -1:
                stones.append(ret)
            else:
                stones.insert(pos, ret)

        if len(stones) == 1:
            return stones[0]
        return 0
