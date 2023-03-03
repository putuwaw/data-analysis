import numpy as np


def calculate(list):
    calculations = {}

    try:
        arr = np.array(list).reshape(3, 3)

        mean_list = []
        var_list = []
        std_list = []
        max_list = []
        min_list = []
        sum_list = []

        temp_list = []
        for i in range(3):
            temp_list.append((arr[:, i].mean()))
        mean_list.append(temp_list)
        temp_list = []
        for i in range(3):
            temp_list.append((arr[i].mean()))
        mean_list.append(temp_list)
        mean_list.append(arr.mean())
        calculations['mean'] = mean_list

        temp_list = []
        for i in range(3):
            temp_list.append((arr[:, i].var()))
        var_list.append(temp_list)
        temp_list = []
        for i in range(3):
            temp_list.append((arr[i].var()))
        var_list.append(temp_list)
        var_list.append(arr.var())
        calculations['variance'] = var_list

        temp_list = []
        for i in range(3):
            temp_list.append((arr[:, i].std()))
        std_list.append(temp_list)
        temp_list = []
        for i in range(3):
            temp_list.append((arr[i].std()))
        std_list.append(temp_list)
        std_list.append(arr.std())
        calculations['standard deviation'] = std_list

        temp_list = []
        for i in range(3):
            temp_list.append((arr[:, i].max()))
        max_list.append(temp_list)
        temp_list = []
        for i in range(3):
            temp_list.append((arr[i].max()))
        max_list.append(temp_list)
        max_list.append(arr.max())
        calculations['max'] = max_list

        temp_list = []
        for i in range(3):
            temp_list.append((arr[:, i].min()))
        min_list.append(temp_list)
        temp_list = []
        for i in range(3):
            temp_list.append((arr[i].min()))
        min_list.append(temp_list)
        min_list.append(arr.min())
        calculations['min'] = min_list

        temp_list = []
        for i in range(3):
            temp_list.append((arr[:, i].sum()))
        sum_list.append(temp_list)
        temp_list = []
        for i in range(3):
            temp_list.append((arr[i].sum()))
        sum_list.append(temp_list)
        sum_list.append(arr.sum())
        calculations['sum'] = sum_list

    except:
        raise ValueError("List must contain nine numbers.")

    return calculations
