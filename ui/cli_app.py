# ui/cli_app.py
from reasoning.reasoning_engine import get_reasoning
from sql_engine.sql_generator import generate_sql
from sql_engine.sql_validator import validate_sql
from sql_engine.sql_executor import execute_sql
from database.mysql_connector import get_connection

def main():
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        print("\n" + "="*60)
        print(f"Question: {question}\n")

        logical_plan = get_reasoning(question)
        sql = generate_sql(question)

        if not validate_sql(sql):
            print("Generated SQL is invalid")
            continue

        conn, cursor = get_connection()
        result = execute_sql(sql, cursor)
        cursor.close()
        conn.close()

        print("Reasoning / Logical Plan:")
        for step in logical_plan.get("steps", []):
            print(" -", step)

        print("\nGenerated SQL:")
        print(sql)

        print("\nQuery Result:")
        print(result)

        print("\nAnswer:")
        print("Answer shown above")
        print("="*60)

if __name__ == "__main__":
    main()
