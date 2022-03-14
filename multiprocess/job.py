import multiprocessing


class CalculateJob(multiprocessing.Process):
    def __init__(self, data: dict):
        super().__init__()
        self.job_settings = data
        self.result_queue = multiprocessing.Queue()

    def run(self):
        for number in range(self.job_settings['start'], self.job_settings['end'] + 1):
            prime = True
            for divider in range(2, number):
                if number % divider == 0:
                    prime = False
                    break
            if prime:
                self.result_queue.put(number)
