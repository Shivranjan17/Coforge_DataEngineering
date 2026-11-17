import json

from openai import AzureOpenAI

from models.ai_model import (
    LearnerRequest,
    LearnerAnalysis,
    LearnerResponse
)

from prompts.ai_prompt import (
    SYSTEM_PROMPT,
    HUMAN_PROMPT
)

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)


client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)


def analyze_learner(request: LearnerRequest):

    # 1. Validate assignment counts
    if request.assignmentCompleted > request.totalAssignment:
        raise ValueError(
            "Completed assignments cannot exceed total assignments"
        )

    # 2. Calculate average score
    average_score = (
        request.pythonScore +
        request.sqlScore +
        request.fastapiScore
    ) / 3

    # 3. Determine performance level
    if average_score >= 85:
        performance_level = "Excellent"
    elif average_score >= 70:
        performance_level = "Good"
    elif average_score >= 50:
        performance_level = "Average"
    else:
        performance_level = "Needs Improvement"

    # 4. Identify strongest and weakest technologies
    scores = {
        "Python": request.pythonScore,
        "SQL": request.sqlScore,
        "FastAPI": request.fastapiScore
    }

    strongest_technology = max(
        scores,
        key=scores.get
    )

    weakest_technology = min(
        scores,
        key=scores.get
    )

    # 5. Calculate assignment completion percentage
    completion_percentage = round(
        (
            request.assignmentCompleted /
            request.totalAssignment
        ) * 100,
        2
    )

    # 6. Build human prompt
    human_prompt = HUMAN_PROMPT.format(
        learnerName=request.learnerName,
        department=request.department,
        pythonScore=request.pythonScore,
        sqlScore=request.sqlScore,
        fastapiScore=request.fastapiScore,
        attendancePercentage=request.attendancePercentage,
        assignmentCompleted=request.assignmentCompleted,
        totalAssignment=request.totalAssignment,
        completionPercentage=completion_percentage
    )

    # 7. Call Azure OpenAI
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": human_prompt
            }
        ],
        temperature=0.3
    )

    # 8. Parse the JSON response
    analysis_json = json.loads(
        response.choices[0].message.content
    )

    # 9. Validate the analysis using Pydantic
    analysis = LearnerAnalysis(
        averageScore=analysis_json["averageScore"],
        performanceLevel=analysis_json["performanceLevel"],
        strongestTechnology=analysis_json["strongestTechnology"],
        weakestTechnology=analysis_json["weakestTechnology"],
        technicalAssessment=analysis_json["technicalAssessment"],
        recommendedLearning=analysis_json["recommendedLearning"]
    )

    # 10. Return final response
    return LearnerResponse(
        learnerName=request.learnerName,
        department=request.department,
        analysis=analysis,
        finalRecommendation=analysis_json["finalRecommendation"]
    )