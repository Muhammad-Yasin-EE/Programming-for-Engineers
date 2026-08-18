# Name: Muhammad Yasin
# CMS ID: 033-25-0040
# Class: BEE-II
# Assignment 02 - Data Analysis (Mean, Median, Mode)

"""
Data Analysis (Mean, Median, Mode)
Assignment 02 - Python

A program that accepts a list of numbers from the user and computes
the mean, median, and mode without using built-in libraries
(no 'statistics', no 'numpy').
"""


def get_numbers():
    """Take space-separated numbers from the user and return them as a list."""
    raw_input_str = input("Enter numbers (separated by spaces): ")
    parts = raw_input_str.split()

    numbers = []
    for part in parts:
        try:
            # Try int first, fall back to float if it has a decimal point
            if "." in part:
                numbers.append(float(part))
            else:
                numbers.append(int(part))
        except ValueError:
            print(f"Skipping invalid value: {part}")

    return numbers


def calculate_mean(numbers):
    """Return the average of the list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def calculate_median(numbers):
    """Return the median (middle value) of the list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 1:
        # Odd number of elements -> middle value
        return sorted_numbers[mid]
    else:
        # Even number of elements -> average of two middle values
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


def calculate_mode(numbers):
    """Return the mode(s) of the list of numbers as a list."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())

    # If every number appears exactly once, there is no mode
    if max_freq == 1:
        return []

    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes


def display_results(numbers):
    """Calculate and print mean, median, and mode."""
    print(f"\nDataset: {numbers}")

    mean_value = calculate_mean(numbers)
    print(f"Mean: {mean_value}")

    median_value = calculate_median(numbers)
    print(f"Median: {median_value}")

    modes = calculate_mode(numbers)
    if len(modes) == 0:
        print("Mode: No mode")
    elif len(modes) == 1:
        print(f"Mode: {modes[0]}")
    else:
        print(f"Mode: {modes} (Multiple modes)")


def main():
    numbers = get_numbers()

    if len(numbers) == 0:
        print("No valid numbers were entered. Exiting program.")
        return

    display_results(numbers)


if __name__ == "__main__":
    main()
