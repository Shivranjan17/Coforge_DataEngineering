from crewai import Task
from agents.tutor_agent import python_tutor

def create_tutor_task(topic):
    tutor_task=Task(
        description=(
            f"Teach the Python topic :{topic}."
            "The learner is a complte fresher "
            "Explain the concept in simple English ."
            "Provide one real-world example"
            "Write two beginner-friendly Python programs"
            "Show the expected output of each program"
            "Create three practice assignments"
            "Do not execute any code"
        ),

        expected_output=(
            "A structured Python lession containing:"
            "1. Topic introduction"
            "2.Detailed explaination"
            "3. Real world example"
            "4. Two Python programs"
            "5.Expected outputs"
            "6. Three practice assignments "
        ),
        agent=python_tutor
    )

    return tutor_task