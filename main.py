from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

task = input("Enter your task: ")
plan = PlannerAgent().create_plan(task)
results = ExecutorAgent().execute(plan)
final = VerifierAgent().verify(task, results)
print(final)
