"""Convert decimal numbers to binary and hex from a given file"""
import sys
import os
import time

def convert_hex(number: int) -> str:
    """Converts a given number to hexadecimal"""
    if number < 0:
        sign = "-"
        number = abs(number)
    else:
        sign = ""
    hex_result = ""
    hex_digits = "0123456789ABCDEF"
    while number > 0:
        remainder = number % 16
        hex_result = hex_digits[remainder] + hex_result
        number //= 16
    return sign + hex_result

def convert_binary(number: int) -> str:
    """Converts a given number to binary"""
    if number < 0:
        sign = "-"
        number = abs(number)
    else:
        sign = ""
    binary_result = ""
    while number > 0:
        remainder = number % 2
        binary_result = str(remainder) + binary_result
        number //= 2
    return sign + binary_result

def load_file(file_path: str) -> list[float]:
    """Loads the file of numbers given path"""
    file_numbers = []
    with open(file_path, 'r', encoding='utf-8') as file_content:
        file_lines = file_content.readlines()
        for line in file_lines:
            try:
                file_numbers.append(int(line.strip()))
            except ValueError:
                continue
    return file_numbers

def create_file(file_path: str, write_results: list[str], delta_time: float) -> None:
    """Creates a file with the same results shown in the terminal"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('Results\n')
        for single_result in write_results:
            file.write(single_result + '\n')
        file.write(f'Execution time was: {delta_time}')

path = sys.argv[1]
if len(sys.argv) > 1:
    if os.path.isfile(path) and os.path.exists(path):
        startTime = time.time()
        numbers = load_file(path)
        results = []
        for num in numbers:
            result = f'Decimal: {num}\t Bin: {convert_binary(num)}\t Hex: {convert_hex(num)}'
            results.append(result)
            print(result)
        delta = round(time.time() - startTime, 4)
        create_file('ConvertionResults.txt', results, delta)
        print(f'Execution time: {delta}')
    else:
        print('Something went wrong trying to read the file')
else:
    print('No file was provided')
