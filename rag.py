import os
os.environ["USER_AGENT"] = "MyStudentProject/1.0"
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PDFPlumberLoader, WebBaseLoader
from langchain_classic.chains import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import BSHTMLLoader
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


load_dotenv()

#Constants
CHUNK_SIZE = 1024
EMBEDDING_MODEL = "Alibaba-NLP/gte-base-en-v1.5"
VECTORSTORE_DIR= Path(__file__).parent /"resources/vectorstore"
COLLECTION_NAME=("Research_Paper_Reader")

llm=None
vector_store=None


def initialize_components():
    global llm, vector_store

    if llm is None:
        llm=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9, max_tokens=500)

    ef=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL,
                             model_kwargs={"trust_remote_code": True}
                                 )

    if vector_store is None:
        vector_store=Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(VECTORSTORE_DIR),
        embedding_function=ef
    )



# Define where to save the database
PERSIST_DIRECTORY = "chroma_db"


def get_smart_loader(urls):
    documents = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for url in urls:
        try:
            # Case 1: Local HTML File (Jo tumne save kiya)
            if url.endswith(".html") or url.endswith(".htm"):
                print(f"🏠 Loading Local HTML: {url}")
                loader = BSHTMLLoader(url, open_encoding="utf-8") # Encoding fix added
                documents.extend(loader.load())

            # Case 2: PDF (Agar future me chahiye ho)
            elif url.endswith(".pdf"):
                print(f"📄 Loading PDF: {url}")
                loader = PDFPlumberLoader(url)
                documents.extend(loader.load())

            # Case 3: Live Website (Ye blocked sites par fail hoga)
            else:
                print(f"🌐 Loading Web Page: {url}")
                loader = WebBaseLoader(url, header_template=headers)
                documents.extend(loader.load())

        except Exception as e:
            print(f"❌ Error loading {url}: {e}")

    return documents


def process_urls(urls):
    print("Initializing... Components")

    initialize_components()

    vector_store.reset_collection()

    print("Load Data")
    data = get_smart_loader(urls)


    print("Split Text")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=150,
    )
    Splited_Piece=text_splitter.split_documents(data)

    print("Add Documents to Vector Db")
    print(f"Adding {len(Splited_Piece)} chunks to Vector DB...")
    vector_store.add_documents(documents=Splited_Piece)



def generate_answer(query):
    if not vector_store:
        raise RuntimeError("No vector database initialized")
    chain=RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever=vector_store.as_retriever())
    result=chain.invoke({"question": query},return_only_outputs=True)
    return result['answer']


if __name__=="__main__":
    urls=["https://www.aajtak.in/uttar-pradesh/story/lucknow-fsda-action-on-7-malls-lulu-hypermarket-and-kfc-closed-lcly-rpti-2402140-2025-12-03"]

    process_urls(urls)
    answer=generate_answer("How many teams did the raid?")
    print(f"Answer: {answer}")
