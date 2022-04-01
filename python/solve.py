import gc
import itertools
import random

from multiprocessing import Pool
from sys import argv
from time import perf_counter
from nltk.corpus import words as english

from book import BOOK
from data import LINES, keys

words = set(english.words())

theme = 'computer'
if len(argv) >= 2:
    theme = argv[1]

start_idx = 0
if len(argv) >= 3:
    start_idx = int(argv[2])

if ("random" not in argv):
    print ("SELECTING COMBINATIONS")
    print (LINES[theme])
    combinations = [list(line) for line in itertools.product(*LINES[theme])]
    print ("SELECTED")
else:
    combinations = []

def contains_words(msg):
    for word in msg.split(' '):
        if word not in words:
            return False
    return True


def gen_message(m: list[int], offset: int):
    message = ""
    for i in range(20):
        #m[i] += offset
        m[i] %= 26
        while m[i] > 0:
            m[i] -= 26

        m[i] += 122  # ord("z")
        if m[i] == 122:
            message += ' '
        else:
            message += chr(m[i])
    return message

def random_combination():
    lines = []
    for page in BOOK:
       lines.append(random.choice(page))
    lines.append("key goes here")
    return lines

def solve_lines_key(lines: list[str], key: str, offset: int):

    lines[13] = key

    n = 0
    m = [0] * 20

    lines = lines[offset - 1:] + lines[0:offset - 1]

    for line in lines:
        for letter in line:
            x = ord(letter)
            m[n] += x
            n += 1
            if n == 20:
                n = 0

    message = gen_message(m, offset)

    if contains_words(message):
        print ()
        print ("*****************************************")
        print(lines)
        print(key)
        print(message)
        print ("*****************************************")
        print()

    del message
    del lines
    del m
    del n


def solve_random_combinations(key):
    key, offset = key
    start = perf_counter()
    local_start = start

    max = 1000000

    gc.collect()
    gc.enable()

    i = 0
    while (i<max):
        solve_lines_key(random_combination(), key, offset)
        i += 1
    time = perf_counter() - start
    print(f'finished {max} lines for key {key} in {round(time * 1000, 3)}ms')

   
def solve_key(key):
    key, offset = key
    start = perf_counter()
    local_start = start

    gc.collect()
    gc.enable()

    for i in range(start_idx, len(combinations)):
        solve_lines_key([*(str(line) for line in combinations[i])], key, offset)

        if i % 10 ** 5 == 0 and i != 0:
            now = perf_counter()
            print(f'Key {key} reached {i} in {now - local_start} seconds')
            local_start = now

    time = perf_counter() - start
    print(f'finished key {key} in {round(time * 1000, 3)}ms')


def main():
    if ("random" in argv):
        print(f'Kicking off {len(keys)} processes. Will run until stopped manually')
        while(True):
            with Pool() as pool:
                pool.map(solve_random_combinations, keys)
    else:
        print(f'Kicking off {len(keys)} processes to go through {len(combinations)} combinations each')
        with Pool() as pool:
              pool.map(solve_key, keys)

if __name__ == '__main__':
    main()
