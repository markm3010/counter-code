import re

'''
Take a filename from count_the_chars(), open
file, read file, and create a regular expression.
Then use finditer() to read the data into "m".  

After that, print each character found (including 
spaces, backslashes, dots and newline characters).

Lastly, it counts characters as it prints each 
one, and returns the total count to the caller.
'''


def get_char_ct(filename):
    with open(filename, 'r') as file1:
        contents = file1.read()
        searcher = re.compile(r'[\w\\\n\s.]')
        m = searcher.finditer(contents)

        i = 0
        for match in m:
            print(match.group(0), end='')
            if match.group(0) == '\n':
                i += 2           # this accounts for the 2 characters in a newline (\r\n)
            else:
                i += 1
        return i


def count_the_chars():
    filename = "word_probs.txt"
    char_ct = get_char_ct(filename)
    print(f'\n\nCharacter in {filename}: {char_ct}')


if __name__ == '__main__':
    count_the_chars()
