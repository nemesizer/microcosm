import gc
import itertools
import random
import time
from multiprocessing import Pool
from sys import argv
from time import perf_counter

from nltk.corpus import words as english

from book import BOOK
from data import LINES, keys

words = set(word.lower() for word in english.words())

# theme defaults to 'computer', since it's quick... 
# specify the theme you want on the command line, such as:
# python solve.py washington

theme = 'computer'

if len(argv) >= 2:
    theme = argv[1]

if ("random" not in argv):
    print ("SELECTING COMBINATIONS")
    print (LINES[theme])
    count = 0
    combinations = [list(line) for line in itertools.product(*LINES[theme])]
    print ("SELECTED " + str(len(combinations)) + " COMBINATIONS")
else:
    combinations = []


def contains_words(msg):
    # determine if a message is made up exclusively of English words or not:
    for word in msg.split(' '):
        if word not in words:
            # message contains something which is not an English word
            return False
    return True


def gen_message(m: list[int], offset: int):
    # generate the final output message
    message = ""
    for i in range(20):
        m[i] %= 26
        while m[i] > 0:
            m[i] -= 26

        m[i] += 122  # ord("z")
        if m[i] == 122:
            # convert 'z' into a space
            message += ' '
        else:
            message += chr(m[i])
    return message


def random_combination():
    # generate a random combination of lines from the book:
    return [random.choice(page) for page in BOOK] + ['key goes here']


def solve_lines_key(lines: list[str], key: str, offset: int):
    n = 0
    m = [0] * 20

    # apply an offset. This means instead of starting at line 1,
    # we start with the line specified by the offset, and then
    # cycle back round to the beginning.

    lines = lines[offset - 1:-1] + [key] + lines[0:offset - 1] 

    assert (len(lines) == 14)

    # this is the main loop. Loop through all characters, and add them up:
    for line in lines:
        for letter in line:
            x = ord(letter)
            m[n] += x
            n += 1
            if n == 20:
                n = 0

    message = gen_message(m, offset)

    if contains_words(message):
        print("\n*****************************************")
        print("Offset = " + str(offset))
        print(lines)
        print(key)
        print("*****************************************")
        print(message)
        print("*****************************************\n")

    del message
    del lines
    del m
    del n


def solve_random_combinations(key: str, n=10 ** 6):
    """
    Tries a bunch of random combinations. Won't log anything until it finds something.
    :param key:
    :param n: number of combinations to try
    """
    key, offset = key

    gc.collect()
    gc.enable()

    for i in range(n):
        solve_lines_key(random_combination(), key, offset)
        if (offset > 1):
            # also try with offset of 1 (which means no offset), just in case:
            solve_lines_key(random_combination(), key, 1)


def solve_key(key: str):
    key, offset = key
    start = perf_counter()
    local_start = start

    gc.collect()
    gc.enable()

    for i in range(0, len(combinations)):
        solve_lines_key([*(str(line) for line in combinations[i])], key, offset)
        if (offset > 1):
            solve_lines_key([*(str(line) for line in combinations[i])], key, 1)


def main():
    if ("random" in argv):
        print(f'Kicking off {len(keys)} processes. Will run until stopped manually')
        while(True):
            with Pool() as pool:
                pool.map(solve_random_combinations, keys)
                # just not to overwork the cpu idk
                time.sleep(1)
    else:
        print(f'Kicking off {len(keys)} processes to go through {len(combinations)} combinations each')
        with Pool() as pool:
              pool.map(solve_key, keys)

if __name__ == '__main__':
    main()
