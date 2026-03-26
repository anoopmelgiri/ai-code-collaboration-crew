from crewai import Agent
from src.config import get_llm

def get_reviewer():
    return Agent(
        role="Code Reviewer",
        goal="Ensure code quality, correctness, and best practices",
        backstory=(
            "A meticulous reviewer who catches bugs, improves performance, "
            "and enforces clean coding standards."
        ),
        verbose=True,
        llm=get_llm(),
    )