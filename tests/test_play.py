import random
from unittest import TestCase
from schnapsen.bots import RandBot, RdeepBot
from schnapsen.game import SchnapsenGamePlayEngine
from typing import List, Dict



def test_tournament(bots: [any], repeats: int, game_engine: SchnapsenGamePlayEngine) -> None:
    """
        this is a tournament format for testing performance of each bot.
    """

    n = len(bots)
    wins = {str(bot): 0 for bot in bots}
    matches = [(p1, p2) for p1 in range(n) for p2 in range(n) if p1 < p2]

    totalgames = (n * n - n) / 2 * repeats
    playedgames = 0

    print("Playing {} games:".format(int(totalgames)))
    for a, b in matches:
        for r in range(repeats):
            if random.choice([True, False]):
                p = [a, b]
            else:
                p = [b, a]

            winner_id, game_points, score = game_engine.play_game(
                bots[p[0]], bots[p[1]], random.Random(45)
            )

            wins[str(winner_id)] += game_points

            playedgames += 1
            print(
                "Played {} out of {:.0f} games ({:.0f}%): {} \r".format(
                    playedgames, totalgames, playedgames / float(totalgames) * 100, wins
                )
            )
            

# Create bots.
bot1 = RandBot(rand=random.Random(42), name="randbot")
bot2 = RandBot(rand=random.Random(44), name="randbot2")
bot3 = RdeepBot(3,2,rand=random.Random(44), name="RdeepBot")

# Set test parameters
myrepeats = 10
bots = [bot1, bot2, bot3]
engine = SchnapsenGamePlayEngine()
perspective = PlayerPerspective()

# Create test matches
test_tournament(bots, myrepeats, engine)
