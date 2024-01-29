from schnapsen.game import SchnapsenGamePlayEngine
from schnapsen.bots import RandBot, RdeepBot, MLPlayingBot
from observer_bot import collect_data, make_model
from observer_bot import HowToPlay_MLDataBot, HowNotToPlay_MLDataBot
from random import Random
import settings
import pathlib


bot_to_mimic = RdeepBot(num_samples=settings.samples, depth=settings.depth, rand=Random(settings.rand_seed))  # Bot we want to mimic.
opponent_bot = RdeepBot(num_samples=settings.samples, depth=settings.depth, rand=Random(settings.rand_seed))  # Opponent bot.

# Path and file names for storing replay memory and training models.
# Make sure to change file names for different versions of ObserverBot! Path names can remain the same.
memory_file_name = f"memory_{settings.gamesplayed}_{settings.hntp_ratio}_{settings.samples}{settings.depth}_{settings.method}"
model_file_name = f"model_{settings.gamesplayed}_{settings.hntp_ratio}_{settings.samples}{settings.depth}_{settings.method}"
memory_path = pathlib.Path(f"schnapsen/tests/observer_bot/ml_path/{memory_file_name}.txt")
model_path = pathlib.Path(f"schnapsen/tests/observer_bot/ml_path/{model_file_name}")


# Collects game replay memory as the bot we want to mimic.
how_to_play_bot = HowToPlay_MLDataBot(bot=bot_to_mimic, replay_memory_location=memory_path)

# Collects game replay memory as the bot we don't want to mimic.
how_not_to_play_bot = HowNotToPlay_MLDataBot(bot=RandBot(rand=Random(1)), replay_memory_location=memory_path)


# Run games to collect replay data and create a model for ObserverBot.
def make_ml_model() -> None:
    collect_data(how_to_play_bot, opponent_bot, settings.gamesplayed)
    collect_data(how_not_to_play_bot, opponent_bot, (int(settings.gamesplayed * settings.hntp_ratio)))

    make_model(memory_path, model_path)


make_ml_model()




if settings.auto_fill_model:
    model_name = f"model_{settings.gamesplayed}_{settings.hntp_ratio}_{settings.samples}{settings.depth}_{settings.method}"
else:
    model_name = settings.manual_model_name

model_file_path = pathlib.Path(f"schnapsen/tests/observer_bot/ml_path/{model_name}")
control = RdeepBot(num_samples=settings.samples, depth=settings.depth, rand=Random(settings.rand_seed), name="control")
opponent = RdeepBot(num_samples=settings.samples, depth=settings.depth, rand=Random(settings.rand_seed), name="opponent")
observer_b = MLPlayingBot(model_location=model_file_path, name="ObserverBot")


def play(n, bot) -> float:
    engine = SchnapsenGamePlayEngine()
    won = 0

    for num in range(n):
        name, game_points, score = engine.play_game(bot1=bot, bot2=opponent, rng=Random(num + 1000))
        if name == bot:
            won += 1
    
    win_percent = (won/n) * 100
    print(f"name: {bot}, win: {won}/{n} --> {win_percent}%")
    return win_percent


def evaluate_model() -> None:
    result = play(settings.evaluation_games, observer_b) - play(settings.evaluation_games, control)
    print(result)



evaluate_model()
