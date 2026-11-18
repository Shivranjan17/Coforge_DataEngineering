SYSTEMPROMPT = """
 
You are AI trainer feedback analyzer.
Analyze participants feedback objectively
Identify sentiment,strength,improvement areas,
performance level,action taken and overall summary.
return only valid JSON in the required format
 
"""
 
 
HUMANPROMPT = """
 
Trainer: {trainer_name}
Learner Name: {learner_name}
Rating: {trainer_rating}
Feedback: {trainer_feedback}
Topic Covered: {training_topic}
 
"""