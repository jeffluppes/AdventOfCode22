import numpy as np
import string

def solution(data: list) -> tuple:
    '''solution for day 4'''

    job_assignments_pairs = []
    for j in data:
        pairs = j.split(',')
        job_assignments = []
        for pair in pairs:
            start, end = pair.split('-')
            job_assignments.append(set(range(int(start), int(end)+1)))
        
        job_assignments_pairs.append(job_assignments) 

    answer_part_1 = calculate_part_one(job_assignments_pairs)
    answer_part_2 = calculate_part_two(job_assignments_pairs)

    return answer_part_1, answer_part_2

def calculate_part_one(job_assignments_pairs) -> int:
    score = 0
    for A, B in job_assignments_pairs:
        if A.issubset(B) or B.issubset(A):
            score += 1

    return score

def calculate_part_two(job_assignments_pairs) -> int:
    score=0
    for A, B in job_assignments_pairs:
        if len(A.union(B)) == len(A)+len(B):
            score+=1

    # we end up with how many jobs dont overlap at all, so substract these from the total to get the actual answer
    score = len(job_assignments_pairs)-score
    return score

if __name__ == '__main__':
    with open('input.txt') as f:
        data: list[str] = f.read().splitlines()

    print(solution(data))