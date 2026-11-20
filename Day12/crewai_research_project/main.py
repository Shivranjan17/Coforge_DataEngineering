from crewai import Crew

from agents.researcher_agent import researcher
from agents.writer_agent import writer
from agents.editor_agent import editor

from tasks.researcher_tasks import create_tasks


def main():

    topic = input("Enter a topic for research: ")

    tasks = create_tasks(topic)

    crew = Crew(
        agents=[
            researcher,
            writer,
            editor
        ],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    print("\nFinal Output:\n")
    print(result)


if __name__ == "__main__":
    main()