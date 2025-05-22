import autogen
import os
from dotenv import load_dotenv
from autogen import AssistantAgent,UserProxyAgent,GroupChat,GroupChatManager

from autogen_core.tools import FunctionTool
load_dotenv()

config_list=[{
    "model":"gemini-1.5-flash",
    "api_key":os.getenv("google_api")
}]

llm_config = {
    "config_list": config_list,
    "temperature": 0,
}

# Define agents
data_fetcher = AssistantAgent(
    name="DataFetcher",
    llm_config=llm_config,
    description="Fetches CSV data and prepares it for analysis."
)

analyst = AssistantAgent(
    name="Analyst",
    llm_config=llm_config,
    description="Analyzes data and generates visualizations using Pandas and Matplotlib."
)

user = UserProxyAgent(
    name="User",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=3,
    code_execution_config={"use_docker": False},
    description="User who initiates the task and interacts with the agents."
)

# GroupChat setup
groupchat = autogen.GroupChat(
    agents=[user, data_fetcher, analyst],
    messages=[],
    max_round=5,
    speaker_selection_method="round_robin"
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Initiate the task
user.initiate_chat(manager, message="Load the sample CSV and provide a visualization of the data.")


