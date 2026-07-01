from langgraph import Graph, State
import inspect
import os
from typing import Any, Dict

class MyState(State):
    """
    State for the graph. Holds the query string and the result.
    """
    query: str
    result: str = ""

def get_source_of_file(file_path: str) -> str:
    """
    Reads the source code of a file.

    Args:
        file_path: Path to the file relative to this module.

    Returns:
        The file contents or an error message if the file does not exist.
    """
    if not os.path.isfile(file_path):
        return f"File not found: {file_path}"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading {file_path}: {e}"

def get_source_of_object(obj_name: str) -> str:
    """
    Retrieves the source code of a Python object (function, class, etc.) by name.

    Args:
        obj_name: Name of the object defined in this module.

    Returns:
        The source code string or an error message if the object is not found.
    """
    obj = globals().get(obj_name)
    if obj is None:
        return f"Object not found: {obj_name}"
    try:
        return inspect.getsource(obj)
    except Exception as e:
        return f"Could not retrieve source for {obj_name}: {e}"

def reflect(state: MyState) -> MyState:
    """
    Node that processes a query asking for source code.

    Supported queries:
        - "source of <file.py>"
        - "source of <function_name>"

    The result is stored in state.result.
    """
    query = state.query.strip()
    if query.lower().startswith("source of "):
        target = query[10:].strip()
        if target.endswith(".py"):
            # Resolve file path relative to this module
            file_path = os.path.join(os.path.dirname(__file__), target)
            source = get_source_of_file(file_path)
        else:
            source = get_source_of_object(target)
        state.result = source
    else:
        state.result = (
            "Unsupported query. Please use 'source of <file.py>' "
            "or 'source of <function_name>'."
        )
    return state

# Build the LangGraph graph
graph = Graph()
graph.add_node("reflect", reflect)
graph.set_entry_point("reflect")
graph.set_finish("reflect")