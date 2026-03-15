# command_sqlite_fun.py

# 执行SQL指令

import sqlite3

def command_sqlite(database_path, sql_type, sql_command):

    conn = sqlite3.connect(database_path)
    curs = conn.cursor()

    try:
        sql_clean = sql_command.strip()
        sql_type = sql_clean.lower().split()[0]
        curs.execute(sql_clean)

        # 查询语句
        if sql_type == 'select':
            rows = curs.fetchall()
            columns = [desc[0] for desc in curs.description]
            if rows:
                result_lines = []
                result_lines.append(' | '.join(columns))
                result_lines.append('-' * 178)
                for row in rows:
                    result_lines.append(' | '.join(str(v) for v in row))
                result_text = (f'\n指令：\n{sql_command}\n'
                                f'查询结果（{len(rows)} 行）：\n' + '\n'.join(result_lines) + '\n')
            else:
                result_text = (f'\n指令：\n{sql_command}\n''查询成功，但结果为空。\n')

        # 非查询语句
        else:
            conn.commit()
            result_text = (f'\n指令：\n{sql_command}\n执行成功！影响行数：{curs.rowcount}\n')

        return [True, result_text]

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