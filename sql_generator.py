def generate_sql(question: str):
    q = question.lower()
    if "customer" in q:
        return "SELECT CustomerId, FirstName, LastName FROM Customer LIMIT 5;"
    elif "order" in q:
        return "SELECT OrderId, CustomerId, OrderDate FROM Orders LIMIT 5;"
    else:
        return "SELECT 'No matching table for query' AS message;"
