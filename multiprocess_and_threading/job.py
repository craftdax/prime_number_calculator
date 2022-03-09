import multiprocessing
import time
import threading


class CalculateJob(multiprocessing.Process):
    def __init__(self, data: dict):
        super().__init__()
        self.job_settings = data
        self.max_threads = self.job_settings['max_threads']
        self.active_threads = 0
        self.result_queue = multiprocessing.Queue()

    def run(self):
        for number in range(self.job_settings['start'], self.job_settings['end'] + 1):
            while self.active_threads >= self.max_threads:
                time.sleep(0.01)
            else:
                threading.Thread(target=self.calculating_thread, args=(number,)).start()
                self.active_threads += 1

    def calculating_thread(self, number):
        prime = True
        for divider in range(2, number):
            if number % divider == 0:
                prime = False
                break
        if prime:
            self.result_queue.put(number)
        self.active_threads -= 1
