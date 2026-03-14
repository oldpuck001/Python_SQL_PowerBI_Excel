# in_out_value_check_sum_fun.py

# input output value check 对比模式一：总量、总额对比

from xlsx_tools_openxl import fill_in_xlsx_list_fun

def in_out_value_check_sum(sheet_1_name, sheet_1_in_out_mode, sql_sheet_1_df, sheet_1_in_col, sheet_1_out_col,
                           sheet_1_in_out_value, sheet_1_in_out_col, sheet_1_in_label, sheet_1_out_label,
                           sheet_2_name, sheet_2_in_out_mode, sql_sheet_2_df, sheet_2_in_col, sheet_2_out_col,
                           sheet_2_in_out_value, sheet_2_in_out_col, sheet_2_in_label, sheet_2_out_label,
                           file_path):

    fill_text = ''

    if sheet_1_in_out_mode == '双列模式':
        quantity_in_sheet_1_df = sql_sheet_1_df[sheet_1_in_col].dropna().shape[0]
        quantity_out_sheet_1_df = sql_sheet_1_df[sheet_1_out_col].dropna().shape[0]
        amount_in_sheet_1_df = round(sql_sheet_1_df[sheet_1_in_col].sum(), 2)
        amount_out_sheet_1_df = round(sql_sheet_1_df[sheet_1_out_col].sum(), 2)
    elif sheet_1_in_out_mode == '+/-单列模式':
        quantity_in_sheet_1_df = sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_value] > 0][sheet_1_in_out_value].dropna().shape[0]
        quantity_out_sheet_1_df = sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_value] < 0][sheet_1_in_out_value].dropna().shape[0]
        amount_in_sheet_1_df = round(sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_value] > 0][sheet_1_in_out_value].sum(), 2)
        amount_out_sheet_1_df = round(-sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_value] < 0][sheet_1_in_out_value].sum(), 2)
    elif sheet_1_in_out_mode == '标识列单列模式':
        quantity_in_sheet_1_df = sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_col] == sheet_1_in_label][sheet_1_in_out_value].dropna().shape[0]
        quantity_out_sheet_1_df = sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_col] == sheet_1_out_label][sheet_1_in_out_value].dropna().shape[0]
        amount_in_sheet_1_df = round(sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_col] == sheet_1_in_label][sheet_1_in_out_value].sum(), 2)
        amount_out_sheet_1_df = round(sql_sheet_1_df[sql_sheet_1_df[sheet_1_in_out_col] == sheet_1_out_label][sheet_1_in_out_value].sum(), 2)

    if sheet_2_in_out_mode == '双列模式':
        quantity_in_sheet_2_df = sql_sheet_2_df[sheet_2_in_col].dropna().shape[0]
        quantity_out_sheet_2_df = sql_sheet_2_df[sheet_2_out_col].dropna().shape[0]
        amount_in_sheet_2_df = round(sql_sheet_2_df[sheet_2_in_col].sum(), 2)
        amount_out_sheet_2_df = round(sql_sheet_2_df[sheet_2_out_col].sum(), 2)
    elif sheet_2_in_out_mode == '+/-单列模式':
        quantity_in_sheet_2_df = sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_value] > 0][sheet_2_in_out_value].dropna().shape[0]
        quantity_out_sheet_2_df = sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_value] < 0][sheet_2_in_out_value].dropna().shape[0]
        amount_in_sheet_2_df = round(sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_value] > 0][sheet_2_in_out_value].sum(), 2)
        amount_out_sheet_2_df = round(-sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_value] < 0][sheet_2_in_out_value].sum(), 2)

    elif sheet_2_in_out_mode == '标识列单列模式':
        quantity_in_sheet_2_df = sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_col] == sheet_2_in_label][sheet_2_in_out_value].dropna().shape[0]
        quantity_out_sheet_2_df = sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_col] == sheet_2_out_label][sheet_2_in_out_value].dropna().shape[0]
        amount_in_sheet_2_df = round(sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_col] == sheet_2_in_label][sheet_2_in_out_value].sum(), 2)
        amount_out_sheet_2_df = round(sql_sheet_2_df[sql_sheet_2_df[sheet_2_in_out_col] == sheet_2_out_label][sheet_2_in_out_value].sum(), 2)

    fill_in_list = [['数值合计对比', 0, 1],
                    [25, 20, 20, 20],
                    [20,                20,                          20,                        20,                           20],
                    [['sheet',      1], ['quantity_in',          1], ['amount_in',          1], ['quantity_out',          1], ['amount_out',          1]],
                    [[sheet_1_name, 2], [quantity_in_sheet_1_df, 3], [amount_in_sheet_1_df, 4], [quantity_out_sheet_1_df, 3], [amount_out_sheet_1_df, 4]],
                    [[sheet_2_name, 2], [quantity_in_sheet_2_df, 3], [amount_in_sheet_2_df, 4], [quantity_out_sheet_2_df, 3], [amount_out_sheet_2_df, 4]],
                    [['difference', 1], ['=B2-B3',               3], ['=C2-C3',             4], ['=D2-D3',                3], ['=E2-E3',              4]]
                    ]

    # 填写.xlsx文件
    fill_text += fill_in_xlsx_list_fun.fill_in_xlsx_list(file_path, fill_in_list)

    return fill_text