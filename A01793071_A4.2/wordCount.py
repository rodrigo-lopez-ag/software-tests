"""Counts frequency of words from a given file"""
import sys
import os
import time


def count_word(words: list[str]) -> dict[str, int]:
    """Returns a dictionary with word frequency of given list"""
    frequency_count = {}
    for word in words:
        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1
    return frequency_count


def load_file(file_path: str) -> list[str]:
    """Loads the file of words given path"""
    words = []
    with open(file_path, 'r', encoding='utf-8') as file_content:
        lines = file_content.readlines()
        for line in lines:
            words.append(line.strip())
    return words


def create_file(file_path: str, write_results: list[str],
                delta_time: float) -> None:
    """Creates a file with the same results shown in the terminal"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('Results\n')
        for single_result in write_results:
            file.write(single_result + '\n')
        file.write(f'Execution time was: {delta_time}')


path = sys.argv[1]
if len(sys.argv) == 2:
    if os.path.isfile(path) and os.path.exists(path):
        startTime = time.time()
        results = []
        word_list = load_file(path)
        frequencies = count_word(word_list)
        for key, value in frequencies.items():
            result = f'{key}    {value}'
            results.append(result)
            print(result)
        delta = round(time.time() - startTime, 4)
        create_file('WordCountResults.txt', results, delta)
        print(f'Execution time: {delta}')
    else:
        print('Something went wrong trying to read the file')
else:
    print('No file was provided')
