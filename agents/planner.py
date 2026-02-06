import json
from llm.openai_llm import call_llm

class PlannerAgent:
    def create_plan(self, user_input: str):
        prompt = f"""
You are a Planner Agent.

Break the user task into steps.
Each step MUST contain:
- step_id
- action
- tool (github | weather | news)

Respond ONLY in JSON format like:
{
  "steps": [
    {"step_id": 1, "action": "...", "tool": "..."}
  ]
}

User task: {user_input}
"""
        response = call_llm(prompt)
        return json.loads(response)
