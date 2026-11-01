from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

load_dotenv()

@tool
def search(query: str)->str:
    """ tool that search over internet
    args:
        query:the query to search for
    Returns:
        the search result
    """
    print(f"searching for {query}")
    return tavily.search(query=query)
    #return "tokyo weather is sunny"

llm = ChatOllama(model="qwen2.5:0.5b",temperature=0)
tools = [search]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You have access to a search tool. Always call the search tool to look up facts such as weather instead of answering from memory.",
)

def main() -> None:
    print("Hello from langchain-course1!")
    result = agent.invoke({"messages":[HumanMessage(content="Search for the current weather in Tokyo.")]})
    print(result)

if __name__ == "__main__":
    main()