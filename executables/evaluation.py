import math
import random
import pathlib
import re
from typing import List


from typing import Optional, List


def distance_round(list1: List[int], list2: List[int]) -> int:
    '''
        it chechs Euclidian similarity of the data set.
    '''
    if len(list1) != len(list2):
        raise ValueError('Those have different number of elements!')
            
    return math.sqrt(sum((int(a) - int(b)) ** 2 for a, b in zip(list1[:-1], list2[:-1])))
    
def extract_moves_from_file(file_path):
    '''
        It cleans the output files with spliting into the moves of digits(174).
        Each sublist in the list represent the game record of each round.
    '''
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            moves = re.findall(r'\b\d+\b', content)
            divided_lists = [moves[i * 174:(i + 1) * 174] for i in range(int(len(moves)/174))]
            return divided_lists
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def distance_game(list1: List[List[int]], list2: List[List[int]]) -> int:
    '''
        It caculates a Euclidian distance for whole rounds(game).
        return: average distance between the moves.
    '''
    sum = 0
    count = 0
    for i in range(len(list1)):
        if (int(list1[i][-1]) == 1) and (int(list2[i][-1]) == 1):
            sum += distance_round(list1[i],list2[i])
            count += 1
    print(f'sum of distance: {sum} and number of comparation: {count}')
    return round(sum/count,3)

ObserverBot_move_file_path = '/Users/song/Projects/schnapsen/Observer_replay_memories/random_random_10k_games_100_to_compare-1.txt'
RdeepBot_move_file_path = '/Users/song/Projects/schnapsen/Observer_replay_memories/random_random_10k_games_100.txt'

moves_list1 = extract_moves_from_file(ObserverBot_move_file_path)
moves_list2 = extract_moves_from_file(RdeepBot_move_file_path)

# print(moves_list2[0])
print(distance_game(moves_list1,moves_list2))
# print(len(moves_list1))

