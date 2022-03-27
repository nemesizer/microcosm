import itertools

from nltk.corpus import words as english

from data import LINES, keys

combinations = [list(line) for line in itertools.product(*LINES['computer'])]

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
    for lines in combinations:
        solve_line(lines)


if __name__ == '__main__':
    main()
