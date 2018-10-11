import pandas


def parse_format(arg):
    """
    对每一个值进行格式化处理
    :param arg:
    :return:
    """
    result = str(arg).strip()
    return result

def excel_to_dict(filename, sheet_name:int, header:int):
    """

    :param filename: 文件路径
    header: 为表头所在的行，从0算起
    :return: yield dict
    """
    data = pandas.read_excel(filename, sheet_name=sheet_name, header=header)
    for values in data.get_values():
        result = {}
        column_num = 0
        headers = list(data.head())
        for value in values:
            value = parse_format(value)
            result[headers[column_num]] = value
            column_num += 1
        yield result


if __name__ == '__main__':
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(BASE_DIR, 'data', 'test.xlsx')
    response = excel_to_dict(data_path, 0, 2)
    for i in response:
        print(i)
