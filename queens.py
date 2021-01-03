import numpy as np
import time


class Queens:
    def __init__(self, size, output=False):
        self.size = size
        self.solutions = 0
        self.solutions_list = []
        self.output = output

    def solve(self):
        start = time.perf_counter()

        positions = [-1] * self.size
        self.place(positions, 0)

        end = time.perf_counter()

        if self.output:
            file = open('solution_queens.txt', 'w')
            file.write('Rastu variantu: {}\nUztruko laiko: {}\n\n'.format(
                self.solutions, end - start))

            file.write(''.join(self.solutions_list))

            file.close()

        return end - start

    def place(self, positions, row):
        if(row == self.size):
            self.solutions += 1
            if (self.output):
                self.solutions_list.append(self.show_full_board(positions))
        else:
            for column in range(self.size):
                if self.check_place(positions, row, column):
                    positions[row] = column
                    self.place(positions, row + 1)

    def check_place(self, positions, row, column):
        if (row == 0 or row == self.size - 1):
            if (column == 0 or column == self.size - 1):
                return False
        for i in range(row):
            if positions[i] == column or positions[i] - i == column - row or positions[i] + i == column + row:
                return False
        return True

    def show_full_board(self, positions):
        solution = ""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            solution += line + '\n'
        solution += '\n'

        return solution
