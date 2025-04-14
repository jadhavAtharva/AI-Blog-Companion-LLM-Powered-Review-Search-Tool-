# AI Blog Companion & LLM-Powered Review Search Tool

This repository contains a Streamlit-based web app that implements two projects:

1. **AI Blog Generator**: Uses GPT-4, Gemini, and Claude to dynamically generate context-aware blog posts.
2. **Review Search Tool**: Implements semantic search with LangChain and ChromaDB to query embedded place reviews using Retrieval-Augmented Generation (RAG).

## Project Structure

my_ai_project/ ├── app.py # Main entry point for the Streamlit app ├── blog_generator.py # Module for AI-powered blog generation ├── review_search.py # Module for semantic review search functionality └── apiKey.py # File containing your API keys


## Prerequisites

Ensure you have [Python 3.x](https://www.python.org/downloads/) installed. Then, install the required packages by running:

```bash
pip install streamlit langchain chromadb openai google-genai anthropic
```

Setup

1. Clone the Repository
Open your terminal and clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
2. Configure API Keys
Open the file apiKey.py and replace the placeholder strings with your actual API keys:
```bash
# apiKey.py
google_gemini_api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
openai_api_key = "YOUR_OPENAI_API_KEY"
claudai_api_key = "YOUR_CLAUDAI_API_KEY"
```
3. Running the Project

After completing the setup and installing the required packages, run the project with:
```bash
streamlit run app.py
```

This command will launch the application in your web browser. Use the sidebar to navigate between:

AI Blog Generator: Input blog details (title, keywords, number of words) and select a model to generate your blog.
Review Search Tool: Input your query to search through sample place reviews.
Usage

AI Blog Generator
Input: Blog title, keywords (comma-separated), and desired word count.
Select Model: Choose from Gemini Pro, ChatGPT 4o, or Claud AI.
Generate: Click the "Generate Blog" button to produce your blog post in real-time.
Review Search Tool
Input Query: Type your query regarding place reviews (for example, "Find reviews mentioning excellent service at Pizza Place").
Search: Click the "Search" button to view semantic search results.
