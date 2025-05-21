from autogen_ext.models.openai import OpenAIChatCompletionClient

llm = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key="AIzaSyCojNDEiD2Lhphj_9vRKbSRItedf-PUQ7o",
    )

def debug_code(code: str) -> str:
    """
    Use Gemini to lint and suggest fixes for the given Python code.
    """
    prompt = f"""You are a Python expert and code reviewer.

Please analyze the following Python code. Identify any bugs, inefficiencies, or bad practices and rewrite the fixed version of the code.

Only return the corrected version of the code, and nothing else.
{code}

bash
Copy
Edit
"""
    try:
        response = llm.chat(messages=[{"role": "user", "content": prompt}])
        return response.content.strip()
    except Exception as e:
        return f"# Error during debugging: {str(e)}"