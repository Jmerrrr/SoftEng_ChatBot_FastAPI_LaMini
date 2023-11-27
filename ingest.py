from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
# Working Vector Database

# Load and process the text
loader = TextLoader('PATH_OF_TEXT_FILE_HERE')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

persist_directory = 'db'

embedding = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=persist_directory)

vectordb.persist()
vectordb = None