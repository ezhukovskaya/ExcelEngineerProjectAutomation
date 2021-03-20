import numpy as np


def get_mean_value(_list):
    return float(sum(_list)) / max(len(_list), 1)


def get_grades_variance(my_list, average):
    variance = 0
    for i in my_list:
        variance += (average - i) ** 2
    return variance / len(my_list)


def get_accumulated_dynamic_factor(value, distance, i_max):
    _sum = 0
    for i in range(0, i_max):
        _sum += value
    return _sum / distance


def get_dynamic_factor(_max, x_r):
    return _max / x_r


def get_frame_torsion(front_right_force, rear_right_force, front_left_force, rear_left_force):
    return (front_right_force + rear_right_force) - (front_left_force + rear_left_force)


def get_longitudinal_roll(front_right_force, rear_right_force, front_left_force, rear_left_force):
    return (rear_right_force + rear_left_force) - (front_left_force + front_right_force)


def get_lateral_roll(front_right_force, rear_right_force, front_left_force, rear_left_force):
    return (front_left_force + rear_left_force) - (rear_right_force + front_right_force)


def get_deviation(my_list):
    return np.std(my_list)
