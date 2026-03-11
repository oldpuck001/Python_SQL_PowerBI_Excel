# df_col_label_fun.py

# 获取列的唯一值列表

def df_col_label(df, col_label):

    in_out_list_cleaned =[]

    in_out_np = df[col_label].unique()
    in_out_list = in_out_np.tolist()

    for item in in_out_list:

        if not isinstance(item, (int, float)):
            
            in_out_list_cleaned.append(item.replace('\t', ''))

        else:

            in_out_list_cleaned.append(item)

    info = ''

    return [True, info, in_out_list_cleaned]