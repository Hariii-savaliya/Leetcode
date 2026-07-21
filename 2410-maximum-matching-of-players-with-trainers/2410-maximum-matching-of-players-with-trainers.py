class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        c = 0
        i = j = 0
        players.sort()
        trainers.sort()
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                c += 1
                i += 1
            j += 1
        return c

        