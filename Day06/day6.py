from collections import Counter

def lanternfish():
    fish = Counter([int(x) for x in open('day6.txt').readline().split(',')])
    for day in range(256):
        new_counter = Counter()
        for timer in range(9):
            new_counter[timer-1] = fish[timer]
        new_counter[8] = new_counter[-1]
        new_counter[6] += new_counter[-1]
        del new_counter[-1]
        fish = new_counter
    print(sum(fish.values()))


if __name__ == '__main__':
    lanternfish()