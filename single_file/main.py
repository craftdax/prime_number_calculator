import json
import time

"""


"""


class PrimeNumberCalculator:
    def __init__(self):
        self.prime_numbers = []
        with open('settings.json', 'r') as f:
            self.settings = json.load(f)

    def calculate(self):
        for number in range(self.settings['lowest_number'], self.settings['highest_number']+1):
            prime = True
            for divider in range(2, number):
                if number % divider == 0:
                    prime = False
                    break
            if prime:
                self.prime_numbers.append(number)

    def print_result(self):
        print(self.prime_numbers)


start = time.time()
P = PrimeNumberCalculator()
P.calculate()
P.print_result()
print(f'Execution time = {time.time() - start} seconds')