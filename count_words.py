import re

'''
Count number of words in a file
'''


def count_words(f: object) -> object:
    with open(f) as fh:
        data_src = fh.read()
        word_detector = re.compile(r'(\b[1-9a-z?.-]+)(\s|\n)?', re.IGNORECASE)

        data_set = word_detector.finditer(data_src)
        ct = 0
        for word in data_set:
            print(word.group(0), end='')
            ct += 1

        return ct


if __name__ == '__main__':
    filename = "word_probs.txt"
    word_ct = count_words(filename)
    print(f'\n\nNumber of words in {filename}: {word_ct}')
