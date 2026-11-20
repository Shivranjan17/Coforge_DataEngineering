from crewai import Agent
from config.settings import llm

editor = Agent(
    role="Content Editor",
    goal="Review and improve content quality",
    backstory=(
        "You are an experienced editor who checks grammar, "
        "clarity, accuracy, and readability before publication."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)