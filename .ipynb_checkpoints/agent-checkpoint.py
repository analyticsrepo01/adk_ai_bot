from google.adk.agents import LlmAgent
from google.genai import types
from pydantic import BaseModel
from google.adk.agents import Agent
from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.loop_agent import LoopAgent

from prompt import ROOT_AGENT_INSTRUCTION
from tools.character_counter import count_characters

root_agent = Agent(
    name="adk_short_bot",
    model="gemini-2.0-flash-001",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)