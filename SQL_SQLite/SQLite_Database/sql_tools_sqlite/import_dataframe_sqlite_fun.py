# import_dataframe_sqlite_fun.py

# 导入DataFrame到指定表

import sqlite3

def import_dataframe_sqlite(database_file_path, df, table_name, if_exists, index, index_label):

    try:

        conn = sqlite3.connect(database_file_path)
        curs = conn.cursor()
        df.to_sql(table_name, conn, if_exists=if_exists, index=index, index_label=index_label)
        return [True, '']
    
    except sqlite3.OperationalError as e:

        return [False, e]

    except sqlite3.IntegrityError as e:

        return [False, e]

    except sqlite3.Error as e:

        return [False, e]

    except Exception as e:

        return [False, e]
    
    finally:
        
        # 关闭数据库
        curs.close()
        conn.close()