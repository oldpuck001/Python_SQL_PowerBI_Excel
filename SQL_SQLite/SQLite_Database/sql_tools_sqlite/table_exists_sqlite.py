# table_exists_sqlite.py

# 检查表是否存在

import sqlite3

def table_exists(sql_path, table_name):

    try:

        conn = sqlite3.connect(sql_path)
        curs = conn.cursor()
        curs.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = curs.fetchone()
        
        if result is None:
            return [False, f'False! The tabel {table_name} was not found in the database.\n']
        else:
            return [True, f'True! The tabel {table_name} was found in the database.\n']
        
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