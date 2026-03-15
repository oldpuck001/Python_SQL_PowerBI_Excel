# get_all_tables_sqlite_fun.py

# 获取所有表名

import sqlite3

def get_all_tables_sqlite(database_file_path):

    try:

        conn = sqlite3.connect(database_file_path)
        curs = conn.cursor()
        curs.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = curs.fetchall()
        return [True, [table[0] for table in tables]]
    
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