from crewai import Crew

from src.agents.backend_engineer import get_backend_engineer
from src.agents.reviewer import get_reviewer
from src.agents.tester import get_tester

from src.tasks.coding_task import create_coding_task
from src.tasks.review_task import create_review_task
from src.tasks.testing_task import create_testing_task


def build_crew(feature_request: str):
    backend = get_backend_engineer()
    reviewer = get_reviewer()
    tester = get_tester()

    coding_task = create_coding_task(backend, feature_request)

    # Placeholder chaining (CrewAI will pass context)
    review_task = create_review_task(reviewer, "{coding_task_output}")
    testing_task = create_testing_task(tester, "{review_task_output}")

    return Crew(
        agents=[backend, reviewer, tester],
        tasks=[coding_task, review_task, testing_task],
        verbose=True,
        memory=False,
    )