# get_table_info_sqlite_fun.py

# 获取表信息

import sqlite3

def get_table_info_sqlite(sql_path, table_name):

    try:

        conn = sqlite3.connect(sql_path)
        curs = conn.cursor()

        curs.execute(f"PRAGMA table_info({table_name})")
        columns = curs.fetchall()

        curs.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = curs.fetchone()[0]
        
        return [True, [columns, row_count]]
    
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