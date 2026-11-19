from crewai import Crew,Process
from agents.tutor_agent import python_tutor
from agents.assesment_agent import assessment_agent
from tasks.tutor_task import create_tutor_task
from tasks.assesment_task import create_assessment_task

def main():
    print("=============================")
    print("Multi Agent AI PYTHON TUTOR")
    print("Powered By CrewAI")
    print("=============================")

    topic = input(
        "Enter Python topic :"
    ).strip()

    if not topic:
        print("Please enter a valid topic.")
        return 

    #Step 1:Create the task
    tutor_task=create_tutor_task(topic)

    #Step2 : Create teaching task
    assessment_task = create_assessment_task(
        topic,
        tutor_task
    )

    #Step 3Create CREWAI crew
    

    python_crew=Crew(
        agents=[python_tutor,assessment_agent],
        tasks=[tutor_task,assessment_task],
        process=Process.sequential,
        verbose=True

        
    )
    #Step4:Execute the crew 
    try:
        result = python_crew.kickoff()
        print("\n===================Python Lesson======\n")
        print(tutor_task.output.raw)

        print("\n===================Python Assessment======\n")
        print(assessment_task.output.raw)

        print("\n===================Final CREW Output======\n")
        print(result.raw)
    except Exception as error:
        print(
            "CrewAI execution failed",
            type(error).__name__
        )

if __name__=="__main__":
    main()

