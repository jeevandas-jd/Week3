from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
from autogen_agentchat.ui import Console
def add(a:int,b:int)->int:
    print("adding fucntion called here")
    return a + b


def output(result:int)->str:
    return f"The result is: {result}"
add_func=FunctionTool(add, description="Adds two numbers together.")
output_func=FunctionTool(output, description="Outputs the result of the addition.")
config_list=[
    {
        "model":"gemini-1.5-flash-8b",
        "api_key":"AIzaSyCojNDEiD2Lhphj_9vRKbSRItedf-PUQ7o",

    }
]


llm_config = {
    "config_list": config_list,
    "temperature": 0,
}

client=OpenAIChatCompletionClient(
    model="gemini-1.5-flash-8b",
    api_key="AIzaSyCojNDEiD2Lhphj_9vRKbSRItedf-PUQ7o",
)

adding_agent= AssistantAgent(
    name="AddingAgent",
    model_client=client,
    description="Adds two numbers together.",
    tools=[add_func]
)

output_agent= AssistantAgent(
    name="OutputAgent",
    model_client=client,
    description="Outputs the result of the addition.",
    tools=[output_func]
)

teams=RoundRobinGroupChat(
    [adding_agent,output_agent],
    max_turns=5,
)


# ... all your agent setup code ...
async def main():
    stream = teams.run_stream(task="Add 10 and 222")  # DO NOT await here
    await Console(stream)  # Console expects an async generator

if __name__ == "__main__":
    asyncio.run(main())
