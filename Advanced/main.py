from llama_index.llms.ollama import Ollama

model = Ollama(model="mistral", request_timeout=30.0)

result = model.complete("Hello World")

print(result)