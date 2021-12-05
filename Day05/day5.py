import numpy as np


def hydrothermal_venture():
    vents = [vent.strip().split(' -> ') for vent in open('day5.txt')]
    sea = np.zeros((1000,1000), dtype=int)
    for vent in vents:
        x0, y0 = map(int, vent[0].split(','))
        x1, y1 = map(int, vent[1].split(','))
        if x0 == x1:
            y_start = y0 if y0 < y1 else y1
            y_end = y0 if y0 > y1 else y1
            for y in range(y_start, y_end+1):
                sea[y, x0] += 1
        elif y0 == y1:
            x_start = x0 if x0 < x1 else x1
            x_end = x0 if x0 > x1 else x1
            for x in range(x_start, x_end+1):
                sea[y0, x] += 1

        # added for part 2 ----------------------------
        else:
            sea[y0, x0] += 1
            if x0 < x1 and y0 < y1:
                while x0 != x1:
                    x0 += 1
                    y0 += 1
                    sea[y0, x0] += 1
            elif x0 > x1 and y0 < y1:
                while x0 != x1:
                    x0 -= 1
                    y0 += 1
                    sea[y0, x0] += 1
            elif x0 < x1 and y0 > y1:
                while x0 != x1:
                    x0 += 1
                    y0 -= 1
                    sea[y0, x0] += 1
            else:
                while x0 != x1:
                    x0 -= 1
                    y0 -= 1
                    sea[y0, x0] += 1   

    print(np.count_nonzero(sea > 1))


if __name__ == '__main__':
    hydrothermal_venture()