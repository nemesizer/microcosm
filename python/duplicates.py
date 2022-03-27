from book import BOOK

lines = []

dups = {}

words = {}

for page in BOOK:
    for line in page:
        if line in lines:
            if line not in dups:
                dups[line] = 0
            dups[line] += 1
        else:
            lines.append(line)

        for word in line.split(' '):
            if word not in words:
                words[word] = 0
            words[word] += 1

print(dups)

print('\n'.join(list(f'{k}: {v}' for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True))))
