def plan_tasks(user_query):
    """
    Simple planning logic without LLM (stable version)
    """

    return f"""
Patient: father

User Request: {user_query}

Tasks:
1. Retrieve medical history
2. Find nephrologist availability
3. Book appointment
4. Search latest kidney treatments
5. Summarize treatment methods
"""