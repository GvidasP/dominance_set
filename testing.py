import concurrent.futures
from tqdm import tqdm
import statistics

from bishops import Bishops
from queens import Queens


# def find_bishops(size):
#     results = []

#     bishops = Bishops(size)
#     for i in range(100):
#         result = bishops.solve()
#         results.append(result)

#     return results


# def find_queens(size):
#     results = []

#     queens = Queens(size)
#     for i in range(100):
#         result = queens.solve()
#         results.append(result)

#     return results


def find_queens(n_from, n_to):
    avg = []
    for j in tqdm(range(n_from, n_to + 1), desc='Valdoves'):
        queens = Queens(j)
        results = []
        for i in range(100):
            result = queens.solve()
            results.append(result)

        avg.append(statistics.mean(results))

    return avg


def find_bishops(n_from, n_to):
    avg = []
    for j in tqdm(range(n_from, n_to + 1), desc='Rikiai'):
        bishops = Bishops(j)
        results = []
        for i in range(100):
            result = bishops.solve()
            results.append(result)

        avg.append(statistics.mean(results))

    return avg


def do_testing(n_from, n_to):
    queens_res = find_queens(n_from, n_to)
    bishops_res = find_bishops(n_from, n_to)

    print(queens_res)
    print(bishops_res)
