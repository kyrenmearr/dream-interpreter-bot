from llama_index import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.tools import QueryEngineTool, ToolMetadata

try:
    storage_context = StorageContext('data')