import random


class MonteCarlo:
    def __init__(self, fun, argcount):
        self.fun = fun
        self.argcount = argcount
        self.possibility = 0

    def sample(self, fun, argcount):
        num = []
        for i in range(argcount):
            num.append(random.random())
        return fun(num)

    def montecarlo(self, round):
        trues = 0
        for i in range(round):
            if self.sample(self.fun, self.argcount):
                trues += 1
        self.possibility = trues / round
        return self.possibility


def circlearea(num):
    return num[0] ** 2 + num[1] ** 2 <= 1


montecarlo = MonteCarlo(circlearea, 2)
area = montecarlo.montecarlo(100000)
print(area)

pi = 4 * area
print(pi)
