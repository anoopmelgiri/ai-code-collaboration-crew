from crewai import Agent
from src.config import get_llm

def get_backend_engineer():
    return Agent(
        role="Senior Backend Engineer",
        goal="Write clean, scalable, and production-ready Python code",
        backstory=(
            "Expert backend developer with strong knowledge of APIs, "
            "system design, and performance optimization."
        ),
        allow_delegation=False,
        llm=get_llm(),
        verbose=True,
    )