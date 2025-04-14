import os
import streamlit as st
from openai import OpenAI
from google import genai
from google.genai import types
import anthropic
from apiKey import google_gemini_api_key, openai_api_key, claudai_api_key

#AI Agent for ClaudAI
claud_client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=claudai_api_key,
)

#Setting up the ChatGPT AI agent client 
client = OpenAI(api_key=openai_api_key)

def generate(title, keywords, num_words):
    finalTxt = ""
    client = genai.Client(
        api_key=google_gemini_api_key,
    )

    model = "gemini-2.5-pro-exp-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Generate a comprehensive, engaging blog post relevant to the give {title} and {keywords}. Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Generate a comprehensive, engaging blog post relevant to the give title and keywords. Make sure to incorporate these keywords in the blog post. The blog should be approximately give words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        finalTxt += chunk.text
    
    st.write(finalTxt)
def run():
    #title of the app
    st.title('✍🏼🤖 BlogPost: Your AI Blog Generating Companion')

    #create a sub header
    st.subheader('Now you can craft perfect blogs with the help of AI - BlogPost is you new Blog Generating Companion')

    #sidebar for user input
    with st.sidebar:
        st.title("Input ypur Blog Details:")
        st.subheader("Enter the details of the Blog you want the AI to generate")

        blog_title = st.text_input("Blog Title")

        keywords = st.text_area("Keywords (comma - seperated)")

        #slider for number of words
        num_words = st.slider("Number of words", min_value=100, max_value=5000, step=100)
        
        #num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)
        option = st.selectbox("Choose the model you want to use", ("Gemini Pro", "ChatGPT 4o", "Claud AI"))


        submit_button = st.button("Generate Blog")

    if submit_button:
        if option == "Gemini Pro":
            st.title("Your Blog Post (Gemini):")
            generate(blog_title, keywords, num_words)

        elif option == "ChatGPT 4o":
            response = client.responses.create(
                model="gpt-4o",
                input=f"Generate a comprehensive, engaging blog post relevant to the give {blog_title} and {keywords}. Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
            )
            st.title("Your Blog Post (ChatGPT 4o):")
            st.write(response.output_text)
        
        elif option == "Claud AI":
            message = claud_client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": f"Generate a comprehensive, engaging blog post relevant to the give {blog_title} and {keywords}. Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."}
                ]
            )
            st.title("Your Blog Post (ClaudAI):")
            st.write(message.content)
