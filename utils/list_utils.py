def get_specific_column_by_its_number(my_list, number):
    specific_column = []
    for i in range(0, len(my_list)):
        specific_column.append(my_list[i][number])
    return specific_column


def cut_list(my_list, start):
    for _ in range(0, start):
        my_list.pop(0)
    return my_list


def get_index(my_list, value):
    return my_list.index(value)


def get_table(list_1, list_2, list_3):
    table = []
    for i in range(0, len(list_1)):
        table.append((list_1[i], list_2[i], list_3[i]))
    return table


def find_value_tuple_in_the_list(data, value, column_to_find):
    index = get_specific_column_by_its_number(data, column_to_find).index(value)
    return data[index]
