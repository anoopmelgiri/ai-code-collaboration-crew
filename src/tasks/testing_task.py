from crewai import Task

def create_testing_task(agent, code):
    return Task(
        description=f"""
        Write pytest test cases for the following code:

        {code}

        Include:
        - Edge cases
        - Valid scenarios
        - Failure cases
        """,
        agent=agent,
        expected_output="pytest test cases",
    )