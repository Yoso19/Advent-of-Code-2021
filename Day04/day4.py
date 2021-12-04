import numpy as np


class Board():

    def __init__(self, rows):
        self.board = np.array(rows).astype(np.int)

    def get_numbers(self):
        return set(self.board.flatten())

    def get_rows_and_columns(self):
        result = []
        for i in range(5):
            result.append(set(self.board[i]))
            result.append(set(self.board[:,i]))
        return result

    def check_if_winning(self, numbers):
        drawn = set(numbers)
        for line in self.get_rows_and_columns():
            if line.issubset(drawn):
                return True
        return False


def giant_squid():
    with open('day4.txt') as input:
        drawn = [int(x) for x in next(input).strip().split(',')]
        row = 0
        rows = []
        boards = []
        for line in input.readlines():
            if line == '\n':
                continue
            if row == 4:
                row = 0
                rows.append(line.split())
                boards.append(Board(rows))
                rows = []
            else:
                rows.append(line.split())
                row += 1

    winners = []
    n = []
    for number in range(5, 102):
        numbers = drawn[0:number]
        for board in boards:
            if board.check_if_winning(numbers):
                if board not in winners:
                    winners.append(board)
                    n.append(numbers)
    print(winners[0].board)
    print(sum(winners[0].get_numbers()-set(n[0])) * n[0][-1])
    print(winners[-1].board)
    print(sum(winners[-1].get_numbers()-set(n[-1])) * n[-1][-1])


if __name__ == '__main__':
    giant_squid()