"""Compute statistics from a given file containing numbers"""
import sys
import os.path
import time

def mean(nums: list[float]) -> float:
    """Calculates the mean from list"""
    buffer = 0
    for num in nums:
        buffer += num
    return buffer / len(nums)

def median(nums: list[float]) -> float:
    """Calculates the median from list"""
    for i, j in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    return nums[n//2]

def mode(nums: list[float]) -> float:
    """Calculates the mode(s) from list"""
    element_count = {}
    for number in nums:
        if number in element_count:
            element_count[number] += 1
        else:
            element_count[number] = 1
    max_frequency = max(element_count.values())
    modes = [key for key, value in element_count.items() if value == max_frequency]
    return modes

def variance(nums: list[float], mu: float) -> float:
    """Calculates the variance from list and mu"""
    deviations = []
    for number in nums:
        deviations.append((number-mu) ** 2)
    return mean(deviations)

def standard_deviation(var: float) -> float:
    """Calculates the standard deviation from variance"""
    return var ** 0.5

def load_file(file_path: str) -> list[float]:
    """Loads the file of numbers given path"""
    file_numbers = []
    with open(file_path, 'r', encoding='utf-8') as file_content:
        file_lines = file_content.readlines()
        for line in file_lines:
            try:
                file_numbers.append(float(line.strip()))
            except ValueError:
                continue
    return file_numbers

def create_file(file_path: str, write_results: list[str], delta_time: float) -> None:
    """Creates a file with the same results shown in the terminal"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('Results\n')
        file.write(write_results + '\n')
        file.write(f'Execution time was: {delta_time}')

path = sys.argv[1]
if len(sys.argv) == 2:
    if os.path.isfile(path) and os.path.exists(path):
        startTime = time.time()
        numbers = load_file(path)
        mu_value = mean(numbers)
        median_value = median(numbers)
        mode_value = mode(numbers)
        var_value = variance(numbers, mu_value)
        std = standard_deviation(var_value)
        result = f'Count: {len(numbers)}\nMean: {mu_value}\nMedian: {median_value}\nMode: \
            {mode_value}\nStandard Deviation: {std}\nVariance: {var_value}'
        delta = round(time.time() - startTime, 4)
        print(result)
        create_file('StatisticsResults.txt', result, delta)
        print(f'Execution time: {delta}')
    else:
        print('Something went wrong trying to read the file')
else:
    print('No file was provided')
