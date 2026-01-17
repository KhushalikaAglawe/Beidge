def validate_sql(sql: str) -> bool:
    sql = sql.strip().lower()
    return sql.startswith("select")
