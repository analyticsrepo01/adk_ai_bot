# adk_ai_bot

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
