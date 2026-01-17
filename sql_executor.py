# sql_engine/sql_executor.py

def execute_sql(sql: str, cursor):
    """
    Executes SQL and returns result as a list of dicts.
    """
    cursor.execute(sql)
    return cursor.fetchall()
