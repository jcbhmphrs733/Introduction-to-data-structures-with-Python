```py
class Player:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level
```
```py
class PlayerQueue:
    def __init__(self):
        self.players = []

    def enqueue_player(self, player):
        self.players.append(player)

    def dequeue_player(self):
        if not self.is_empty():
            dequeued_player = self.players.pop(0)
            return dequeued_player
        else:
            return None
        
    def pair_players(self):
        paired_players = []

        # Group players by skill level
        skill_levels_dict = {}
        for player in self.players:
            skill_levels_dict.setdefault(player.skill_level, []).append(player)

        # Pair players with similar skill levels
        for skill, players in skill_levels_dict.items():
            while len(players) >= 2:
                player1 = players.pop()
                player2 = players.pop()
                pair = (player1, player2)
                paired_players.append(pair)

        return paired_players
```
[back](/queues.md)