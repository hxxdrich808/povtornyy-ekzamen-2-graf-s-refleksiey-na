# Graph with Reflection on Code

A lightweight Python project that demonstrates how to build a **LangGraph** workflow powered by **LangChain** and the **OpenAI** API.  
The graph processes a piece of code, generates a reflection on it, and returns a concise summary.

> **Repository**: <https://git.brojs.ru/kuzakhmetovartur/povtornyy-ekzamen-2-graf-s-refleksiey-na>

---

## 📌 Overview

- **LangGraph** – orchestrates the flow of data between nodes.
- **LangChain** – provides the language model wrappers and utilities.
- **OpenAI** – the LLM that performs code analysis and reflection.

The workflow consists of three main nodes:

1. **Input Node** – receives raw code.
2. **Analysis Node** – calls the OpenAI model to analyze the code.
3. **Reflection Node** – generates a reflection and summary.

The graph is defined in `graph.py` and can be executed via the CLI or imported as a library.

---

## 🚀 Features

- **Code Analysis** – extracts key functions, classes, and comments.
- **Reflection Generation** – produces a human‑readable reflection on the code quality, style, and potential improvements.
- **Modular Design** – each node can be replaced or extended independently.
- **OpenAI Integration** – uses the `gpt-4o-mini` model by default (configurable).

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://git.brojs.ru/kuzakhmetovartur/povtornyy-ekzamen-2-graf-s-refleksiey-na.git
cd povtornyy-ekzamen-2-graf-s-refleksiey-na

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

> **Requirements**  
> - Python 3.10+  
> - `langgraph`, `langchain`, `openai` (listed in `requirements.txt`)  
> - An OpenAI API key set as the environment variable `OPENAI_API_KEY`.

---

## 📦 Usage

### Command‑Line

```bash
python main.py --file path/to/your_code.py
```

The script will:

1. Load the file content.
2. Run it through the LangGraph workflow.
3. Print the reflection and summary to the console.

### Programmatic

```python
from graph import CodeReflectionGraph

graph = CodeReflectionGraph()
result = graph.run(code="def hello():\n    print('Hello, world!')")
print(result["reflection"])
```

---

## 📁 Project Structure

```
povtornyy-ekzamen-2-graf-s-refleksiey-na/
├── graph.py          # LangGraph workflow definition
├── main.py           # CLI entry point
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── tests/
    └── test_graph.py # Unit tests
```

---

## 🤝 Contributing

Feel free to open issues or submit pull requests.  
Please follow the existing coding style and add tests for new features.

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

- **Author**: Artur Kuzakhmetov  
- **Email**: artur.kuzakhmetov@example.com

--- 
END