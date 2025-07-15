from code_reader import code_reader
from prompts import context, code_parser_template

from dotenv import load_dotenv

from llama_parse import LlamaParse
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.llms.ollama import Ollama

load_dotenv()

model = Ollama(model="mistral", request_timeout=240.0)

parser = LlamaParse(result_type="markdown")

file_extractor = {".pdf": parser}

documents = SimpleDirectoryReader("./Advanced/data", file_extractor=file_extractor).load_data()

embed_model = resolve_embed_model("local:BAAI/bge-m3")

vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

query_engine = vector_index.as_query_engine(llm=model)

tools = [
    code_reader,
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="api_documentation",
            description="This give documentation about code for an API. Use this for reading docs for the API.",
        )
    )
]

code_llm = Ollama(model="codellama")
agent = ReActAgent.from_tools(tools, llm=code_llm, context=context, verbose=True)

#result = agent.query("Send a post request to make a new item using the api in python.")
result = agent.query("Read the content of the file test.py and give me the exact code in it.")

print("Result: ", result)