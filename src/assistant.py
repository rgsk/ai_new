from dotenv import load_dotenv
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()  # take environment variables from .env.

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True
)  # type: ignore
assistant.print_response("What is the meaning of life?", markdown=True)
