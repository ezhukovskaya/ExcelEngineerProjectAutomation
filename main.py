import utils.math_utils as mut
import constants.data_constants as data_provider
import models.process_model as model

front_right_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.FRONT_RIGHT)
front_left_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.FRONT_LEFT)
rear_left_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.REAR_LEFT)
rear_right_model = model.ProcessModel(data_provider.STAT_MIKASHEVICHI_FILE_NAME, data_provider.REAR_RIGHT)

R = mut.get_frame_torsion(front_right_model.mean, rear_right_model.mean, front_left_model.mean, rear_left_model.mean)
P = mut.get_longitudinal_roll(front_right_model.mean, rear_right_model.mean, front_left_model.mean,
                              rear_left_model.mean)
B = mut.get_lateral_roll(front_right_model.mean, rear_right_model.mean, front_left_model.mean, rear_left_model.mean)

