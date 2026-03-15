# execute_query_sqlite_fun.py

# 执行SQL查询并返回结果DataFrame

import sqlite3
import pandas as pd

def execute_query_sqlite(database_file_path, query):

    try:

        conn = sqlite3.connect(database_file_path)         # 建立数据库连接
        curs = conn.cursor()
        result_df = pd.read_sql(query, conn)               # 从数据库读取数据

        return [True, result_df]
    
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