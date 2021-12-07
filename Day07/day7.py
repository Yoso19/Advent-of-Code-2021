def the_treachery_of_whales():
    with open('day7.txt') as horizontals:
        h = [int(x) for x in horizontals.readline().split(',')]
    fuel1 = []
    fuel2 = []
    for hor in range(min(h), max(h)+1):
        fuel1.append(sum([abs(x-hor) for x in h]))
        fuel2.append(sum([(abs(x-hor)*(abs(x-hor)+1))/2 for x in h]))
    print('part1:', min(fuel1))
    print('part2:', int(min(fuel2)))

if __name__ == '__main__':
    the_treachery_of_whales()