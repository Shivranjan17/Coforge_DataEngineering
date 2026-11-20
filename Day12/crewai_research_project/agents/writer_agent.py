from crewai import Agent
from config.settings import llm

writer = Agent(
    role="Content Writer",
    goal="Create engaging and well-structured content",
    backstory=(
        "You are a professional content writer who converts "
        "research findings into easy-to-read articles and reports."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)