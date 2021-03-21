import utils.math_utils as mut
import utils.list_utils as lut
import constants.data_constants as data_provider
import constants.math_constants as maths
import models.process_model as model
import utils.excel_utils as ex

OUTPUT_PATH = r'resources\Превышение Кд.xlsx'

front_right_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.FRONT_RIGHT,
                                       maths.X_R_FRONT)
front_left_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.FRONT_LEFT,
                                      maths.X_R_FRONT)
rear_left_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.REAR_LEFT, maths.X_R_REAR)
rear_right_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.REAR_RIGHT,
                                      maths.X_R_REAR)

R = mut.get_frame_torsion(front_right_model.mean, rear_right_model.mean, front_left_model.mean, rear_left_model.mean)
P = mut.get_longitudinal_roll(front_right_model.mean, rear_right_model.mean, front_left_model.mean,
                              rear_left_model.mean)
B = mut.get_lateral_roll(front_right_model.mean, rear_right_model.mean, front_left_model.mean, rear_left_model.mean)

k_d_list = [front_left_model.dynamics, front_right_model.dynamics, rear_right_model.dynamics, rear_left_model.dynamics]
greater_k_d_list = mut.get_greater_k_limit(1, k_d_list)
max_list = [front_left_model.max, front_right_model.max, rear_right_model.max, rear_left_model.max]
distance_list = [lut.find_value_tuple_in_the_list(front_left_model.data, max_list[0], 1)[2],
                 lut.find_value_tuple_in_the_list(front_right_model.data, max_list[1], 1)[2],
                 lut.find_value_tuple_in_the_list(rear_right_model.data, max_list[2], 1)[2],
                 lut.find_value_tuple_in_the_list(rear_left_model.data, max_list[3], 1)[2]]

for_table_list = lut.get_table(greater_k_d_list, max_list, distance_list)

row_names = [data_provider.FRONT_LEFT[1], data_provider.FRONT_RIGHT[1],
             data_provider.REAR_RIGHT[1], data_provider.REAR_LEFT[1]]

column_names = ['Превышение', 'MAX', 'Путь от начала']

ex.create_table(OUTPUT_PATH, for_table_list, column_names, row_names)

