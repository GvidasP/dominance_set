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
        futures = {executor.submit(
            queens_class.solve): i for i in range(100)}

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results, size


def start_bishops_process(size):
    bishops_class = Bishops(size)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(
            bishops_class.solve): i for i in range(100)}

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results, size


def do_testing(n_from, n_to):
    with tqdm(total=((n_to - n_from + 1) * 2)) as pbar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            mean_bishops = {}
            mean_queens = {}

            queens_futures = {executor.submit(
                start_queens_process, i): i for i in range(n_from, n_to + 1)}
            bishops_futures = {executor.submit(
                start_bishops_process, i): i for i in range(n_from, n_to + 1)}

            for future in concurrent.futures.as_completed(queens_futures):
                result_queens, size = future.result()
                queens_avg = statistics.mean(result_queens)
                mean_queens[size] = queens_avg

                pbar.update(1)

            for future in concurrent.futures.as_completed(queens_futures):
                result_bishops, size = future.result()
                bishops_avg = statistics.mean(result_bishops)
                mean_bishops[size] = bishops_avg

                pbar.update(1)

    print('\n')

    print('Valdoviu sprendimo laiko vidurkis didejimo tvarka (n: laikas): {}'.format(
        dict(sorted(mean_queens.items(), key=lambda item: item[1]))))
    print('Rikiu sprendimo laiko vidurkis didejimo tvarka (n: laikas): {}'.format(
        dict(sorted(mean_bishops.items(), key=lambda item: item[1]))))

    input()
