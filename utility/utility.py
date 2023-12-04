

class Utility:

    def __init__(self):
        pass

    def is_prime(self, number):
        if number <= 1:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            # Check for factors up to the square root of the number
            for i in range(3, int(number ** 0.5) + 1, 2):
                if number % i == 0:
                    return False
            return True
