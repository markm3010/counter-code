import re


def selfish_meter(file_in):
    fh = open(file_in, "r")
    data = fh.read()
    fh.close()
    # print(data)

    searcher = re.compile(r'\bI\b|\bI\'ve\b|\bI\'[md]\b|\bmy\b|\bmine\b')
    matches = searcher.finditer(data)
    i = 0
    print('\nSelfish words found:')
    for match in matches:
        print(match.group(0), end=' ')
        i += 1

    return i


if __name__ == '__main__':
    filename = "random-blog.txt"
    count = selfish_meter(filename)
    print(f'\n\nnumber of selfish words found: {count}')
