from crewai import Task

from agents.researcher_agent import researcher
from agents.writer_agent import writer
from agents.editor_agent import editor


def create_tasks(topic):

    research_task = Task(
        description=f"""
        Research the topic: {topic}

        Collect Definition and overview, Key concepts, Benefits
        What are the Challenges and Recent trends
        Real-world applications

        Provide detailed research notes in bullet points.
        """,
        expected_output="""
        A structured research report containing:
        - Overview
        - Key findings
        - Benefits
        - Challenges
        - Trends
        - Conclusion
        """,
        agent=researcher
    )

    writing_task = Task(
        description=f"""
        Using the research findings, write a professional
        article on {topic}.

        Include Title ,Intoduction, Main Content ,Benefits,Challenges,Future Scope,Conclusion

        The content should be informative and easy to understand.
        """,
        expected_output="""
        A complete article of 500-800 words based on the research.
        """,
        agent=writer,
        context=[research_task]
    )

    editing_task = Task(
        description="""
        Review the article created by the writer.

        Check Grammar, Spelling Mistake,Clarity,Readability,Flow

        Improve sentence structure where needed.
        Make the content professional and engaging.
        """,
        expected_output="""
        A polished, publication-ready article with corrected
        grammar and improved readability.
        """,
        agent=editor,
        context=[writing_task]
    )

    return [research_task, writing_task, editing_task]