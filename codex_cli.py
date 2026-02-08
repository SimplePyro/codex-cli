#!/usr/bin/env python3
"""
Codex CLI - A ChatGPT-like coding assistant for your terminal
"""

import os
import sys
import argparse
from openai import OpenAI

# Optional: for better terminal output
try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.syntax import Syntax
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Initialize
client = None
console = Console() if RICH_AVAILABLE else None

SYSTEM_PROMPT = """You are Codex, an AI coding assistant running in a terminal.
You help users write, debug, and explain code. Be concise but thorough.
When providing code, always specify the language for syntax highlighting.
Format your responses in markdown."""

conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]


def init_client():
    """Initialize the OpenAI client."""
    global client
    if client is None:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def print_response(text: str):
    """Print response with optional rich formatting."""
    if RICH_AVAILABLE:
        console.print(Markdown(text))
    else:
        print(text)


def chat(user_message: str) -> str:
    """Send a message and get a response."""
    init_client()
    conversation_history.append({"role": "user", "content": user_message})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo" for faster/cheaper
            messages=conversation_history,
            temperature=0.7,
            max_tokens=2000
        )
        
        assistant_message = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_message})
        return assistant_message
    
    except Exception as e:
        return f"Error: {str(e)}"


def read_file(filepath: str) -> str:
    """Read a file and return its contents."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


def interactive_mode():
    """Run the interactive chat loop."""
    print("\n🤖 Codex CLI - Your Terminal AI Assistant")
    print("=" * 45)
    print("Commands:")
    print("  /file <path>  - Load a file into context")
    print("  /clear        - Clear conversation history")
    print("  /exit         - Exit the program")
    print("=" * 45 + "\n")
    
    while True:
        try:
            user_input = input("\n\033[92mYou:\033[0m ").strip()
            
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() == "/exit":
                print("Goodbye! 👋")
                break
            
            elif user_input.lower() == "/clear":
                conversation_history.clear()
                conversation_history.append({"role": "system", "content": SYSTEM_PROMPT})
                print("🗑️  Conversation cleared.")
                continue
            
            elif user_input.lower().startswith("/file "):
                filepath = user_input[6:].strip()
                content = read_file(filepath)
                if not content.startswith("Error"):
                    user_input = f"Here's the content of `{filepath}`:\n```\n{content}\n```\nPlease analyze this file."
                else:
                    print(content)
                    continue
            
            # Get AI response
            print("\n\033[94mCodex:\033[0m", end=" ")
            response = chat(user_input)
            print()
            print_response(response)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break


def single_query(query: str):
    """Handle a single query from command line arguments."""
    response = chat(query)
    print_response(response)


def main():
    parser = argparse.ArgumentParser(description="Codex CLI - Terminal AI Assistant")
    parser.add_argument("query", nargs="*", help="Direct query (or start interactive mode if empty)")
    parser.add_argument("-f", "--file", help="Include a file in your query")
    args = parser.parse_args()
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set.")
        print("   Set it with: export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)
    
    # If a file is provided, include it
    if args.file:
        file_content = read_file(args.file)
        if file_content.startswith("Error"):
            print(file_content)
            sys.exit(1)
        query = f"File `{args.file}`:\n```\n{file_content}\n```\n\n" + " ".join(args.query)
        single_query(query)
    
    # Direct query mode
    elif args.query:
        single_query(" ".join(args.query))
    
    # Interactive mode
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
