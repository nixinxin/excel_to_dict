A small package to convert records in excel into dict.

######使用方法：
    from excel_to_dict.excel_to_dict import excel_to_dict
    response = excel_to_dict("test.xlsx", 0, 2)
    for i in response:
        print(i)
