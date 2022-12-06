import numpy as np


def solution(data) -> tuple:
    """solution for day 5"""

    answer_part_1 = calculate_part_one(data)
    answer_part_2 = calculate_part_two(data)

    return answer_part_1, answer_part_2


def find_marker_in_string(data: str, n: int):
    i = n - 1
    while i < len(data):
        if len(set(data[i : i + n])) == n:
            return i + n
        i += 1


def calculate_part_one(data) -> str:
    return find_marker_in_string(data, 4)


def calculate_part_two(data) -> str:
    return find_marker_in_string(data, 14)


def get_input():
    """convenience function"""
    with open("input.txt") as f:
        data: list[str] = f.read().splitlines()

    return data[0]


if __name__ == "__main__":
    data = get_input()
    print(solution(data))
