import os
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

class RAGService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        self.vector_store = None
        self.qa_chain = None
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
    def load_documents(self):
        """Load and process documents from data directory"""
        data_path = Path(__file__).parent.parent.parent / "data"
        
        loader = DirectoryLoader(
            str(data_path),
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents = loader.load()
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(documents)
        
        return chunks
    
    def create_vector_store(self):
        """Create FAISS vector store from documents"""
        chunks = self.load_documents()
        self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        
    def initialize_chain(self):
        """Initialize the conversational retrieval chain"""
        if not self.vector_store:
            self.create_vector_store()
            
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 3}),
            memory=self.memory,
            return_source_documents=True,
            verbose=False
        )
    
    async def get_response(self, question: str) -> dict:
        """Get response from RAG system"""
        if not self.qa_chain:
            self.initialize_chain()
        
        # Add system context to improve responses
        enhanced_question = f"""You are an AI assistant representing Anthony Lesenfans, software engineer and AI developer. 
        Answer professionally and concisely based only on the provided information.
        If you don't know the answer, say so honestly.
        
        Question: {question}"""
        
        result = self.qa_chain({"question": enhanced_question})
        
        return {
            "answer": result["answer"],
            "sources": [doc.metadata.get("source", "") for doc in result.get("source_documents", [])]
        }

# Global instance
rag_service = RAGService()
