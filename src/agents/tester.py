from crewai import Agent
from src.config import get_llm

def get_tester():
    return Agent(
        role="QA Engineer",
        goal="Write robust unit tests and validate correctness",
        backstory="Expert in pytest and edge-case-driven testing.",
        verbose=True,
        llm=get_llm(),
    )