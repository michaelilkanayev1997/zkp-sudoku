import random

# The Sudoku Puzzle
puzzle = [
    5, 3, 0, 0, 7, 0, 0, 0, 0, \
    6, 0, 0, 1, 9, 5, 0, 0, 0, \
    0, 9, 8, 0, 0, 0, 0, 6, 0, \
    8, 0, 0, 0, 6, 0, 0, 0, 3, \
    4, 0, 0, 8, 0, 3, 0, 0, 1, \
    7, 0, 0, 0, 2, 0, 0, 0, 6, \
    0, 6, 0, 0, 0, 0, 2, 8, 0, \
    0, 0, 0, 4, 1, 9, 0, 0, 5, \
    0, 0, 0, 0, 8, 0, 0, 7, 9
]

# The Sudoku Solution
solution = [
    5, 3, 4, 6, 7, 8, 9, 1, 2, \
    6, 7, 2, 1, 9, 5, 3, 4, 8, \
    1, 9, 8, 3, 4, 2, 5, 6, 7, \
    8, 5, 9, 7, 6, 1, 4, 2, 3, \
    4, 2, 6, 8, 5, 3, 7, 9, 1, \
    7, 1, 3, 9, 2, 4, 8, 5, 6, \
    9, 6, 1, 5, 3, 7, 2, 8, 4, \
    2, 8, 7, 4, 1, 9, 6, 3, 5, \
    3, 4, 5, 2, 8, 6, 1, 7, 9
]

# Transform each value into a list of three identical elements
transformed_puzzle = [[value]*3 for value in solution]

# Chunk it into rows
def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

 # Transpose the puzzle to work with columns instead of rows
def transpose(puzzle):
    return list(map(list, zip(*puzzle)))

# Check that all digits exist only once in a packet
def all_digits_exist_once(iterable):
    digit_mask = [0 for i in range(9)]
    for x in iterable:
        digit_mask[x-1]=1
    return all(digit_mask)

# Check boolean value to get better answer
def check_bool(boolean):
    if (boolean):
        return "Pass"
    else:
        return "Fail"

# Shuffle cards in a packet
def shuffle_packet(packet):
    random.shuffle(packet)
    return packet