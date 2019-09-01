""" Created by Moe Ramzi Assal from scratch.
    Machine Learning project.
    python 3.3+
    v3.0
"""

import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        return (self.y - f(self.x)) ** 2


temp_var = []
number_of_var = 0
point_num = 0
learning_rate = 0.00001
degree = 0
var = []
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
    for q in range(0, point_num):
        global pointr
        x = int(input("type x value of point (" + str(q) + "): "))
        y = int(input("type y value of point (" + str(q) + "): "))
        pointr.append(Point(x, y))
    return True


def fill_var_from_terminal():
    global degree, number_of_var
    degree = int(input("degree: "))
    number_of_var = degree + 1
    for w in range(0, number_of_var):
        ran = random.randint(-5, 5)
        var.append(ran)
    return True


def print_final_function():
    for e in range(0, number_of_var):
        print(str(var[e]) + " x^" + str(e))


def f(x):  # this is the main function
    t = 0
    for o in range(0, number_of_var):
        t = t + var[o] * (x ** i)
    return t


def derive_f_wrt_var(x, var_num):   # partial derivative of main function wrt to variable
    t = f(x) - (var[var_num] * (x ** var_num))
    t = t + ((var[var_num] + 0.001) * (x ** var_num))
    return t


def cost():  # cost of the error btn the point and the function
    total = 0
    for y in range(point_num):
        total = total + pointr[y].cost()
    return total


def derive_cost(var_num):  # partial derivative function, derivates wrt to variable
    total = 0
    for t in range(point_num):
        total = total + (pointr[t].y - derive_f_wrt_var(pointr[t].x, var_num)) ** 2
    return total


def train(repeat_num):  # train to minimize the cost by changing variables
    global temp_var
    for p in range(0, repeat_num):
        temp_var.clear()
        for d in range(0, number_of_var):
            temp = var[d] - learning_rate * ((derive_cost(d) - cost()) / 0.001)
            temp_var.append(temp)
        for d in range(0, number_of_var):
            var[d] = temp_var[d]
    return True


def get_points_from_file(fname, points_num_):  # get points from file in form "x,y\n" ex: "5,8\n9,6"
    global point_num
    point_num = points_num_
    with open(fname) as file:
        for r in range(0, point_num):
            global pointr
            content = file.readline()
            x, y = content.split(',')
            pointr.append(Point(int(x), int(y)))


if __name__ == '__main__':
    while True:
        print_direction()
        sw_num = int(input("type your number: "))
        if sw_num == 1:
            get_points_from_user()
            fill_var_from_terminal()
        elif sw_num == 2:
            path = input("enter the file's full path: ")
            points_num = int(input("enter the points' number: "))
            get_points_from_file(path, points_num)
        elif sw_num == 3:
            repeat_training = int(input("print the number times you want to train your model: "))
            print("training model")
            train(repeat_training)
            print("finished training")
            print_final_function()
        elif sw_num == 4:
            pointr.clear()
            var.clear()
            number_of_var = 0
            degree = 0
            learning_rate = 0.00001
        elif sw_num == 5:
            print(cost())
        elif sw_num == 6:
            input_data = input("type [y]es or [n]o to modify variables of polynomial: ")
            if input_data == "y":
                for i in range(0, number_of_var):
                    if input("type [y]es or [n]o to modify variable of x^" + str(i) + " : ") == "y":
                        var[i] = float(input("type the number: "))
            input_data = input("type [y]es or [n]o to modify learning rate: ")
            if input_data == "y":
                learning_rate = float(input("type your number: "))
        elif sw_num == 7:
            print("thank you for using the app, by Moe Asaal")
            break
        else:
            print("unexpected error occurred, please stick to instructions")
