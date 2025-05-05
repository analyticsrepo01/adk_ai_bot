# adk_ai_bot

# Basic ADK Agent Example

## What is an ADK Agent?

The `LlmAgent` (often aliased simply as `Agent`) is a core component in ADK that acts as the "thinking" part of your application. It leverages the power of a Large Language Model (LLM) for:
- Reasoning
- Understanding natural language
- Making decisions
- Generating responses
- Interacting with tools

Unlike deterministic workflow agents that follow predefined paths, an `LlmAgent`'s behavior is non-deterministic. It uses the LLM to interpret instructions and context, deciding dynamically how to proceed, which tools to use (if any), or whether to transfer control to another agent.

## Required Agent Structure

For ADK to discover and run your agents properly (especially with `adk web`), your project must follow a specific structure:

```
parent_folder/
    agent_folder/         # This is your agent's package directory
        __init__.py       # Must import agent.py
        agent.py          # Must define root_agent
        .env              # Environment variables
```

### Essential Components:

1. **`__init__.py`**
   - Must import the agent module: `from . import agent`
   - This makes your agent discoverable by ADK

2. **`agent.py`**
   - Must define a variable named `root_agent`
   - This is the entry point that ADK uses to find your agent

3. **Command Location**
   - Always run `adk` commands from the parent directory, not from inside the agent directory
   - Example: Run `adk web` from the parent folder that contains your agent folder

This structure ensures that ADK can automatically discover and load your agent when running commands like `adk web` or `adk run`.


## Overview

This project implements an AI bot designed to shorten messages while maintaining their core meaning, leveraging the Google ADK (presumably Agent Development Kit).

## Agent Details

The core logic resides in `agent.py`, which defines the agent:

*   **Name:** adk\_short\_bot
*   **Model:** gemini-2.0-flash
*   **Description:** A bot that shortens messages while maintaining their core meaning.
*   **Instruction:** Defined in `prompt.py`, this provides the agent with instructions on how to shorten messages, including counting characters, creating concise versions, and adhering to specific formatting rules.
*   **Tools:** The agent has access to the following tools:
    *   `count_characters`: This tool, defined in `tools/character_counter.py`, counts the number of characters in a given message.

## Functionality

The bot takes an input message and performs the following steps:

1.  Counts the original characters using the `count_characters` tool.
2.  Creates a shortened version of the message, adhering to the rules defined in `prompt.py`.
3.  Counts the characters in the shortened message.
4.  Returns the original character count, the new character count, and the shortened message.

## Required Agent Structure

For ADK to discover and run your agents properly (especially with adk web), your project must follow a specific structure:




## Running the Example

To run this basic agent example, you'll use the ADK CLI tool which provides several ways to interact with your agent:

1. Navigate to the 1-basic-agent directory containing your agent folder.
2. Start the interactive web UI:
```bash
adk web
```

3. Access the web UI by opening the URL shown in your terminal (typically http://localhost:8000)

4. Select your agent from the dropdown menu in the top-left corner of the UI

5. Start chatting with your agent in the textbox at the bottom of the screen

### Troubleshooting

If your agent doesn't appear in the dropdown menu:
- Make sure you're running `adk web` from the parent directory (1-basic-agent), not from inside the agent directory
- Check that your `__init__.py` properly imports the agent module
- Verify that `agent.py` defines a variable named `root_agent`

### Alternative Run Methods

The ADK CLI tool provides several options:

- **`adk web`**: Launches an interactive web UI for testing your agent with a chat interface
- **`adk run [agent_name]`**: Runs your agent directly in the terminal
- **`adk api_server`**: Starts a FastAPI server to test API requests to your agent