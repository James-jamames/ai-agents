import os

from llama_index.core.tools import FunctionTool

def code_reader_func(file_name: str):
    path = os.path.join("C:/Users/tiago/OneDrive/Documentos/Github/ai-agents/Advanced/data", file_name)

    with open(path, 'r') as file:
        content = file.read()
        return {"file_content": content}
    
code_reader = FunctionTool.from_defaults(
    fn=code_reader_func,
    name="code_reader",
    description="This tool reads the content of a code file and return their content as result. Use this for reading code files.",
)