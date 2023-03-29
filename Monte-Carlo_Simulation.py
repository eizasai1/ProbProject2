import math
import random

use_random_number_generator = True

#Variables used for random number generator
x = 1000
a = 24693
c = 3517
k = 2 ** 17

#seconds of each event
dial = 6
busy = 3
unavailable = 25
end = 1

#probabilities
probability_of_busy = 0.2
probability_of_unavailable = 0.3
probability_of_available = 1 - probability_of_busy - probability_of_unavailable

#Expected value of Exponential random variable
expected_exponential = 12


def generate_random_number():
    global use_random_number_generator
    if use_random_number_generator:
        global x, a, c, k
        x = ((a * x + c) % k)
        return x / k
    else:
        return random.random()


def calculate_exponential_rv():
    global expected_exponential
    probability = generate_random_number()
    seconds = -(math.log(1 - probability) * expected_exponential)
    return seconds


def realization_for_w(count=0):
    global dial, busy, unavailable, end
    if count == 4:
        return 0
    probability = generate_random_number()
    if probability <= probability_of_busy:
        return dial + busy + end + realization_of_w(count + 1)
    elif probability <= probability_of_busy + probability_of_unavailable:
        return dial + unavailable + end + realization_of_w(count + 1)
    else:
        seconds_elapsed_for_answer = calculate_exponential_rv()
        if seconds_elapsed_for_answer >= 25:
            return dial + unavailable + end + realization_of_w(count + 1)
        else:
            return dial + seconds_elapsed_for_answer


def get_500_w_values():
    w_values_list = []
    for i in range(500):
        w_values_list.append(realization_of_w())
    return w_values_list


def get_mean(values):
    total = 0
    for i in range(len(values)):
        total += values[i]
    return total / len(values)


def main():
    # print(get_u_values())
    file = open("Probability Project 2.txt", 'w')
    file.close()
    file = open("Probability Project 2.txt", 'a')
    values = get_500_w_values()
    for i in range(len(values)):
        file.write(str(round(values[i], 4)) + "\n")
    file.close()
    values.sort()
    mean = get_mean(values)
    median = ((values[len(values) // 2] + values[len(values) // 2 + 1]) / 2)
    print(str(len(values)) + " w values", "median : " + str(median), "mean : " + str(mean))


def get_u_values():
    values_to_get = [51, 52, 53]
    return_values = []
    for i in range(values_to_get[-1]):
        value = generate_random_number()
        if i+1 in values_to_get:
            return_values.append(round(value, 4))
            print(i)
    return return_values


main()
