from typing import TypedDict
from langgraph.graph import StateGraph,START,END

from services.llm_service import analyze_feedback
from models.training_model import (TrainerRequest,TrainerResponse)

class TrainingFeedbackState(TypedDict):

    #Creating the states

    trainer_name:str
    learner_name:str
    training_topic: str
    trainer_rating: int
    trainer_feedback:str


    sentiments:str
    performance_level:str
    strengths:list[str]
    improvement_areas:list[str]
    overall_summary:str
    action_taken:str

def analyze_training_feedback_node(state:TrainingFeedbackState):
    request= TrainerRequest(
        trainer_name=state["trainer_name"],
        learner_name=state["learner_name"],
        trainer_rating=state["trainer_rating"],
        trainer_feedback=state["trainer_feedback"],
        training_topic=state["training_topic"]
    )

    #calling the langchain
    result = analyze_feedback(request)
    return{
        "sentiments":result.sentiments,
        "performance_level":result.performance_level,
        "strengths":result.strengths,
        "improvement_areas":result.improvement_areas,
        "overall_summary":result.overall_summary,
        "action_taken":result.action_taken
    }  

def check_trainer_performance_level(
        state: TrainingFeedbackState
):
    if state["performance_level"] == "Needs Improvement":
        return "Change Trainer"
 
    return "Continue Trainer"
 
 
def change_trainer_node(
        state: TrainingFeedbackState
):
    return {
        "action_taken": "Change Trainer"
    }
 
 
def Continue_trainer_node(
        state: TrainingFeedbackState
):
    return {
        "action_taken": "Continue Trainer"
    }
 



# Step6 :Create workflow

workflow = StateGraph(TrainingFeedbackState)

    #add Nodes
workflow.add_node("analyze_training_feedback_node",analyze_training_feedback_node)
workflow.add_node("Change_trainer_node",change_trainer_node)
workflow.add_node("Continue_trainer_node",Continue_trainer_node)

    #Step 8:Starting Edge
workflow.add_edge(START,"analyze_training_feedback_node"),
workflow.add_conditional_edges("analyze_training_feedback_node",check_trainer_performance_level,
                                {
                                    "Change_trainer_node",change_trainer_node,
                                    "Change_trainer_node",Continue_trainer_node
                                })

workflow.add_edge("Change_trainer_node",END)
workflow.add_edge("Continue_trainer_node",END)

workflow_graph=workflow.compile()

