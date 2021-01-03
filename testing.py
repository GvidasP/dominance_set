import concurrent.futures
import threading
import statistics
from tqdm import tqdm
from queue import Queue

from queens import Queens
from bishops import Bishops


def start_queens_process(size):
    queens_class = Queens(size)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(
            queens_class.solve) for i in range(100)]

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results, size


def start_bishops_process(size):
    bishops_class = Bishops(size)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(
            bishops_class.solve) for i in range(100)]

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results, size


def t_queens(n_to, n_from):
    with tqdm(total=((n_to - n_from + 1)), desc='Valdoves') as pbar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            mean_queens = {}
            queens_futures = [executor.submit(
                start_queens_process, i) for i in range(n_from, n_to + 1)]

            for future in concurrent.futures.as_completed(queens_futures):
                result_queens, size = future.result()
                queens_avg = statistics.mean(result_queens)
                mean_queens[size] = queens_avg
                pbar.update(1)

    return 'Valdoviu sprendimo laiko vidurkis didejimo tvarka (n: laikas): {}'.format(
        dict(sorted(mean_queens.items(), key=lambda item: item[1])))


def t_bishops(n_to, n_from):
    with tqdm(total=((n_to - n_from + 1)), desc='Rikiai') as pbar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            mean_bishops = {}
            bishops_futures = [executor.submit(
                start_bishops_process, i) for i in range(n_from, n_to + 1)]

            for future in concurrent.futures.as_completed(bishops_futures):
                result_bishops, size = future.result()
                bishops_avg = statistics.mean(result_bishops)
                mean_bishops[size] = bishops_avg
                pbar.update(1)

    return 'Rikiu sprendimo laiko vidurkis didejimo tvarka (n: laikas): {}'.format(
        dict(sorted(mean_bishops.items(), key=lambda item: item[1])))


def do_testing(n_from, n_to):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        queens = executor.submit(t_queens, n_to, n_from)
        bishops = executor.submit(t_bishops, n_to, n_from)

        print(queens.result())
        print(bishops.result())
