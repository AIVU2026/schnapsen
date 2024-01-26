from random import Random
from schnapsen.bots import RandBot
from observer_bot import collect_data, make_model
from how_to_play import HowToPlay_MLDataBot, HowNotToPlay_MLDataBot
import pathlib


"""
Run this python script to train a model that the ObserverBot can use to mimic other bots.
Variables gamesplayed, bot_to_mimic and opponent_bot can be changed for the desired model.
Make sure that each model has it's own unique memory_file_name and model_file_name.
Other variables can be left as they are.
"""


gamesplayed: int = 1000                 # Number of games played to collect data from.
bot_to_mimic = RandBot(rand=Random(1))  # Bot we want to mimic: Randbot is a placeholder for now.
opponent_bot = RandBot(rand=Random(2))  # Opponent bot.


# Path and file names for storing replay memory and training models.
# Make sure to change file names for different versions of ObserverBot! Path names can remain the same.
memory_file_name = "test_memory"
model_file_name = "test_model"
memory_path = pathlib.Path(f"schnapsen/tests/observer_bot/ml_path/{memory_file_name}.txt")
model_path = pathlib.Path(f"schnapsen/tests/observer_bot/ml_path/{model_file_name}")


# Collects game replay memory as the bot we want to mimic.
how_to_play_bot = HowToPlay_MLDataBot(bot=bot_to_mimic, replay_memory_location=memory_path)

# Collects game replay memory as the bot we don't want to mimic.
how_not_to_play_bot = HowNotToPlay_MLDataBot(bot=RandBot(rand=Random(1)), replay_memory_location=memory_path)



# Run games to collect replay data and create a model for ObserverBot.
collect_data(how_to_play_bot, opponent_bot, gamesplayed)
collect_data(how_not_to_play_bot, opponent_bot, gamesplayed)

make_model(memory_path, model_path)


# To create an instance of ObserverBot to play games with copy the following code 
# and change model_name to the model you want ObserverBot to play like.
# observer_bot also needs to be initialized before use.
"""model_name = "--model name--"
model_file_path = pathlib.Path(f"schnapsen/tests/observer_bot/ml_path/{model_name}")
observer_bot = MLPlayingBot(model_location=model_file_path, name="ObserverBot")"""
