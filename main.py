from utils.excel_utils import read_excel_column_values_by_three_names

FRONT_RIGHT = ("Процесс", "Передний правый", "Значение", 0, 4)
FRONT_LEFT = ("Процесс", "Передний левый", "Значение", 0, 4)
REAR_RIGHT = ("Процесс", "Задний правый", "Значение", 0, 4)
REAR_LEFT = ("Процесс", "Задний левый", "Значение", 0, 4)

RACK = ("Процесс", "RACK", "Значение", 0)
PITCH = ("Процесс", "PITCH", "Значение", 0)
BIAS = ("Процесс", "BIAS", "Значение", 0)

STAT_MIKASHEVICHI_FILE_NAME = "resources/Stat_Mikashevichi.xlsx"

front_right_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, FRONT_RIGHT[0], FRONT_RIGHT[1],
                                                           FRONT_RIGHT[2], FRONT_RIGHT[3], FRONT_RIGHT[4])
front_left_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, FRONT_LEFT[0], FRONT_LEFT[1],
                                                          FRONT_LEFT[2], FRONT_LEFT[3], FRONT_LEFT[4])
rear_right_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, REAR_RIGHT[0], REAR_RIGHT[1],
                                                          REAR_RIGHT[2], REAR_RIGHT[3], REAR_RIGHT[4])
rear_left_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, REAR_LEFT[0], REAR_LEFT[1],
                                                         REAR_LEFT[2], REAR_LEFT[3], REAR_LEFT[4])

front_right_list_speed = front_right_list[6][2]
front_left_list_speed = front_left_list[6][2]
rear_right_list_speed = rear_right_list[6][2]
rear_left_list_speed = rear_left_list[6][2]

front_right_list_route = front_right_list[5][2]
front_left_list_route = front_left_list[5][2]
rear_right_list_route = rear_right_list[5][2]
rear_left_list_route = rear_left_list[5][2]

rack_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, RACK[0], RACK[1],
                                                    RACK[2], RACK[3])
pitch_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, PITCH[0], PITCH[1],
                                                     PITCH[2], PITCH[3])
bias_list = read_excel_column_values_by_three_names(STAT_MIKASHEVICHI_FILE_NAME, BIAS[0], BIAS[1],
                                                    BIAS[2], BIAS[3])
rack_mean = rack_list[3][2]
pitch_mean = pitch_list[3][2]
bias_mean = bias_list[3][2]

rack_dispersion = rack_list[4][2]
pitch_dispersion = pitch_list[4][2]
bias_dispersion = bias_list[4][2]
