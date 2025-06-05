import random


class MonteCarlo:
    def __init__(self, fun, argcount):
        self.fun = fun
        self.argcount = argcount
        self.possibility = 0

    def sample(self):
        num = [random.random() for _ in range(self.argcount)]
        return self.fun(num)

    def montecarlo(self, rounds):
        self.possibility = sum(self.sample() for _ in range(rounds)) / rounds
        return self.possibility


def circlearea(num):
    return num[0] ** 2 + num[1] ** 2 <= 1


montecarlo = MonteCarlo(circlearea, 2)
area = montecarlo.montecarlo(100000)
pi = 4 * area
print(pi)
