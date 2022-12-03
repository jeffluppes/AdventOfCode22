import numpy as np

VALUES = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}
def solution(moves: list) -> tuple:
    '''solution for day 2'''

    moves = [(VALUES.get(x[0]), VALUES.get(x[1])) for x in moves]

    answer_part_1 = calculate_score(moves)
    answer_part_2 = calculate_part_two(moves)

    return answer_part_1, answer_part_2

def calculate_part_two(moves) -> int:
    our_moves = []
    for m in moves:
        if m[1] == 2:
            our_moves.append(m[0])
        elif m[1] == 1:
            # we need to lose
            if m[0] == 1:
                our_moves.append(3)
            elif m[0] == 2:
                our_moves.append(1)
            else:
                our_moves.append(2)
        else:
            # we need to win
            if m[0] == 1:
                our_moves.append(2)
            elif m[0] == 2:
                our_moves.append(3)
            else:
                our_moves.append(1)
    
    score = 0
    for i, m in enumerate(our_moves):
        score += m
        score += calculate_match_bonus((moves[i][0], m))

    return score

def calculate_score(moves: list) -> int:
    score = 0
    for m in moves:
        score += m[1]
        score += calculate_match_bonus(m)

    return score

def calculate_match_bonus(m) -> int:
    if m[0] == m[1]:
        return 3
    elif np.absolute(m[0] - m[1]) == 1:
        if m[1] > m[0]:
            return 6
        else:
            return 0
    else:
        if m[1] < m[0]:
            return 6
        else:
            return 0

if __name__ == '__main__':
    with open('input.txt') as f:
        moves: list[str] = f.read().splitlines()

    moves = [tuple(x.split(' ')) for x in moves]
    print(solution(moves))