from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai
import os


class GeminiRAGService:
    def __init__(self):
        # FREE Google Gemini (15 req/min)
        api_key = os.getenv("GOOGLE_API_KEY")  # Free on https://makersuite.google.com/
        genai.configure(api_key=api_key)

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001", task_type="retrieval_document"
        )

        self.llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.7)

        # Initialize vector store directly
        chunks = self.load_documents()
        self.vector_store = FAISS.from_documents(chunks, self.embeddings)

        # Initialize chain directly
        prompt = ChatPromptTemplate.from_template(
            """
        You are an AI assistant representing Anthony Lesenfans, software engineer and AI developer.
        Answer professionally and concisely based only on the provided context.
        Respond in the same language as the user's question.
        If you don't know the answer, say so honestly.
        
        Chat History: {chat_history}
        Context: {context}
        Question: {input}
        """
        )

        document_chain = create_stuff_documents_chain(self.llm, prompt)
        self.qa_chain = create_retrieval_chain(
            self.vector_store.as_retriever(search_kwargs={"k": 3}), document_chain
        )

    def load_documents(self):
        data_path = Path(__file__).parent.parent.parent.parent / "data"
        loader = DirectoryLoader(
            str(data_path),
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
        )
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, length_function=len
        )
        chunks = text_splitter.split_documents(documents)
        return chunks

    async def get_response(
        self, question: str, history: list[dict] | None = None
    ) -> dict:
        # Format history from frontend
        history_text = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in (history or [])]
        )

        result = self.qa_chain.invoke({"input": question, "chat_history": history_text})

        return {
            "answer": result["answer"],
            "sources": [
                doc.metadata.get("source", "") for doc in result.get("context", [])
            ],
        }
