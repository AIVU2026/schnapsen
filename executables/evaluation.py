import math
import random
import pathlib
import re


from typing import Optional, List


def distance(file1: List[int], file2: List[int]) -> int:
    '''
        it chechs Euclidian similarity of the data set.
    '''
    if len(file1) != len(file2):
        raise ValueError('Those have different number of elements!')
            
    
    if list1[-1] == 1 and list2[-1] == 1:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(list1[:-1], list2[:-1])))
    
    else:
        return -1
    
def extract_numbers_from_file(file_path):
    '''
        It cleans the output files with spliting into the numbers of digits(174).
        Each sublist in the list represent the game record of each round.
    '''
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = re.findall(r'\b\d+\b', content)
            divided_lists = [numbers[i * 174:(i + 1) * 174] for i in range(int(len(numbers)/174))]
            return divided_lists
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    

ObserverBot_move_file_path = '/Users/song/Projects/schnapsen/Observer_replay_memories/random_random_10k_games_100_to_compare-1.txt'
RdeepBot_move_file_path = '/Users/song/Projects/schnapsen/Observer_replay_memories/random_random_10k_games_100.txt'

numbers_list1 = extract_numbers_from_file(ObserverBot_move_file_path)
numbers_list2 = extract_numbers_from_file(RdeepBot_move_file_path)

print(len(numbers_list2))
# print(len(numbers_list1))

