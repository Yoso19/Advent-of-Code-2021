import collections
from functools import reduce
def part_1():
    report = [int(x) for x in open('day1.txt').readlines()]
    print('Part 1 solution:', sonar_sweep(report))
    part_2(report)

def sonar_sweep(report):
    counter = 0
    for a, b in zip(report[:-1], report[1:]):
        if a < b:
            counter += 1
    return counter

def part_2(report):
    sums = [a+b+c for a, b, c in zip(report[:-2], report[1:-1], report[2:])]
    print('Part 2 solution:', sonar_sweep(sums))

if __name__ == '__main__':
    part_1()