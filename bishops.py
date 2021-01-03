import numpy as np
import time


class Bishops:
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
            file = open('solution_bishops.txt', 'w')
            file.write('Rastu variantu: {}\nUztruko laiko: {}\n\n'.format(
                self.solutions//2, end - start))

            file.write(
                ''.join(self.solutions_list[:len(self.solutions_list)//2]))

            file.close()

        return end - start

    def place(self, positions, row):
        if(row == self.size):
            board = self.convert_bishops_positions_to_array(positions)
            if(-1 not in board):
                self.solutions += 1
                if (self.output):
                    solution = self.show_full_board(positions)
                    self.solutions_list.append(solution)
        else:
            for column in range(self.size):
                if self.check_place(positions, row, column):
                    positions[row] = column
                    self.place(positions, row + 1)

    def check_place(self, positions, row, column):
        for i in range(row):
            if positions[i] - i == column - row or positions[i] + i == column + row:
                return False

        return True

    def convert_bishops_positions_to_array(self, positions):
        board = np.full((self.size, self.size), -1, int)

        for row in range(self.size):
            for column in range(self.size):
                if positions[row] == column:
                    board[row][column] = 1

        bishops = np.where(board == 1)
        bishops_positions = list(zip(bishops[0], bishops[1]))

        for row, column in bishops_positions:
            for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
                board[i][j] = 1
            for i, j in zip(range(row, self.size, 1), range(column, -1, -1)):
                board[i][j] = 1
            for i, j in zip(range(row, self.size, 1), range(column, self.size, 1)):
                board[i][j] = 1
            for i, j in zip(range(row, -1, -1), range(column, self.size, 1)):
                board[i][j] = 1

        return board

    def show_full_board(self, positions):
        solution = ""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "B "
                else:
                    line += ". "
            solution += line + '\n'
        solution += '\n'

        return solution
