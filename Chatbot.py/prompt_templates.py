# prompt_templates.py

def build_prompt(user_question: str, context: str) -> str:
    """
    Builds a structured prompt for the LLM using user input and website context.

    Parameters:
    - user_question (str): The question asked by the user
    - context (str): The background/contextual info from QuantalAI's website

    Returns:
    - str: A formatted prompt string
    """
    prompt = f"""
You are an intelligent, helpful AI assistant for a fintech company called QuantalAI.

Use the information provided in the context section to answer the user's question.

---CONTEXT---
{context}
--------------

---QUESTION---
{user_question}
--------------

Provide a concise, clear, and professional answer suitable for website visitors, investors, or potential hires.
If the answer is not in the context, say "Sorry, I don't have information on that yet."
"""
    return prompt
