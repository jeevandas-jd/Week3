from autogen_agentchat.ui import Console
import asyncio
from autogen_core.tools import FunctionTool
from queryHandler import (
    get_chroma_collection,
    get_query_embedding,
    search_collection,
    generate_answer
)
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
# Wrapping the search
def retrieve_documents(query: str) -> list[str]:
    collection = get_chroma_collection()
    embedding = get_query_embedding(query)
    docs = search_collection(collection, embedding)
    return docs

# Wrapping the answer generation
def answer_query_with_docs(query: str, docs: list[str]) -> str:
    return generate_answer(docs, query)

# Register tools
retrieve_docs_tool = FunctionTool(retrieve_documents, description="Retrieves relevant docs for a query.")
generate_answer_tool = FunctionTool(answer_query_with_docs, description="Answers user queries using given docs.")

client=OpenAIChatCompletionClient(
    model="gemini-1.5-flash-8b",
    api_key="AIzaSyCojNDEiD2Lhphj_9vRKbSRItedf-PUQ7o",
)
rag_agent = AssistantAgent(
    name="RAGRetrieverAgent",
    model_client=client,
    description="Agent that fetches relevant information from documents.",
    tools=[retrieve_docs_tool]
)

qa_agent = AssistantAgent(
    name="AnsweringAgent",
    model_client=client,
    description="Agent that answers the user's query using provided documents.",
    tools=[generate_answer_tool]
)

team = RoundRobinGroupChat(
    [rag_agent, qa_agent],
    max_turns=6,
)
async def main():
    stream = team.run_stream(task="What is the KlaWa app?")
    await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())