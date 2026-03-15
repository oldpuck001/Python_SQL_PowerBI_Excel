# get_table_columns_sqlite.py

# 获取所有列名

import sqlite3

def get_table_columns(database_file_path, table_name):

    try:

        conn = sqlite3.connect(database_file_path)
        curs = conn.cursor()
        curs.execute(f'PRAGMA table_info({table_name})')
        columns = curs.fetchall()
        
        return [True, [column[1] for column in columns]]                # 提取列名（PRAGMA返回的第二个元素是列名）
    
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