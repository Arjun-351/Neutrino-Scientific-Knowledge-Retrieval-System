# ⚛️ Neutrino: Scientific Knowledge Retrieval System

![Python](https://img.shields.io/badge/Python-3.13-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.40-red) ![LangChain](https://img.shields.io/badge/LangChain-RAG-green) ![FAISS](https://img.shields.io/badge/Vector%20DB-Chroma%2FFaiss-orange)

**Neutrino** is an advanced AI-powered RAG (Retrieval-Augmented Generation) tool designed to extract, analyze, and answer questions from complex scientific documents, including ArXiv papers and University Date Sheets.

It solves the problem of "Hallucination" by grounding AI answers in actual document data, using **LangChain**, **HuggingFace Embeddings**, and **Vector Databases**.

## 🚀 Features

* **📄 Smart PDF Processing:** Uses `PDFPlumber` and `TokenTextSplitter` to accurately parse complex layouts, tables, and scientific notation.
* **🔍 Vector Search:** Efficiently indexes documents using ChromaDB/FAISS to find the exact paragraph needed to answer a query.
* **🤖 AI-Powered Answers:** Connects retrieved context to an LLM (Language Model) to generate human-like answers.
* **🌐 Web & Local Support:** Capable of processing both online PDF URLs (ArXiv) and local files.
* **🧠 Anti-Hallucination:** Strictly answers based on the provided document context.

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Framework:** LangChain
* **Embeddings:** HuggingFace (`Alibaba-NLP/gte-Qwen2-1.5B-instruct` or `all-MiniLM-L6-v2`)
* **Vector Store:** ChromaDB / FAISS
* **PDF Processing:** PDFPlumber, TikToken

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Arjun-351/Neutrino-Scientific-Knowledge-Retrieval-System.git](https://github.com/Arjun-351/Neutrino-Scientific-Knowledge-Retrieval-System.git)
    cd Neutrino-Scientific-Knowledge-Retrieval-System
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Usage

1.  **Run the Streamlit App:**
    ```bash
    streamlit run main.py
    ```

2.  **Enter a URL:**
    * Paste a link to a PDF (e.g., an ArXiv paper or University Date Sheet).
    * Click **"Process"** to build the vector database.

3.  **Ask a Question:**
    * Example: *"What is the core challenge mentioned in the abstract?"*
    * Example: *"When is the Computer Graphics exam?"*

## 📁 Project Structure
