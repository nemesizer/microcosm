import gc
import itertools
from functools import cache
from multiprocessing import Pool
from sys import argv
from time import perf_counter

from nltk.corpus import words as english

from data import LINES, keys

words = set(english.words())

theme = 'computer'
if len(argv) == 2:
    theme = argv[1]

combinations = [list(line) for line in itertools.product(*LINES[theme])]


@cache
def not_word_english(word):
    return word not in words


def contains_words(msg):
    for word in msg.split(' '):
        if not_word_english(word):
            return False
    return True


def gen_message(m: list[int]):
    message = ""
    for i in range(20):
        m[i] %= 26
        while m[i] > 0:
            m[i] -= 26

        m[i] += 122  # ord("z")
        if m[i] == 122:
            message += ' '
        else:
            message += chr(m[i])
    return message


def solve_lines_key(lines, key: str, offset: int):
    lines[13] = key

    n = 0
    m = [0] * 20

    for line in lines[offset - 1:] + lines[0:offset - 1]:
        for letter in line:
            x = ord(letter)
            m[n] += x
            n += 1
            if n == 20:
                n = 0

    message = gen_message(m)

    if contains_words(message):
        print(lines)
        print(key)
        print(message)
        print()

    del message
    del m
    del n
    del lines
    gc.collect()


def solve_key(key):
    # import cProfile
    # import pstats

    key, offset = key
    start = perf_counter()

    # with cProfile.Profile() as pr:

    for lines in combinations:
        solve_lines_key([*lines], key, offset)

    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()

    time = perf_counter() - start
    print(f'finished key {key} in {round(time * 1000, 3)}ms')


def main():
    print(f'Kicking off {len(keys)} processes to go through {len(combinations)} combinations each')
    with Pool() as pool:
        pool.map(solve_key, keys)


if __name__ == '__main__':
    main()
