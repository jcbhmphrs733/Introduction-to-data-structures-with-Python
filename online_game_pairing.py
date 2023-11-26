from queue import Queue

class Player:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

def pair_players(queue):
    paired_players = []
    
    # Sort the queue based on skill level
    sorted_players = sorted(list(queue.queue), key=lambda x: x.skill_level)

    while len(sorted_players) >= 2:
        player1 = sorted_players.pop(0)
        player2 = sorted_players.pop(0)
        pair = (player1, player2)
        paired_players.append(pair)
        print(f"Paired: {player1.name} (Skill: {player1.skill_level}) and {player2.name} (Skill: {player2.skill_level})")

    return paired_players

def main():
    player_queue = Queue()

    # Add players to the queue with skill levels
    player_queue.put(Player("Player1", 1200))
    player_queue.put(Player("Player2", 1300))
    player_queue.put(Player("Player3", 1100))
    player_queue.put(Player("Player4", 1250))
    player_queue.put(Player("Player5", 1400))

    # Pair players based on skill levels and get the result
    paired_players = pair_players(player_queue)

    # Handle any remaining players (odd number of players)
    if player_queue.qsize() > 0:
        print("Remaining players:")
        while not player_queue.empty():
            remaining_player = player_queue.get()
            print(remaining_player.name)

if __name__ == "__main__":
    main()