# -*- encoding=utf-8 -*-
def gen_data_from_file(file_name):
    for line in open(file_name):
        yield line


def gen_words(line):
    for word in (w for w in line.split() if w.strip()):
        yield word


def count_words(file_name):
    word_map = {}
    for line in gen_data_from_file(file_name):
        for word in gen_words(line):
            if word not in word_map:
                word_map[word] = 0
            word_map[word] += 1
    return word_map


def count_total_chars(file_name):
    total = 0
    for line in gen_data_from_file(file_name):
        total += len(line)
    return total


print(count_words('read_file.py'), count_total_chars('read_file.py'))
