from collections import Counter
from copy import deepcopy

def binary_diagnostic():
    input = open('day3.txt').readlines()
    counters = [Counter() for _ in range(len(input[0])-1)]
    for number in input:
        for i, digit in enumerate(list(number.strip())):
            counters[i].update(digit)
    gamma = ''
    for counter in counters:
        gamma += counter.most_common(1)[0][0]
    mask = 0b111111111111
    print('part 1:', int(gamma, 2) * (int(gamma, 2)^mask))


    #part 2
    oxygen = input.copy()
    oxygen_count = deepcopy(counters)
    co2 = input.copy()
    co2_count = deepcopy(counters)

    for bit in range(len(input[0])-1):
        print(oxygen_count, '\n')
        o = []
        for value in oxygen:
            if value[bit] == oxygen_count[bit].most_common(1)[0][0]:
                o.append(value)
        if len(o) == 1:
            print(o)
            oxygen = o.copy()
            break
        oxygen_count = recount(o)
        oxygen = o.copy()


    for bit in range(len(input[0])-1):
        print(co2_count, '\n')
        c = []

        if len(co2_count[bit].most_common()) == 2 and co2_count[bit].most_common()[0][1] == co2_count[bit].most_common()[1][1]:
            for value in co2:
                if value[bit] == '0':
                    c.append(value)
            if len(c) == 1:
                print(c)
                co2 = c.copy()
                break
            co2_count = recount(c)
            co2 = c.copy()
            continue
        
        for value in co2:
            if value[bit] != co2_count[bit].most_common(1)[0][0]:
                c.append(value)
        
        if len(c) == 1:
            print(c)
            co2 = c.copy()
            break
        co2_count = recount(c)
        co2 = c.copy()
    print(int(oxygen[0].strip(), 2)*int(co2[0].strip(), 2))

def recount(input):
    counters = [Counter() for _ in range(len(input[0])-1)]
    for number in input:
        for i, digit in enumerate(list(number.strip())):
            counters[i].update(digit)        
    return counters


if __name__ == '__main__':
    binary_diagnostic()