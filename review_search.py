import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI as LangChainOpenAI
from langchain.chains import RetrievalQA
from apiKey import openai_api_key

def create_sample_reviews():
    # Sample reviews for different places
    reviews = [
        {"place": "Pizza Place", "review": "The pizza was delicious with a crispy crust and fresh toppings. Exceptional service and cozy ambiance."},
        {"place": "Coffee Corner", "review": "A quaint coffee shop offering expertly brewed coffee and a relaxing environment."},
        {"place": "Burger Barn", "review": "Juicy burgers with a variety of toppings. The fries were a bit too salty, but overall a great experience."},
        {"place": "Sushi Spot", "review": "Fresh sushi with creative combinations and attentive staff. The presentation was exquisite."},
        {"place": "Taco Stand", "review": "Authentic tacos bursting with flavor. A must-visit for anyone craving a spicy kick."},
    ]
    # Combine place and review info into single text documents
    documents = [f"Place: {item['place']}. Review: {item['review']}" for item in reviews]
    return documents

def setup_vector_store(documents):
    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    # Create an in-memory Chroma vector store
    vector_store = Chroma.from_texts(texts=documents, embedding=embeddings, collection_name="place_reviews")
    return vector_store

def run():
    st.title("📍 LLM-Powered Review Search Tool")
    st.subheader("Query Place Reviews using Semantic Search and RAG")

    # Create sample reviews and set up the vector store
    documents = create_sample_reviews()
    vector_store = setup_vector_store(documents)
    
    # Initialize the language model for RetrievalQA using OpenAI
    llm = LangChainOpenAI(temperature=0, openai_api_key=openai_api_key)
    
    # Set up the RetrievalQA chain with the retriever from our vector store
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
    
    st.markdown("### Enter your query about place reviews:")
    query = st.text_input("Query", placeholder="e.g., Find reviews mentioning excellent service at Pizza Place")
    if st.button("Search"):
        if not query:
            st.warning("Please enter a query!")
        else:
            result = qa_chain.run(query)
            st.markdown("### Search Result:")
            st.write(result)
