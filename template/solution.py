def solution(readings: list) -> int:
    return 1

if __name__ == '__main__':
    with open('input.txt') as f:
        readings: list[str] = f.readlines()

    print(solution(readings))