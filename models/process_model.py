import utils.list_utils as lut
import utils.math_utils as mut
import constants.math_constants as current_const
import utils.excel_utils as exeut


def get_data(file_path, first_column_name, second_column_name, third_column_name,
             start_index=0, end_index=0):
    return exeut.read_excel_column_values_by_three_names(file_path, first_column_name, second_column_name,
                                                         third_column_name, start_index, end_index)


class ProcessModel:
    values = []
    speed = 0.0
    route = 0.0
    mean = 0.0
    dispersion = 0.0
    deviation = 0.0
    min = 0.0
    max = 0.0
    pressure = 0.0
    time = 0.0
    distance = 0.0
    dynamics = 0.0
    accumulated_dynamic_factor = 0.0
    x_r = 0.0
    data = []

    def __init__(self, file_path, my_tuple, x_r):
        self.x_r = x_r
        self.data = get_data(file_path, my_tuple[0], my_tuple[1],
                             my_tuple[2], my_tuple[3], my_tuple[4])
        self.values = self.__get_values()
        self.speed = self.__get_speed()
        self.route = self.__get_route()
        self.mean = self.__get_mean()
        self.dispersion = self.__get_dispersion()
        self.deviation = self.__get_deviation()
        self.min = self.__get_min()
        self.max = self.__get_max()
        self.pressure = self.__get_pressure()
        self.time = self.__get_time()
        self.distance = self.__get_distance()
        self.dynamics = self.__get_dynamics()
        self.accumulated_dynamic_factor = self.__get_accumulated_dynamic_factor()

    def __get_values(self):
        return lut.cut_list(lut.get_specific_column_by_its_number(self.data, 1), 12)

    def __get_accumulated_dynamic_factor(self):
        return mut.get_accumulated_dynamic_factor(self.__get_max(), self.__get_distance(),
                                                  lut.get_index(self.__get_values(), self.__get_max()) + 1)

    def __get_mean(self):
        return mut.get_mean_value(self.__get_values())

    def __get_dispersion(self):
        return mut.get_grades_variance(self.__get_values(), self.__get_mean())

    def __get_deviation(self):
        return mut.get_deviation(self.__get_values())

    def __get_max(self):
        return max(self.__get_values())

    def __get_min(self):
        return min(self.__get_values())

    def __get_speed(self):
        return self.data[6][2]

    def __get_route(self):
        return self.data[5][2]

    def __get_dynamics(self):
        return mut.get_dynamic_factor(self.__get_max(), self.x_r)

    def __get_pressure(self):
        return lut.find_value_tuple_in_the_list(self.data, self.__get_max(), 1)[1]

    def __get_time(self):
        return lut.find_value_tuple_in_the_list(self.data, self.__get_max(), 1)[0]

    def __get_distance(self):
        return lut.find_value_tuple_in_the_list(self.data, self.__get_max(), 1)[2]
