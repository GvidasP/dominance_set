from tqdm import tqdm
import statistics

from bishops import Bishops
from queens import Queens


def find_queens(n_from, n_to):
    avg = []
    for j in tqdm(range(n_from, n_to + 1), desc='Valdoves'):
        queens_class = Queens(j)
        results = []
        for i in range(100):
            result = queens_class.solve()
            results.append(result)

        avg.append(statistics.mean(results))

    return avg


def find_bishops(n_from, n_to):
    avg = []
    for j in tqdm(range(n_from, n_to + 1), desc='Rikiai'):
        bishops_class = Bishops(j)
        results = []
        for i in range(100):
            result = bishops_class.solve()
            results.append(result)

        avg.append(statistics.mean(results))

    return avg


def do_testing(n_from, n_to):
    queens_res = find_queens(n_from, n_to)
    bishops_res = find_bishops(n_from, n_to)

    print(queens_res)
    print(bishops_res)
