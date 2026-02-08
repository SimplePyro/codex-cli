# Codex CLI

A ChatGPT-like coding assistant for your terminal. Get AI-powered help with coding, debugging, and code explanations without leaving the command line.

## Features

- **Interactive Chat Mode** - Have natural conversations with an AI assistant in your terminal
- **Code Generation** - Ask the AI to write code for you
- **Code Explanation** - Get detailed explanations of code snippets
- **File Operations** - Load files into context for analysis
- **Syntax Highlighting** - Beautiful code formatting using the Rich library
- **Single Query Mode** - Run one-off queries directly from command line

## Installation

### Option 1: Download Pre-built Executables (Recommended)

Download the latest release for your operating system from the [Releases page](https://github.com/SimplePyro/codex-cli/releases):

- **Linux**: `codex-linux-amd64`
- **macOS**: `codex-macos-amd64`
- **Windows**: `codex-windows-amd64.exe`

Make the file executable (Linux/macOS):
```bash
chmod +x codex-linux-amd64
sudo mv codex-linux-amd64 /usr/local/bin/codex
```

On Windows, rename to `codex.exe` and add to your PATH.

### Option 2: Install from Source

1. Clone the repository:
```bash
git clone https://github.com/SimplePyro/codex-cli.git
cd codex-cli
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the script executable (Linux/macOS):
```bash
chmod +x codex_cli.py
```

## Configuration

Set your OpenAI API key as an environment variable:

```bash
# Linux/macOS
export OPENAI_API_KEY='your-api-key-here'

# Windows (PowerShell)
$env:OPENAI_API_KEY='your-api-key-here'

# Windows (CMD)
set OPENAI_API_KEY=your-api-key-here
```

To make it permanent, add it to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):
```bash
echo "export OPENAI_API_KEY='your-api-key-here'" >> ~/.bashrc
source ~/.bashrc
```

Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys).

## Usage

### Interactive Mode

Start an interactive chat session:

```bash
python codex_cli.py
```

Or if using the executable:
```bash
codex
```

You'll see:
```
🤖 Codex CLI - Your Terminal AI Assistant
=============================================
Commands:
  /file <path>  - Load a file into context
  /clear        - Clear conversation history
  /exit         - Exit the program
=============================================

You: 
```

### Available Commands in Interactive Mode

- **`/file <path>`** - Load a file into the conversation context for analysis
- **`/clear`** - Clear the conversation history and start fresh
- **`/exit`** - Exit the program

### Single Query Mode

Ask a one-off question:

```bash
python codex_cli.py "How do I sort a list in Python?"
```

Or:
```bash
codex "How do I sort a list in Python?"
```

### File Mode

Analyze a specific file:

```bash
python codex_cli.py -f script.py "What does this code do?"
```

Or:
```bash
codex -f script.py "What does this code do?"
```

## Examples

### Code Generation

```bash
You: Write a Python function to calculate fibonacci numbers

Codex: Here's a Python function to calculate Fibonacci numbers:

```python
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example usage
print(fibonacci(10))  # Output: 55
```
```

### Code Explanation

```bash
You: /file my_script.py

Codex: I'll analyze this file...
```

### Debugging Help

```bash
You: I'm getting a "TypeError: 'int' object is not iterable" error. What does this mean?

Codex: This error occurs when you try to iterate over an integer...
```

## Building from Source

To create your own executable:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --onefile --name codex codex_cli.py
```

3. Find your executable in the `dist/` directory.

## Creating a Release

To trigger the automated build workflow and create a new release:

1. Tag your commit:
```bash
git tag v1.0.0
git push origin v1.0.0
```

2. The GitHub Actions workflow will automatically:
   - Build executables for Linux, macOS, and Windows
   - Create a new GitHub Release
   - Upload all executables as release assets

## Requirements

- Python 3.11 or higher
- OpenAI API key
- Dependencies: `openai>=1.0.0`, `rich>=13.0.0`

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/SimplePyro/codex-cli/issues) on GitHub.

## Acknowledgments

- Built with [OpenAI API](https://openai.com/)
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Inspired by GitHub Copilot CLI
