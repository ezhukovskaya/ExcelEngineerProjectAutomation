import utils.math_utils as mut
import constants.data_constants as data_provider
import constants.math_constants as maths
import models.process_model as model

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
