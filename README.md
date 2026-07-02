# LangGraph Code Review Agent with Reflection – Graph-Based Implementation

This repository contains a minimal example of a code review agent built with **LangGraph** using the **graph-based approach** exclusively. The original project mixed both graph and chain paradigms; this refactor removes all chain references and consolidates the logic into a single graph.

## Features

- **Graph-based workflow**: Three nodes – `review`, `reflect`, and `output`.
- **OpenAI LLM integration**: Uses `langchain_openai.ChatOpenAI` (requires an OpenAI API key).
- **Simple usage**: Provide a Python file `sample_code.py` with the code you want to review.

## Prerequisites

- Python 3.10+
- `pip install -r requirements.txt`
- An OpenAI API key set in the environment variable `OPENAI_API_KEY`.

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/langgraph-code-review-agent-with-reflect.git
cd langgraph-code-review-agent-with-reflect

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. **Add a code snippet**  
   Create a file named `sample_code.py` in the project root and paste the code you want to review.

2. **Run the agent**  

   ```bash
   python -m src.index
   ```

   The agent will output the review and reflection directly to the console.

## Project Structure

```
langgraph-code-review-agent-with-reflect/
├── src/
│   └── index.py          # Main graph implementation
├── sample_code.py        # Code snippet to review
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Customization

- **LLM model**: Edit `src/index.py` to change the model (e.g., `gpt-4o`).
- **Prompt tuning**: Modify the system prompts in `review_node` and `reflect_node`.
- **Graph expansion**: Add more nodes or edges to extend the workflow.

## License

MIT License

## Acknowledgements

- [LangGraph](https://github.com/run-llama/langgraph)
- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI](https://openai.com)

--- 
*This project is a simplified educational example and is not intended for production use.*