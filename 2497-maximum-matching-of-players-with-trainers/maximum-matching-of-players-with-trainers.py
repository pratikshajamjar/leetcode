class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j, res = len(players) - 1, len(trainers) - 1, 0
        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                res += 1
                i, j = i - 1, j - 1
            else:
                i -= 1
        return res