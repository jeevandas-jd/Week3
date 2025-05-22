
# FAQ-RAG: Retrieval-Augmented FAQ Answering System

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows you to query a document (e.g., `faq.txt`) and get intelligent answers powered by **Google Gemini** and **ChromaDB**.

## 🔍 Project Overview

**Goal:**  
Answer user questions using document context. We embed and store the document (`faq.txt`) in ChromaDB, retrieve the most relevant chunks using semantic search, and generate natural language answers using Gemini models.
```bash
---
├── FAQ.py 
├── faq.txt 
├── main.py 
├── __pycache__ 
│   └── queryHandler.cpython-313.pyc
├── queryHandler.py#
└── ragRetriver.py#
```

---

## ⚙️ How It Works

1. **Document Ingestion** (`ragRetriver.py`)
   - Reads `faq.txt`
   - Splits it into semantic chunks using `SemanticChunker` from LangChain
   - Embeds chunks using **GoogleGenerativeAIEmbeddings**
   - Stores them in a persistent **ChromaDB** vector store

2. **Query Handling** (`queryHandler.py`)
   - Embeds the user query
   - Searches for top-matching chunks in ChromaDB
   - Sends context + question to **Gemini Chat Model**
   - Returns the answer

3. **Orchestration** (`FAQ.py`)
   - Provides the command-line or callable interface
   - Calls the retriever and handler in sequence

---

## 📦 Requirements

- Python 3.10+
- Google Generative AI SDK (`langchain_google_genai`)
- LangChain
- ChromaDB
- `python-dotenv` for loading API keys

---

## 🧪 Usage

1. ✅ Set your Google API key in a `.env` file:
GOOGLE_API_KEY=your_api_key_here

2. ✅ Add your FAQs or text content to `faq.txt`.

3. ✅ Run the main FAQ handler:

```bash
python FAQ.py