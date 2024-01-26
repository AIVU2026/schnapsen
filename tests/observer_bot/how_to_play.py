from schnapsen.bots.ml_bot import MLDataBot, create_state_and_actions_vector_representation
from schnapsen.game import PlayerPerspective, Trick
from typing import cast


class HowToPlay_MLDataBot(MLDataBot):
    """Subclass of MLDatabot: only change is won_label is set to True so that all games in the replay memory are recorded as a win.
    When our bot learns from the replay memory it will learn to play like the bot it's trying to copy whether it wins or loses.
    The goal is to copy the complete behaviour of a bot, not only the behaviour that leads to a won game."""


    def notify_game_end(self, won: bool, perspective: PlayerPerspective) -> None:
        game_history: list[tuple[PlayerPerspective, Trick]] = cast(list[tuple[PlayerPerspective, Trick]], perspective.get_game_history()[:-1])
        won_label = True

        for round_player_perspective, round_trick in game_history:

            if round_trick.is_trump_exchange():
                leader_move = round_trick.exchange
                follower_move = None
            else:
                leader_move = round_trick.leader_move
                follower_move = round_trick.follower_move

            if round_player_perspective.am_i_leader():
                follower_move = None

            state_actions_representation = create_state_and_actions_vector_representation(
                perspective=round_player_perspective, leader_move=leader_move, follower_move=follower_move)

            with open(file=self.replay_memory_file_path, mode="a") as replay_memory_file:
                replay_memory_file.write(f"{str(state_actions_representation)[1:-1]} || {int(won_label)}\n")


class HowNotToPlay_MLDataBot(MLDataBot):
    """won_label is set to False, this way all games in the replay memory are recorded as a loss.
    We mark all games as lost games to show the observer bot examples of things not to do.
    In this case random behaviour is shown to lead to a loss in the replay memory"""


    def notify_game_end(self, won: bool, perspective: PlayerPerspective) -> None:
        game_history: list[tuple[PlayerPerspective, Trick]] = cast(list[tuple[PlayerPerspective, Trick]], perspective.get_game_history()[:-1])
        won_label = False

        for round_player_perspective, round_trick in game_history:

            if round_trick.is_trump_exchange():
                leader_move = round_trick.exchange
                follower_move = None
            else:
                leader_move = round_trick.leader_move
                follower_move = round_trick.follower_move

            if round_player_perspective.am_i_leader():
                follower_move = None

            state_actions_representation = create_state_and_actions_vector_representation(
                perspective=round_player_perspective, leader_move=leader_move, follower_move=follower_move)

            with open(file=self.replay_memory_file_path, mode="a") as replay_memory_file:
                replay_memory_file.write(f"{str(state_actions_representation)[1:-1]} || {int(won_label)}\n")
