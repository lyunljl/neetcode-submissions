class Leaderboard:

    def __init__(self):
        self.scoreboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scoreboard:
            self.scoreboard[playerId] = score
        else:
            self.scoreboard[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for player, score in self.scoreboard.items():
            heapq.heappush(heap, (-score, player))
        total = 0
        for i in range(K):
            score, player = heapq.heappop(heap)
            total += (-1*score)
        return total



    def reset(self, playerId: int) -> None:
        self.scoreboard.pop(playerId)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
