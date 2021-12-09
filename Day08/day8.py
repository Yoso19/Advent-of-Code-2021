def seven_segment_search():
    notes = {k:v for (k,v) in 
        [note.split(' | ') for note in open('day8.txt')]}
    counter = 0
    result = 0
    for key, value in notes.items():
        signals = [set(signal) for signal in key.split()]
        signals.sort(key=len)

        a = signals[1]-signals[0]
        g = (signals[6]^signals[7]^signals[8]) - signals[2] - a
        s = signals[2].copy()
        s.update(a, g)
        e = signals[9] - s
        b = (signals[6]^signals[7]^signals[8]) - a - g - signals[0]
        f = (signals[6]^signals[7]^signals[8]) - a - g - b
        c = signals[0] - f
        d = signals[2] - b - c - f

        zero = a|b|c|e|f|g
        one = c|f
        two = a|c|d|e|g
        three = a|c|d|f|g
        four = b|c|d|f
        five = a|b|d|f|g
        six = a|b|d|e|f|g
        seven = a|c|f
        eight = a|b|c|d|e|f|g
        nine = a|b|c|d|f|g
        numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

        v = ''
        for digit in value.split():
            length = len(digit)
            if length == 2 or length == 3 or length == 4 or length == 7:
                counter += 1
            for i, n in enumerate(numbers):
                if set(digit) == n:
                    v += str(i)
                    break
        result += int(v)
    print(counter)
    print(result)


if __name__ == '__main__':
    seven_segment_search()