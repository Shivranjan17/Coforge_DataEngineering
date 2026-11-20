from crewai import Agent
from config.settings import llm

researcher = Agent(
    role="Research Researcher",
    goal="Collect accurate and relevant information about a topic",
    backstory=(
        "You are an expert researcher who gathers "
        "facts, trends, statistics, and insights from reliable sources."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)