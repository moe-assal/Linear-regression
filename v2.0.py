''' Created by Moe Ramzi Assal, linear regression, to minimize the cost function for y = ax + b
    by changing a and b.
    Enter points and train model.
    python 3.3+
    v2.0
'''

import random


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        return (self.y - f(self.x, a, b)) ** 2


a = random.randint(1, 10)
b = random.randint(1, 10)
point_num = 0
learning_rate = 0.00001

pointr = []


def print_direction():
    print("""
    -type 1 for adding points data from terminal
    -type 2 to read point data from file
    -type 3 to train and get linear equation
    -type 4 to reset data
    -type 5 to print cost
    -type 6 to modify builtins
    -type 7 to exit
    
    for any issues contact Moe Assal""")


def get_points_from_user():
    global pointr, point_num
    point_num = int(input("type the number of point: "))
    for i in range(0, point_num):
        global pointr
        x = int(input("type x value of point (" + str(i) + "): "))
        y = int(input("type y value of point (" + str(i) + "): "))
        pointr.append(point(x, y))
    return True


def f(x, a1, b1):   # this is the main function
    return a1*x + b1


def cost():     # cost of the error btn the point and the line
    total = 0
    for i in range(point_num):
        total = total + pointr[i].cost()
    return total


def derive_cost(a1, b1):    # partial derivative function, add a1 to a, like dx + x respectively
    total = 0
    for i in range(point_num):
        total = total + (pointr[i].y - ((a + a1) * pointr[i].x + (b + b1))) ** 2
    return total


def train(repeat_num):  # train to minimize the cost by changing a and b
    global a, b
    for i in range(repeat_num):
        temp_a = a - learning_rate * ((derive_cost(0.001, 0) - cost()) / 0.001)
        temp_b = b - learning_rate * ((derive_cost(0, 0.001) - cost()) / 0.001)
        a = temp_a
        b = temp_b
    return True


def get_points_from_file(fname, points_num):    # get points from file in form "x,y\n" ex: "5,8\n9,6"
    global point_num
    point_num = points_num
    with open(fname) as file:
        for i in range(0, point_num):
            global pointr
            content = file.readline()
            x, y = content.split(',')
            pointr.append(point(int(x), int(y)))


if __name__ == '__main__':
    while True:
        print_direction()
        sw_num = int(input("type your number: "))
        if sw_num == 1:
            get_points_from_user()
        elif sw_num == 2:
            path = input("enter the file's full path: ")
            points_num = int(input("enter the points' number: "))
            get_points_from_file(path, points_num)
        elif sw_num == 3:
            repeat_training = int(input("print the number times you want to train your model: "))
            print("training model")
            train(repeat_training)
            print("finished training")
            print("y = " + str(round(a, 3)) + "x + " + str(round(b, 3)))
        elif sw_num == 4:
            pointr.clear()

        elif sw_num == 5:
            print(cost())
        elif sw_num == 6:
            input_data = input("type [y]es or [n]o to modify a: ")
            if input_data == "y":
                a = int(input("type your number: "))
            input_data = input("type [y]es or [n]o to modify b: ")
            if input_data == "y":
                b = int(input("type your number: "))
            input_data = input("type [y]es or [n]o to modify learning rate: ")
            if input_data == "y":
                learning_rate = int(input("type your number: "))
        elif sw_num == 7:
            print("thank you for using the app, by Moe Asaal")
            break
        else:
            print("unexpected error occurred, please stick to instructions")
