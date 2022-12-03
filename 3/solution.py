import numpy as np
import string

def solution(backpacks: list) -> tuple:
    '''solution for day 3'''

    answer_part_1 = calculate_part_one(backpacks)
    answer_part_2 = calculate_part_two(backpacks)

    return answer_part_1, answer_part_2

def calculate_part_one(backpacks) -> int:

    special_items = []
    for pack in backpacks:
        # split the pack in left (1st compartment) and right (2nd)
        left = pack[:(len(pack)//2)]
        right = pack[(len(pack)//2):]

        # find items that appear in both sides
        special_items.append(''.join(set(left).intersection(right)))

    score = calculate_sum_of_all_items_in_pack(special_items)
    return score

def calculate_part_two(backpacks) -> int:
    # no need to sort through compartments, but we need to search through backpacks instead
    backpacks = [list(x) for x in backpacks]
    special_items = []
    i = 0

    # find the special item that is in the group of three backpacks and convert it to str
    while(i < len(backpacks)):
        special_items.append(''.join(set([x for x in backpacks[i] if x in backpacks[i+1] and x in backpacks[i+2]])))
        i+=3

    score = calculate_sum_of_all_items_in_pack(special_items)
    return score

def calculate_sum_of_all_items_in_pack(items: list) -> int:
    sum_of_all_items = 0
    for x in items:
        # because string.ascii's index starts at 0, we need to increment the count by 1
        score = string.ascii_letters.index(x)+1
        sum_of_all_items += score

    return sum_of_all_items

if __name__ == '__main__':
    with open('input.txt') as f:
        backpacks: list[str] = f.read().splitlines()

    print(solution(backpacks))