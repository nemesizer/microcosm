import itertools
from multiprocessing import Pool
from sys import argv

from nltk.corpus import words as english

from data import LINES, keys

if len(argv) < 2:
    argv.append('computer')

combinations = [list(line) for line in itertools.product(*LINES[argv[1]])]

words = set(english.words())


def contains_words(msg):
    for word in msg.split():
        if not (word in words):
            return False
    return True


def offset_lines(lns, offset):
    offset -= 1
    return lns[offset:] + lns[0:offset]


def solve_line(lines):
    start = 0
    key_number = 0

    for key, offset in keys:
        key_number += 1
        lines[13] = key

        copy_lines = offset_lines(lines, offset)

        n = 0
        m = []
        for i in range(20):
            m.append(start)

        for line in copy_lines:
            for letter in line:
                x = ord(letter)
                m[n] += x
                n += 1
                if n == 20:
                    n = 0

        message = ""
        for i in range(20):
            while m[i] > 0:
                m[i] -= 26

            m[i] += ord("z")
            if m[i] == ord("z"):
                m[i] = 32
            message += chr(m[i])

        if contains_words(message):
            print(lines)
            print(key)
            print(message)
            print()


def main():
    pool = Pool()
    pool.map(solve_line, combinations)


if __name__ == '__main__':
    main()
