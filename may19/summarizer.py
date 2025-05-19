import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("API_KEY")
print(f"API_KEY: {api_key}")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")
def summarize_text(text):

    try:
        response= model.generate_content(
            f"detailed Summarization the following text:\n\n{text}\n\nSummary:"
            
        )
        summary = response.text
        return summary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    