from autogen import AssistantAgent, UserProxyAgent, GroupChatManager, GroupChat
from web_browser import get_page_source
from summarizer import summarize_text
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    base_llm_config = {
        "config_list": [
            {
                "api_key": os.getenv("API_KEY"),
                "api_type": "google",
                "model": "gemini-1.5-flash"
            }
        ]
    }

    researcher = AssistantAgent(
        name="Researcher",
        llm_config=base_llm_config
    )

    summarizer = AssistantAgent(
        name="Summarizer",
        llm_config=base_llm_config
    )

    # Register tools as dict {function_name: function}
    researcher.register_function(
        {"get_page_source": get_page_source},
        "Fetches the HTML content of a webpage given its URL"
    )

    summarizer.register_function(
        {"summarize_text": summarize_text},
        "Summarizes the given text"
    )

    user = UserProxyAgent(
        name="User",
        human_input_mode="TERMINATE",
        code_execution_config={"use_docker": False}
    )

    groupchat = GroupChat(
        agents=[researcher, summarizer, user],
        messages=[],
        max_round=10
    )

    chat_manager = GroupChatManager(
        groupchat=groupchat,
        llm_config=base_llm_config
    )

    chat_manager.initiate_chat(
        user,
        message=(
            "Researcher, please use the tool 'get_page_source' to fetch the HTML content of this page: https://pypi.org/project/beautifulsoup4/.\n"
            "Then Summarizer, please use the 'summarize_text' tool to summarize the HTML content returned by Researcher."
        )
    )

if __name__ == "__main__":
    main()
