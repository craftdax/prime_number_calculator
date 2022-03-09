import json
import time
from job import CalculateJob
"""


"""


class PrimeNumberCalculator:
    def __init__(self):
        self.prime_numbers = []
        self.processes = {}
        self.active_processes = []
        with open('settings.json', 'r') as f:
            self.settings = json.load(f)
        for first, last, process in self.iteration_function(self.settings['lowest_number'], self.settings['highest_number'], self.settings['number_of_processes']):
            self.processes[f'Process{process}'] = {'start': first, 'end': last, 'max_threads': self.settings['number_of_threads']}

    @staticmethod
    def iteration_function(begin: int, end: int, processes: int):
        division = (end - begin) // processes
        for i in range(processes):
            process_start = i * division + 2
            if i + 1 == processes:
                yield process_start, process_start + division + (end - (process_start + division)), i + 1
            else:
                yield process_start, process_start + division - 1, i + 1

    def calculate(self):
        for process_info in self.processes.keys():
            process = CalculateJob(self.processes[process_info])
            process.start()
            self.active_processes.append(process)
        while len(self.active_processes) > 0:
            for process in self.active_processes:
                if not process.result_queue.empty():
                    self.prime_numbers.append(process.result_queue.get())
                if not process.is_alive():
                    self.active_processes.remove(process)

    def print_result(self):
        print(sorted(self.prime_numbers))


if __name__ == '__main__':
    start = time.time()
    P = PrimeNumberCalculator()
    P.calculate()
    P.print_result()
    print(f'Execution time = {time.time() - start} seconds')
