from llama_index import VectorStoreIndex, GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper
import openai
import os

openai_api_key = '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'

WikipediaReader = download_loader('WikipediaReader')

loader = WikipediaReader()
dream_wiki = loader.load_data(pages=['Dream Interpretation'])

dream_wiki_index = GPTSimpleVectorIndex(dream_wiki)
response = dream_wiki_index.query('What is dream interpretation?')
print(response)