
class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        self.numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

    def search_number(self, x):
        return self.numbers.index(x) + 1 if x in self.numbers else -1
