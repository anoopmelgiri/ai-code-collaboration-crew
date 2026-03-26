from crewai import Task

def create_coding_task(agent, feature_request):
    return Task(
        description=f"""
        Build a Python function for the following requirement:

        {feature_request}

        Requirements:
        - Clean, readable code
        - Type hints
        - Error handling
        """,
        agent=agent,
        expected_output="Production-ready Python code",
    )