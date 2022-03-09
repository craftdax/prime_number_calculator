import json
import threading
import time

"""


"""


class PrimeNumberCalculator:
    def __init__(self):
        self.prime_numbers = []
        with open('settings.json', 'r') as f:
            self.settings = json.load(f)
#        self.calculating_thread = threading.Thread(target=self.calculating_thread, args=(int,))
        self.max_threads = self.settings['max_threads']
        self.active_threads = 0

    def calculate(self):
        for number in range(self.settings['lowest_number'], self.settings['highest_number']+1):
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
            self.prime_numbers.append(number)
        self.active_threads -= 1

    def print_result(self):
        print(sorted(self.prime_numbers))


start = time.time()
P = PrimeNumberCalculator()
P.calculate()
P.print_result()
print(f'Execution time = {time.time() - start} seconds')
