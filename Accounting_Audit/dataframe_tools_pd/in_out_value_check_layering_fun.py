# in_out_value_check_layering_fun.py

# input output value check 对比模式二：金额分层对比
# input output value check 对比模式三：按item分类对比
# input output value check 对比模式四：按时序排列

import pandas as pd
from xlsx_tools_openxl import fill_in_xlsx_list_fun
from xlsx_tools_openxl import fill_in_xlsx_df_fun

def in_out_value_check_layering(sheet_1_name, sheet_2_name,
                                sheet_1_in_out_mode, sheet_1_df, sheet_1_in_col, sheet_1_out_col, sheet_1_in_out_value,
                                sheet_1_in_out_col, sheet_1_in_label, sheet_1_out_label,
                                sheet_2_in_out_mode, sheet_2_df, sheet_2_in_col, sheet_2_out_col, sheet_2_in_out_value,
                                sheet_2_in_out_col, sheet_2_in_label, sheet_2_out_label,
                                sheet_1_item, sheet_2_item,
                                file_path):

    fill_text = ''

    # 获取分层值
    if sheet_1_in_out_mode == '双列模式':
        amounts_sheet_1_in_counts = sheet_1_df[sheet_1_in_col].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_1_in_counts.columns = ['value', 'count_sheet_1']
        amounts_sheet_1_in_counts_set = set(amounts_sheet_1_in_counts['value'])
        sheet_1_in_df = sheet_1_df[sheet_1_df[sheet_1_in_col].isin(amounts_sheet_1_in_counts_set)].dropna(subset=[sheet_1_in_col])
        sheet_1_in_df_col = sheet_1_in_col

        amounts_sheet_1_out_counts = sheet_1_df[sheet_1_out_col].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_1_out_counts.columns = ['value', 'count_sheet_1']
        amounts_sheet_1_out_counts_set = set(amounts_sheet_1_out_counts['value'])
        sheet_1_out_df = sheet_1_df[sheet_1_df[sheet_1_out_col].isin(amounts_sheet_1_out_counts_set)].dropna(subset=[sheet_1_out_col])
        sheet_1_out_df_col = sheet_1_out_col

    elif sheet_1_in_out_mode == '+/-单列模式':
        amounts_sheet_1_in_counts = sheet_1_df[sheet_1_df[sheet_1_in_out_value] > 0][sheet_1_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_1_in_counts.columns = ['value', 'count_sheet_1']
        amounts_sheet_1_in_counts_set = set(amounts_sheet_1_in_counts['value'])
        sheet_1_in_df = sheet_1_df[sheet_1_df[sheet_1_in_out_value].isin(amounts_sheet_1_in_counts_set)].dropna(subset=[sheet_1_in_out_value])
        sheet_1_in_df_col = sheet_1_in_out_value

        amounts_sheet_1_out_counts = sheet_1_df[sheet_1_df[sheet_1_in_out_value] < 0][sheet_1_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_1_out_counts.columns = ['value', 'count_sheet_1']
        amounts_sheet_1_out_counts['value'] = -amounts_sheet_1_out_counts['value']              # 负负得正
        amounts_sheet_1_out_counts_set = set(amounts_sheet_1_out_counts['value'])
        amounts_sheet_1_out_counts_non = pd.DataFrame()
        amounts_sheet_1_out_counts_non['value'] = -amounts_sheet_1_out_counts['value']           # 不改变负号
        amounts_sheet_1_out_counts_set_non = set(amounts_sheet_1_out_counts_non['value'])
        sheet_1_out_df = sheet_1_df[sheet_1_df[sheet_1_in_out_value].isin(amounts_sheet_1_out_counts_set_non)].dropna(subset=[sheet_1_in_out_value])
        sheet_1_out_df_col = sheet_1_in_out_value

    elif sheet_1_in_out_mode == '标识列单列模式':
        amounts_sheet_1_in_counts = sheet_1_df[sheet_1_df[sheet_1_in_out_col] == sheet_1_in_label][sheet_1_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_1_in_counts.columns = ['value', 'count_sheet_1']
        amounts_sheet_1_in_counts_set = set(amounts_sheet_1_in_counts['value'])
        sheet_1_in_df = sheet_1_df[sheet_1_df[sheet_1_in_out_col] == sheet_1_in_label].dropna(subset=[sheet_1_in_out_value])
        sheet_1_in_df_col = sheet_1_in_out_value

        amounts_sheet_1_out_counts = sheet_1_df[sheet_1_df[sheet_1_in_out_col] == sheet_1_out_label][sheet_1_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_1_out_counts.columns = ['value', 'count_sheet_1']
        amounts_sheet_1_out_counts_set = set(amounts_sheet_1_out_counts['value'])
        sheet_1_out_df = sheet_1_df[sheet_1_df[sheet_1_in_out_col] == sheet_1_out_label].dropna(subset=[sheet_1_in_out_value])
        sheet_1_out_df_col = sheet_1_in_out_value
    
    if sheet_2_in_out_mode == '双列模式':
        amounts_sheet_2_in_counts = sheet_2_df[sheet_2_in_col].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_2_in_counts.columns = ['value', 'count_sheet_2']
        amounts_sheet_2_in_counts_set = set(amounts_sheet_2_in_counts['value'])
        sheet_2_in_df = sheet_2_df[sheet_2_df[sheet_2_in_col].isin(amounts_sheet_2_in_counts_set)].dropna(subset=[sheet_2_in_col])
        sheet_2_in_df_col = sheet_2_in_col

        amounts_sheet_2_out_counts = sheet_2_df[sheet_2_out_col].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_2_out_counts.columns = ['value', 'count_sheet_2']
        amounts_sheet_2_out_counts_set = set(amounts_sheet_2_out_counts['value'])
        sheet_2_out_df = sheet_2_df[sheet_2_out_col].dropna()
        sheet_2_out_df = sheet_2_df[sheet_2_df[sheet_2_out_col].isin(amounts_sheet_2_out_counts_set)].dropna(subset=[sheet_2_out_col])
        sheet_2_out_df_col = sheet_2_out_col

    elif sheet_2_in_out_mode == '+/-单列模式':
        amounts_sheet_2_in_counts = sheet_2_df[sheet_2_df[sheet_2_in_out_value] > 0][sheet_2_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_2_in_counts.columns = ['value', 'count_sheet_2']
        amounts_sheet_2_in_counts_set = set(amounts_sheet_2_in_counts['value'])
        sheet_2_in_df = sheet_2_df[sheet_2_df[sheet_2_in_out_value].isin(amounts_sheet_2_in_counts_set)].dropna(subset=[sheet_2_in_out_value])
        sheet_2_in_df_col = sheet_2_in_out_value

        amounts_sheet_2_out_counts = sheet_2_df[sheet_2_df[sheet_2_in_out_value] < 0][sheet_2_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_2_out_counts.columns = ['value', 'count_sheet_2']
        amounts_sheet_2_out_counts['value'] = -amounts_sheet_2_out_counts['value']                  # 负负得正
        amounts_sheet_2_out_counts_set = set(amounts_sheet_2_out_counts['value'])
        amounts_sheet_2_out_counts_non = pd.DataFrame()
        amounts_sheet_2_out_counts_non['value'] = -amounts_sheet_2_out_counts['value']              # 不改变负号
        amounts_sheet_2_out_counts_set_non = set(amounts_sheet_2_out_counts_non['value'])
        sheet_2_out_df = sheet_2_df[sheet_2_df[sheet_2_in_out_value].isin(amounts_sheet_2_out_counts_set_non)].dropna(subset=[sheet_2_in_out_value])
        sheet_2_out_df_col = sheet_2_in_out_value

    elif sheet_2_in_out_mode == '标识列单列模式':
        amounts_sheet_2_in_counts = sheet_2_df[sheet_2_df[sheet_2_in_out_col] == sheet_2_in_label][sheet_2_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_2_in_counts.columns = ['value', 'count_sheet_2']
        amounts_sheet_2_in_counts_set = set(amounts_sheet_2_in_counts['value'])
        sheet_2_in_df = sheet_2_df[sheet_2_df[sheet_2_in_out_col] == sheet_2_in_label].dropna(subset=[sheet_2_in_out_value])
        sheet_2_in_df_col = sheet_2_in_out_value

        amounts_sheet_2_out_counts = sheet_2_df[sheet_2_df[sheet_2_in_out_col] == sheet_2_out_label][sheet_2_in_out_value].dropna().value_counts().sort_index().reset_index()
        amounts_sheet_2_out_counts.columns = ['value', 'count_sheet_2']
        amounts_sheet_2_out_counts_set = set(amounts_sheet_2_out_counts['value'])
        sheet_2_out_df = sheet_2_df[sheet_2_df[sheet_2_in_out_col] == sheet_2_out_label].dropna(subset=[sheet_2_in_out_value])
        sheet_2_out_df_col = sheet_2_in_out_value

    # 对比模式二：金额分层对比
    # 共同值集合
    common_amounts_in = amounts_sheet_1_in_counts_set & amounts_sheet_2_in_counts_set
    common_amounts_out = amounts_sheet_1_out_counts_set & amounts_sheet_2_out_counts_set

    # 共同金额的计数差异
    common_sheet_1_in = amounts_sheet_1_in_counts[amounts_sheet_1_in_counts['value'].isin(common_amounts_in)].set_index('value')
    common_sheet_2_in = amounts_sheet_2_in_counts[amounts_sheet_2_in_counts['value'].isin(common_amounts_in)].set_index('value')
    common_sheet_1_out = amounts_sheet_1_out_counts[amounts_sheet_1_out_counts['value'].isin(common_amounts_out)].set_index('value')
    common_sheet_2_out = amounts_sheet_2_out_counts[amounts_sheet_2_out_counts['value'].isin(common_amounts_out)].set_index('value')

    # 合并对比
    comparison_in = common_sheet_1_in.join(common_sheet_2_in, how='inner', lsuffix='_sheet_1', rsuffix='_sheet_2')
    comparison_in['difference'] = comparison_in['count_sheet_1'] - comparison_in['count_sheet_2']
    comparison_out = common_sheet_1_out.join(common_sheet_2_out, how='inner', lsuffix='_sheet_1', rsuffix='_sheet_2')
    comparison_out['difference'] = comparison_out['count_sheet_1'] - comparison_out['count_sheet_2']

    # 筛选所有计数差异不为0的项（共同金额但计数不同）
    non_zero_diff_in = comparison_in[comparison_in['difference'] != 0][['count_sheet_1', 'count_sheet_2', 'difference']]
    non_zero_diff_out = comparison_out[comparison_out['difference'] != 0][['count_sheet_1', 'count_sheet_2', 'difference']]

    # 找出只在流水或明细中出现的金额
    only_sheet_1_in = amounts_sheet_1_in_counts_set - amounts_sheet_2_in_counts_set
    only_sheet_2_in = amounts_sheet_2_in_counts_set - amounts_sheet_1_in_counts_set
    only_sheet_1_out = amounts_sheet_1_out_counts_set - amounts_sheet_2_out_counts_set
    only_sheet_2_out = amounts_sheet_2_out_counts_set - amounts_sheet_1_out_counts_set

    # input
    height_list = [25,]
    fill_in_xlsx = [['数值合计对比', 6, 1],
                    height_list,
                    [20,                 20,                20,                20               ],
                    [['input_value', 1], [sheet_1_name, 1], [sheet_2_name, 1], ['difference', 1]],
                    ]

    # 第一部分：共同金额但计数不同的情况
    if len(non_zero_diff_in) > 0:            
        for amount in non_zero_diff_in.index:
            sheet_1_count = comparison_in.loc[amount, 'count_sheet_1']
            sheet_2_count = comparison_in.loc[amount, 'count_sheet_2']
            diff_desc = sheet_1_count - sheet_2_count
            fill_in_xlsx.append([[amount, 4], [sheet_1_count, 3], [sheet_2_count, 3], [diff_desc, 3]])
            height_list.append(20)

    # 第二部分：只在 sheet 1 中出现的金额
    if len(only_sheet_1_in) > 0:            
        only_sheet_1_df = amounts_sheet_1_in_counts[amounts_sheet_1_in_counts['value'].isin(only_sheet_1_in)].set_index('value')
        for amount in only_sheet_1_df.index:
            sheet_1_count = only_sheet_1_df.loc[amount, 'count_sheet_1']
            fill_in_xlsx.append([[amount, 4], [sheet_1_count, 3], [0, 3], [sheet_1_count, 3]])
            height_list.append(20)

    # 第三部分：只在 sheet 2 中出现的金额
    if len(only_sheet_2_in) > 0:            
        only_sheet_2_df = amounts_sheet_2_in_counts[amounts_sheet_2_in_counts['value'].isin(only_sheet_2_in)].set_index('value')
        for amount in only_sheet_2_df.index:
            sheet_2_count = only_sheet_2_df.loc[amount, 'count_sheet_2']
            fill_in_xlsx.append([[amount, 4], [0, 3], [sheet_2_count, 3], [-sheet_2_count, 3]])
            height_list.append(20)

    # 填写.xlsx文件
    fill_text += fill_in_xlsx_list_fun.fill_in_xlsx_list(file_path, fill_in_xlsx)

    # 明细表
    non_zero_diff_reset_in = non_zero_diff_in.reset_index()
    # 数值分层对比_in_共同数值但计数不同_sheet_1
    non_zero_diff_reset_in = non_zero_diff_reset_in.rename(columns={'value': sheet_1_in_df_col})
    if sheet_1_in_out_mode == '双列模式':
        fill_df = pd.merge(sheet_1_in_df, non_zero_diff_reset_in[[sheet_1_in_df_col]], on=sheet_1_in_df_col, how='inner')
    elif sheet_1_in_out_mode == '+/-单列模式':
        fill_df = pd.merge(sheet_1_in_df, non_zero_diff_reset_in[[sheet_1_in_df_col]], on=sheet_1_in_df_col, how='inner')
    elif sheet_1_in_out_mode == '标识列单列模式':
        fill_df = pd.merge(sheet_1_in_df, non_zero_diff_reset_in[[sheet_1_in_df_col]], on=sheet_1_in_df_col, how='inner')
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '共同数值但计数不同sheet_in_1', fill_df)

    # 数值分层对比_in_共同数值但计数不同_sheet_2
    non_zero_diff_reset_in = non_zero_diff_reset_in.rename(columns={sheet_1_in_df_col: sheet_2_in_df_col})
    if sheet_2_in_out_mode == '双列模式':
        fill_df = pd.merge(sheet_2_in_df, non_zero_diff_reset_in[[sheet_2_in_df_col]], on=sheet_2_in_df_col, how='inner')
    elif sheet_2_in_out_mode == '+/-单列模式':
        fill_df = pd.merge(sheet_2_in_df, non_zero_diff_reset_in[[sheet_2_in_df_col]], on=sheet_2_in_df_col, how='inner')
    elif sheet_2_in_out_mode == '标识列单列模式':
        fill_df = pd.merge(sheet_2_in_df, non_zero_diff_reset_in[[sheet_2_in_df_col]], on=sheet_2_in_df_col, how='inner')
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '共同数值但计数不同sheet_in_2', fill_df)

    # 数值分层对比_in_只在 sheet 1 中出现的数值
    if sheet_1_in_out_mode == '双列模式':
        fill_df = sheet_1_in_df[sheet_1_in_df[sheet_1_in_df_col].isin(only_sheet_1_in)]
    elif sheet_1_in_out_mode == '+/-单列模式':
        fill_df = sheet_1_in_df[sheet_1_in_df[sheet_1_in_df_col].isin(only_sheet_1_in)]
    elif sheet_1_in_out_mode == '标识列单列模式':
        fill_df = sheet_1_in_df[sheet_1_in_df[sheet_1_in_df_col].isin(only_sheet_1_in)]
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '只在sheet_in_1中出现的数值', fill_df)

    # 数值分层对比_in_只在 sheet 2 中出现的数值
    if sheet_2_in_out_mode == '双列模式':
        fill_df = sheet_2_in_df[sheet_2_in_df[sheet_2_in_df_col].isin(only_sheet_2_in)]
    elif sheet_2_in_out_mode == '+/-单列模式':
        fill_df = sheet_2_in_df[sheet_2_in_df[sheet_2_in_df_col].isin(only_sheet_2_in)]
    elif sheet_2_in_out_mode == '标识列单列模式':
        fill_df = sheet_2_in_df[sheet_2_in_df[sheet_2_in_df_col].isin(only_sheet_2_in)]
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '只在sheet_in_2中出现的数值', fill_df)

    # output
    h = 6 + len(non_zero_diff_in) + len(only_sheet_1_in) + len(only_sheet_2_in) + 3
    height_list = [25,]
    fill_in_xlsx = [['数值合计对比', h, 1],
                    height_list,
                    [20,                  20,                20,                20               ],
                    [['output_value', 1], [sheet_1_name, 1], [sheet_2_name, 1], ['difference', 1]],
                    ]

    # 第一部分：共同金额但计数不同的情况
    if len(non_zero_diff_out) > 0:            
        for amount in non_zero_diff_out.index:
            sheet_1_count = comparison_out.loc[amount, 'count_sheet_1']
            sheet_2_count = comparison_out.loc[amount, 'count_sheet_2']
            diff_desc = sheet_1_count - sheet_2_count
            fill_in_xlsx.append([[amount, 4], [sheet_1_count, 3], [sheet_2_count, 3], [diff_desc, 3]])
            height_list.append(20)

    # 第二部分：只在 sheet 1 中出现的金额
    if len(only_sheet_1_out) > 0:            
        only_sheet_1_df = amounts_sheet_1_out_counts[amounts_sheet_1_out_counts['value'].isin(only_sheet_1_out)].set_index('value')
        for amount in only_sheet_1_df.index:
            sheet_1_count = only_sheet_1_df.loc[amount, 'count_sheet_1']
            fill_in_xlsx.append([[amount, 4], [sheet_1_count, 3], [0, 3], [sheet_1_count, 3]])
            height_list.append(20)

    # 第三部分：只在 sheet 2 中出现的金额
    if len(only_sheet_2_out) > 0:
        only_sheet_2_df = amounts_sheet_2_out_counts[amounts_sheet_2_out_counts['value'].isin(only_sheet_2_out)].set_index('value')
        for amount in only_sheet_2_df.index:
            sheet_2_count = only_sheet_2_df.loc[amount, 'count_sheet_2']
            fill_in_xlsx.append([[amount, 4], [0, 3], [sheet_2_count, 3], [-sheet_2_count, 3]])
            height_list.append(20)

    # 填写.xlsx文件
    fill_text += fill_in_xlsx_list_fun.fill_in_xlsx_list(file_path, fill_in_xlsx)

    non_zero_diff_reset_out = non_zero_diff_out.reset_index()

    # 数值分层对比_out_共同数值但计数不同_sheet_1
    non_zero_diff_reset_out = non_zero_diff_reset_out.rename(columns={'value': sheet_1_out_df_col})
    if sheet_1_in_out_mode == '双列模式':
        fill_df = pd.merge(sheet_1_out_df, non_zero_diff_reset_out[[sheet_1_out_df_col]], on=sheet_1_out_df_col, how='inner')
    elif sheet_1_in_out_mode == '+/-单列模式':
        fill_df = pd.merge(sheet_1_out_df, non_zero_diff_reset_out[[sheet_1_out_df_col]], on=sheet_1_out_df_col, how='inner')
    elif sheet_1_in_out_mode == '标识列单列模式':
        fill_df = pd.merge(sheet_1_out_df, non_zero_diff_reset_out[[sheet_1_out_df_col]], on=sheet_1_out_df_col, how='inner')
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '共同数值但计数不同sheet_out_1', fill_df)

    # 数值分层对比_out_共同数值但计数不同_sheet_2
    non_zero_diff_reset_out = non_zero_diff_reset_out.rename(columns={sheet_1_out_df_col: sheet_2_out_df_col})
    if sheet_2_in_out_mode == '双列模式':
        fill_df = pd.merge(sheet_2_out_df, non_zero_diff_reset_out[[sheet_2_out_df_col]], on=sheet_2_out_df_col, how='inner')
    elif sheet_2_in_out_mode == '+/-单列模式':
        fill_df = pd.merge(sheet_2_out_df, non_zero_diff_reset_out[[sheet_2_out_df_col]], on=sheet_2_out_df_col, how='inner')
    elif sheet_2_in_out_mode == '标识列单列模式':
        fill_df = pd.merge(sheet_2_out_df, non_zero_diff_reset_out[[sheet_2_out_df_col]], on=sheet_2_out_df_col, how='inner')
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '共同数值但计数不同sheet_out_2', fill_df)

    # 数值分层对比_out_只在 sheet 1 中出现的数值
    if sheet_1_in_out_mode == '双列模式':
        fill_df = sheet_1_out_df[sheet_1_out_df[sheet_1_out_df_col].isin(only_sheet_1_out)]
    elif sheet_1_in_out_mode == '+/-单列模式':
        fill_df = sheet_1_out_df[sheet_1_out_df[sheet_1_out_df_col].isin(only_sheet_1_out)]
    elif sheet_1_in_out_mode == '标识列单列模式':
        fill_df = sheet_1_out_df[sheet_1_out_df[sheet_1_out_df_col].isin(only_sheet_1_out)]
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '只在sheet_out_1中出现的数值', fill_df)

    # 数值分层对比_out_只在 sheet 2 中出现的数值
    if sheet_2_in_out_mode == '双列模式':
        fill_df = sheet_2_out_df[sheet_2_out_df[sheet_2_out_df_col].isin(only_sheet_2_out)]
    elif sheet_2_in_out_mode == '+/-单列模式':
        fill_df = sheet_2_out_df[sheet_2_out_df[sheet_2_out_df_col].isin(only_sheet_2_out)]
    elif sheet_2_in_out_mode == '标识列单列模式':
        fill_df = sheet_2_out_df[sheet_2_out_df[sheet_2_out_df_col].isin(only_sheet_2_out)]
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, '只在sheet_out_2中出现的数值', fill_df)


    # 对比模式三：按item分类对比
    fill_df = (sheet_1_in_df.assign(**{sheet_1_item: sheet_1_in_df[sheet_1_item].fillna('空白')})
                            .groupby(sheet_1_item, as_index=False)[[sheet_1_in_df_col]].sum())
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_in按item分类汇总', fill_df, 1, 1)
    fill_df = (sheet_2_in_df.assign(**{sheet_2_item: sheet_2_in_df[sheet_2_item].fillna('空白')})
                            .groupby(sheet_2_item, as_index=False)[[sheet_2_in_df_col]].sum())
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_in按item分类汇总', fill_df, 1, 4)

    fill_df = (sheet_1_out_df.assign(**{sheet_1_item: sheet_1_out_df[sheet_1_item].fillna('空白')})
                            .groupby(sheet_1_item, as_index=False)[[sheet_1_out_df_col]].sum())
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_out按item分类汇总', fill_df, 1, 1)
    fill_df = (sheet_2_out_df.assign(**{sheet_2_item: sheet_2_out_df[sheet_2_item].fillna('空白')})
                            .groupby(sheet_2_item, as_index=False)[[sheet_2_out_df_col]].sum())
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_out按item分类汇总', fill_df, 1, 4)


    # 对比模式四：按时序排列
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_in按时序排列', sheet_1_in_df, 1, 1)
    c_w = len(sheet_1_in_df.columns) + 2
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_in按时序排列', sheet_2_in_df, 1, c_w)

    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_out按时序排列', sheet_1_out_df, 1, 1)
    c_w = len(sheet_1_out_df.columns) + 2
    fill_text += fill_in_xlsx_df_fun.fill_in_xlsx_df(file_path, 'sheet_out按时序排列', sheet_2_out_df, 1, c_w)


    return fill_text