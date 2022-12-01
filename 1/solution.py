from collections import Counter

def solution(readings: list) -> int:
    '''solution for day 1'''

    counter = Counter()
    elves = 0
    for line in readings:
        if line == '\n':
            elves += 1
        else:
            counter[elves] += int(line)

    # Find the amount of calories carried by the winner
    answer_part_1 = counter.most_common(1)[0][1]

    # Calculate the amount of calories carried by the top 3
    answer_part_2 = sum_of_n_elves(counter, 3)

    return answer_part_1, answer_part_2

def sum_of_n_elves(counter: Counter, n: int) -> int:
    '''find the sum of all the calories carried by the top-n elves'''
    total_calories = sum([x[1] for x in list(counter.most_common(n))])
    return total_calories

if __name__ == '__main__':
    with open('input.txt') as f:
        readings: list[str] = f.readlines()

    print(solution(readings))