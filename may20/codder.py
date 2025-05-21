from autogen_ext.models.openai import OpenAIChatCompletionClient

llm = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key="AIzaSyCojNDEiD2Lhphj_9vRKbSRItedf-PUQ7o",
    )

def generate_code(task: str) -> str:
    """
    Use Gemini to generate Python code based on a natural language task.
    """
    prompt = f"""Write clean, working Python code for the following task:

    {task}

    Only return code. Do not explain anything. Make sure the code is executable.
    """
    try:
        response = llm.chat(messages=[{"role": "user", "content": prompt}])
        return response.content.strip()
    except Exception as e:
        return f"# Error during code generation: {str(e)}"
