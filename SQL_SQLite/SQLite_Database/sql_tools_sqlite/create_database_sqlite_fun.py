# create_database_sqlite_fun.py

# 创建数据库

import sqlite3

def create_database_sqlite(database_path):

    try:

        conn = sqlite3.connect(database_path)
        curs = conn.cursor()
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