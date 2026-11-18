from langgraph.graph import StateGraph,START,END
from graph.helpdesk_state import HelpdeskState
from agents.analysis_agent import analyze_issue
from agents.resolution_agent import resolve_issue
from tools.it_support_tools import create_support_ticket
from agents.review_agent import review_resolution


#Node 4: Escalation
def escalate_issue(state):
    ticket_result = create_support_ticket.invoke({
        "employee_id":state["employeeId"],
        "issue":state["issue"],
        "priority":state["priority"]

    })

    #Extract ticket ID from the simulated tool response 
    ticket_id = ticket_result.split("Ticket ID:  ")[1].split(".")[0]

    return{
        "ticketId":ticket_id,
        "status":"Excalated"
    }

#Node 5 : Generate final response 
def generate_response(state):
    status = state["status"]
    if status != "Excalated ":
        status="Resolution Suggested"

    response={
        "employeeId":state["employeeId"],
        "category":state["category"],
        "priority":state["priority"],
        "agentUsed":"Resolution Agent",
        "toolsCalled":state["toolsCalled"],
        "resolution":state["resolution"],
        "reviewStatus":state["reviewStatus"],
        "ticketId":state["ticketId"],
        "status":status
    }

    return {
        "status":status,
        "finalResponse":response
    }



#Conditional routing after analysis

def router_after_analysis(state):
    if state["priority"]=="Critical":
        return "excalate"
    return "resolve"


#Conditional routing after review
def route_after_review(state):
    if state["reviewStatus"]=="Approved":
        return "generate"
    return "escalate"


#Create StateGraph 
workflow =StateGraph(HelpdeskState)


#Regester nodes

workflow.add_node("analyze",analyze_issue)
workflow.add_node("resolve",resolve_issue)
workflow.add_node("review",review_resolution)
workflow.add_node("escalate",escalate_issue)
workflow.add_node("generate",generate_response)


#Starting edge
workflow.add_edge(START,"analyze")

#Routing after issue analysis
workflow.add_conditional_edges(
    "analyze",
    router_after_analysis,
    {
        "resolve":"resolve",
        "escalate":"escalate"
    }
)



#Resolution goes to quality review 
workflow.add_edge("resolve","review")

#Routing after quality review
workflow.add_conditional_edges(
    "review",
    route_after_review,
    {
        "generate":"generate",
        "escalate":"escalate"
    }
)

#Excalation goes to final response 
workflow.add_edge("escalate","generate")

#End Workflow
workflow.add_edge("generate",END)

#Compile time graph 
helpdesk_graph=workflow.compile()