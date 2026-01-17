def get_reasoning(question: str):
    """
    Returns a simple logical plan for demonstration.
    """
    steps = [
        f"Question received: {question}",
        "Identify main entity and relevant table(s)",
        "Determine necessary columns",
        "Apply filters or aggregation if needed"
    ]
    return {"steps": steps}
