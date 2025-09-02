# AI Agent

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Issues](https://img.shields.io/github/issues/NA411/ai-agent.svg)](https://github.com/NA411/ai-agent/issues)

An intelligent AI agent framework designed to automate tasks, interact with various APIs, and provide autonomous decision-making capabilities.

## 🚀 Features

- **Multi-Modal AI Integration**: Support for various AI models (OpenAI, Anthropic, Google, etc.)
- **Tool Integration**: Seamless integration with external tools and APIs
- **Autonomous Decision Making**: Advanced reasoning and planning capabilities
- **Memory Management**: Persistent conversation history and context retention
- **Plugin Architecture**: Extensible plugin system for custom functionality
- **Real-time Processing**: Efficient handling of streaming responses
- **Error Recovery**: Robust error handling and retry mechanisms

## 📋 Prerequisites

- Python 3.8 or higher
- API keys for your chosen AI providers
- Git (for cloning the repository)

## 🛠️ Installation

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/NA411/ai-agent.git
   cd ai-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv ai-agent-env
   
   # On Windows
   ai-agent-env\Scripts\activate
   
   # On macOS/Linux
   source ai-agent-env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

### Development Installation

For development with additional tools:

```bash
pip install -r requirements-dev.txt
pre-commit install
```

## ⚙️ Configuration

Create a `.env` file in the root directory with the following variables:

```env
# AI Provider API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Agent Configuration
AGENT_NAME=MyAIAgent
MAX_ITERATIONS=10
TEMPERATURE=0.7
MAX_TOKENS=2048

# Database Configuration (if applicable)
DATABASE_URL=sqlite:///agent_memory.db

# Logging
LOG_LEVEL=INFO
LOG_FILE=agent.log
```

## 🚀 Quick Usage

### Basic Example

```python
from ai_agent import AIAgent

# Initialize the agent
agent = AIAgent(
    model="gpt-4",
    temperature=0.7
)

# Simple interaction
response = agent.chat("Help me analyze this data and create a summary.")
print(response)

# Task execution
result = agent.execute_task("Research the latest trends in AI and write a brief report")
print(result)
```

### Advanced Usage with Tools

```python
from ai_agent import AIAgent
from ai_agent.tools import WebSearchTool, FileManagerTool

# Initialize agent with tools
agent = AIAgent(
    model="claude-3-sonnet",
    tools=[
        WebSearchTool(),
        FileManagerTool(base_path="./workspace")
    ]
)

# Complex task with tool usage
agent.chat("Search for recent AI research papers and save summaries to a file")
```

### Command Line Interface

```bash
# Interactive mode
python -m ai_agent --interactive

# Single command execution
python -m ai_agent --task "Analyze the log file and identify any errors"

# Batch processing
python -m ai_agent --batch-file tasks.txt

# Custom model selection
python -m ai_agent --model gpt-4 --task "Your task here"
```

## 🔧 Available Tools

The agent comes with several built-in tools:

- **Web Search**: Search the internet for information
- **File Manager**: Read, write, and manage files
- **Calculator**: Perform mathematical calculations
- **Code Executor**: Run Python code safely
- **API Client**: Make HTTP requests to external APIs
- **Database Manager**: Query and manage databases
- **Email Client**: Send and receive emails
- **Calendar Integration**: Manage schedules and events

### Adding Custom Tools

```python
from ai_agent.tools import BaseTool

class CustomTool(BaseTool):
    name = "custom_tool"
    description = "Description of what this tool does"
    
    def execute(self, **kwargs):
        # Your tool logic here
        return "Tool execution result"

# Register the tool
agent.add_tool(CustomTool())
```

## 📁 Project Structure

```
ai-agent/
├── ai_agent/                 # Main package
│   ├── __init__.py
│   ├── agent.py             # Core agent logic
│   ├── models/              # AI model integrations
│   ├── tools/               # Built-in tools
│   ├── memory/              # Memory management
│   ├── planning/            # Task planning and execution
│   └── utils/               # Utility functions
├── examples/                # Usage examples
├── tests/                   # Test suite
├── docs/                    # Documentation
├── .env.example            # Environment template
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── README.md              # This file
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ai_agent

# Run specific test category
pytest tests/unit/
pytest tests/integration/
```

## 📊 Performance Monitoring

The agent includes built-in performance monitoring:

```python
# Enable monitoring
agent = AIAgent(monitoring=True)

# View statistics
stats = agent.get_performance_stats()
print(f"Total tasks: {stats.total_tasks}")
print(f"Success rate: {stats.success_rate}%")
print(f"Average response time: {stats.avg_response_time}s")
```

## 🔒 Security Considerations

- **API Key Management**: Never commit API keys to version control
- **Input Validation**: All inputs are validated and sanitized
- **Sandboxed Execution**: Code execution is performed in isolated environments
- **Access Control**: Configure tool permissions based on your needs
- **Audit Logging**: All agent actions are logged for security review

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Set up pre-commit hooks
pre-commit install

# Run linting
flake8 ai_agent/
black ai_agent/

# Run type checking
mypy ai_agent/
```

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## 🐛 Troubleshooting

### Common Issues

**Issue**: Agent not responding or hanging
- **Solution**: Check your API keys and network connection
- Verify you haven't exceeded API rate limits

**Issue**: Tools not working as expected
- **Solution**: Ensure all required dependencies are installed
- Check tool permissions and configurations

**Issue**: Memory issues with large conversations
- **Solution**: Implement conversation pruning or use a database backend
- Consider using smaller models for routine tasks

**Issue**: High API costs
- **Solution**: Implement caching for repetitive queries
- Use cheaper models for simple tasks
- Set usage limits in your configuration

### Getting Help

- Check our [FAQ](docs/FAQ.md)
- Browse [existing issues](https://github.com/NA411/ai-agent/issues)
- Join our [community discussions](https://github.com/NA411/ai-agent/discussions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: This is an active project under development. Features and APIs may change. Please check the changelog for updates.
