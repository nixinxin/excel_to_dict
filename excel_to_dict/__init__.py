import pandas

name = 'excel_to_dict'


def parse_format(arg):
    """
    对每一个值进行格式化处理
    :param arg:
    :return:
    """
    if isinstance(arg, str):
        arg = str(arg).strip()
    elif isinstance(arg, float) and str(arg) != 'nan':
        arg = int(arg)
    elif isinstance(arg, int):
        pass
    else:
        arg = None
    return arg


def excel_to_dict(filename, sheet_name: int, header: int):
    """

    :param filename: 文件路径
    :param sheet_name: 0, 1, 2, 3
    :param header: 为表头所在的行，从0算起
    :return: yield dict
    """
    data = pandas.read_excel(filename, sheet_name=sheet_name, header=header)
    data = data.to_dict()
    for item in range(0, len(list(data.values())[0])):
        temp_dict = {}
        for key in data.keys():
            temp_dict[key] = data[key][item]
        yield temp_dict


if __name__ == '__main__':
    pass
    # response = excel_to_dict(data_path, 0, 2)
    # for i in response:
    #     print(i)
