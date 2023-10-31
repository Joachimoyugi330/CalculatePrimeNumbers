import os

class PrimeNumberGenerator:
    def __init__(self):
        self.directory = os.getcwd()
        self.filename = "results.txt"
        self.filePath = os.path.join(self.directory, self.filename)

    def check_prime(self, num):
        count = 0
        if num <= 1:
            return False
        else:
            for i in range(1, num + 1):
                if (num % i) == 0:
                    count += 1
            if count == 2:
                return True
            else:
                return False

    def generate_primes(self):
        if os.path.exists(self.filePath):
            print(f"{self.filename} already exists")
        else:
            with open(self.filename, "w") as file:
                for num in range(1, 250):
                    if self.check_prime(num):
                        file.write(str(num) + "\n")

if __name__ == "__main__":
    prime_number_generator = PrimeNumberGenerator()
    prime_number_generator.generate_primes()
