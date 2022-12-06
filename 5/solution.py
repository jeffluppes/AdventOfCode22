import numpy as np

def solution() -> tuple:
    """solution for day 5"""

    answer_part_1 = calculate_part_one()
    answer_part_2 = calculate_part_two()

    return answer_part_1, answer_part_2


def calculate_part_one() -> str:
    moves, stacks = get_input()
    for m in moves:
        for i in range(int(m[2])):
            stacks[m[1]].append(stacks[m[0]].pop())

    return "".join([stacks[x].pop() for x in stacks])


def calculate_part_two() -> str:
    moves, stacks = get_input()
    for m in moves:
        n = len(stacks[m[0]]) - int(m[2])
        stacks[m[1]].extend(stacks[m[0]][n:])
        stacks[m[0]] = stacks[m[0]][:n]

    return "".join([stacks[x].pop() for x in stacks if len(stacks[x]) > 0])


def get_input():
    """convenience function because we need a fresh stack for part 2"""
    with open("input.txt") as f:
        data: list[str] = f.read().splitlines()

    # writing it out and copy-pasting it was faster than writing a parser
    stacks = {
        "1": ["S", "L", "W"],
        "2": ["J", "T", "N", "Q"],
        "3": ["S", "C", "H", "F", "J"],
        "4": ["T", "R", "M", "W", "N", "G", "B"],
        "5": ["T", "R", "L", "S", "D", "H", "Q", "B"],
        "6": ["M", "J", "B", "V", "F", "H", "R", "L"],
        "7": ["D", "W", "R", "N", "J", "M"],
        "8": ["B", "Z", "T", "F", "H", "N", "D", "J"],
        "9": ["H", "L", "Q", "N", "B", "F", "T"],
    }

    moves = []
    for m in data[10:]:
        n = m.split(" from ")[0].split("move ")[1]
        a = m.split(" from ")[1].split(" to ")[0]
        b = m.split(" to ")[1]
        moves.append([a, b, n])
    return moves, stacks


if __name__ == "__main__":
    print(solution())
