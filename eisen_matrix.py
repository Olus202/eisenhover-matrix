# To do:
# Exceptions !!!
# Labels on points in figure
# Descriptions


import pylab as pl
import numpy as np

from datetime import datetime


def clear_file():

    file = open('em_file.txt', 'w')
    file.close()


def create_structure():
    dict_of_tasks = dict()
    list_of_tasks = list()
    list_of_dates = list()
    number = 0

    priorities = []
    date_weights = []

    clear_file()

    return dict_of_tasks, list_of_tasks, list_of_dates, number, priorities, date_weights


def ask_yes():
    ask = input("Do you want add some task? ")

    return ask


def take_tasks_from_user(dict_of_tasks, list_of_tasks, list_of_dates, number):
    while ask_yes() == "yes":
        number += 1
        name = input("Enter the task name: ")
        date = input("Enter the task deadline (dd-mm-yyyy): ")

        deadline = datetime.strptime(date, "%d-%m-%Y")

        dict_of_tasks[str(number)] = {"name": name,
                                      "deadline": deadline,
                                      "date_weight": "-",
                                      "priority": "-"}

        list_of_tasks.append(str(number))
        list_of_dates.append([deadline, str(number)])

    return dict_of_tasks, list_of_tasks, list_of_dates, number


def take_priorities_from_user(dict_of_tasks, list_of_tasks):
    print("-" * 30)
    print("\nThink about priority of each task above, then enter it to programme.\n")

    save_to_file(dict_of_tasks, list_of_tasks)
    print_file()

    priorities = [x for x in list_of_tasks]

    for t in list_of_tasks:
        print("You can use one of these priorities: ", priorities)
        try:
            priority = input("Enter the priority of the task number " + t + ": ")
            properties = dict_of_tasks[t]
            properties["priority"] = priority
            priorities.remove(str(priority))
        except:
            print("Sorry, some mistake... Enter your priorities again.")
            take_priorities_from_user(dict_of_tasks, list_of_tasks)

    return dict_of_tasks


def save_to_file(dict_of_tasks, list_of_tasks):
    clear_file()
    for t in list_of_tasks:
        properties = dict_of_tasks[t]
        n = properties["name"]
        d = properties["deadline"]
        dw = properties["date_weight"]
        p = properties["priority"]

        task_to_file = "{}. {}  || deadline: {} || date weight: {} || priority: {}\n".format(t, n, d, dw, p)

        file = open('em_file.txt', 'a')
        file.write(task_to_file)
        file.close()


def print_file():
    file = open('em_file.txt')
    tasks = file.read()
    print("-" * 30)
    print("Your task:\n")
    print(tasks)
    file.close()


def date_weight(list_of_dates, dict_of_tasks):
    sort_dates = sorted(list_of_dates)
    weights = enumerate(sort_dates)

    for n in weights:
        task_number = n[1][1]
        weight = n[0]
        d = dict_of_tasks[task_number]

        d["date_weight"] = weight + 1

    return dict_of_tasks


def take_priorities_and_weights(dict_of_tasks, list_of_tasks, priorities, date_weights):
    for t in list_of_tasks:
        d = dict_of_tasks[t]
        p = d['priority']
        w = d['date_weight']

        priorities.append(p)
        date_weights.append(w)

    return priorities, date_weights


def create_figure(priorities, date_weights, list_of_tasks):
    tasks = len(list_of_tasks)

    pw = np.array(priorities)
    dw = np.array(date_weights)

    div1 = np.array([tasks/2] * (tasks+1))
    div2 = np.array((range(tasks+1)))

    pl.xlabel('NOT URGENT ---- Date weight ---- URGENT')
    pl.ylabel('NOT IMPORTANT ---- Priority weight ---- IMPORTANT')
    pl.title('Matrix of Eisenhover')

    pl.axis([0, tasks, 0, tasks])

    try:
        pl.plot(dw, pw, 'ro', div1, div2, 'b', div2, div1, 'b')
        pl.savefig('em_figure.png')
        print("-" * 30)
        print("Files with your Matrix of Eisenhover ware saved.")
    except:
        print("-" * 30)
        print("Some mistake... Please try again.")


def run():
    dict_of_tasks, list_of_tasks, list_of_dates, number, priorities, date_weights = create_structure()
    take_tasks_from_user(dict_of_tasks, list_of_tasks, list_of_dates, number)
    take_priorities_from_user(dict_of_tasks, list_of_tasks)
    date_weight(list_of_dates, dict_of_tasks)
    save_to_file(dict_of_tasks, list_of_tasks)
    print_file()
    take_priorities_and_weights(dict_of_tasks, list_of_tasks, priorities, date_weights)
    create_figure(priorities, date_weights, list_of_tasks)

    input("Press ENTER to exit")

run()
