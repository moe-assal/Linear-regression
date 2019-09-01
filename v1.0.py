
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        return (self.y - f(self.x, a, b)) ** 2


pointr = []
pointr.append(point(1, 2))
pointr.append(point(3, 3))
pointr.append(point(3, 5))
'''
y = ax +b
'''

a = 2
b = 2
point_num = 3
learning_rate = 0.00001


def f(x, a1, b1):
    return a1*x + b1


def cost_of_point(pnum):
    global a,b, pointr
    return (pointr[pnum].y - f(pointr[pnum].x, a, b)) ** 2


def cost():
    total = 0
    for i in range(point_num):
        total = total + cost_of_point(i)
    return total


def derive_cost(a1, b1):
    total = 0
    for i in range(point_num):
        total = total + (pointr[i].y - ((a + a1) * pointr[i].x + (b + b1))) ** 2
    return total


def train(repeat_num):
    global a, b
    for i in range(repeat_num):
        temp_a = a - learning_rate * ((-cost() + derive_cost(0.001, 0)) / 0.001)
        temp_b = b - learning_rate * ((-cost() + derive_cost(0, 0.001)) / 0.001)
        a = temp_a
        b = temp_b
    print(a, b)


if __name__ == '__main__':
    print(cost())
    train(10000)
    print(cost())
