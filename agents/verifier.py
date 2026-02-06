from llm.openai_llm import call_llm

class VerifierAgent:
    def verify(self, user_input, results):
        prompt = f"""
Verify results and return final clean answer.

User task: {user_input}
Results: {results}
"""
        return call_llm(prompt)
