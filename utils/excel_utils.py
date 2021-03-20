import pandas as pd


def read_excel_column_values_by_three_names(file_path, first_column_name, second_column_name, third_column_name,
                                            start_index=0, end_index=0):
    data = pd.read_excel(file_path, skipfooter=end_index)
    data_list = data[[first_column_name, second_column_name, third_column_name]].values.tolist()
    del data_list[0:start_index]
    return data_list
