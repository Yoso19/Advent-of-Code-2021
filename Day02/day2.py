def dive():
    horizontal = 0
    depth = 0
    commands = open('day2.txt').readlines()
    for command in commands:
        value = int(command.split()[1])
        if command.startswith('forward'):
            horizontal += value
        elif command.startswith('up'):
            depth -= value
        else:
            depth += value

    print('part 1:', depth*horizontal)

    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        value = int(command.split()[1])
        if command.startswith('forward'):
            horizontal += value
            depth += aim*value
        elif command.startswith('up'):
            aim -= value
        else:
            aim += value
            
    print('part 2:', depth*horizontal)
        
        

if __name__ == '__main__':
    dive()