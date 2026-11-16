from pydantic import BaseModel


class StudentRequest(BaseModel):
    student_id:int
    student_name : str
    course:str
    semester:int
    percentage:float
    primary_skill :str
    career_goal :str


class StudentAnalysis(BaseModel):
    student_name : str
    course:str
    semester:int
    percentage:float
    primary_skill :str
    career_goal :str
    academic_performance:str
    technical_assesment:str
    recommandation_learning:list[str]
    career_recommandation:list[str]
    interview_preparation:list[str]


class StudentResponse(BaseModel):
    student_id:int
    student_name:str
    prompting_techniques:str="One Shot Prompting"
    ai_analysis:StudentAnalysis
