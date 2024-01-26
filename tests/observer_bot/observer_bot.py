from random import Random
from schnapsen.bots import MLPlayingBot, train_ML_model
from schnapsen.game import SchnapsenGamePlayEngine, Bot


def collect_data(bot1: Bot, bot2: Bot, games_played: int) -> None:
    """Let MLDataBot play games vs opponent and store the replay memory.
    :param: bot1: HowToPlay_MLDataBot: "how to play" instance of MLDataBot.
    :param: bot2: Opponent bot."""

    engine = SchnapsenGamePlayEngine()

    for nr in range(games_played):
        engine.play_game(bot1=bot1, bot2=bot2, rng=Random(nr))
        
        # Print game results.
        print(f"Games played {nr}")


def make_model(path_memory, path_model) -> None:
    """Train model with replay memory.
    :param: path_memory: path to the replay memory file.
    :param: path_model: path to the model file"""
    train_ML_model(replay_memory_location=path_memory, model_location=path_model, model_class="LR")
