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
    for values in data.get_values():
        result = {}
        column_num = 0
        headers = list(data.head())
        for value in values:
            value = parse_format(value)
            result[headers[column_num].strip()] = value
            column_num += 1
        yield result


if __name__ == '__main__':
    pass
    # response = excel_to_dict(data_path, 0, 2)
    # for i in response:
    #     print(i)
