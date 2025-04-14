import streamlit as st

#set app to wide mode
st.set_page_config(layout="wide")

st.sidebar.title("Project Navigation")
page = st.sidebar.radio("Select a Project", ("AI Blog Generator", "Review Search Tool"))

if page == "AI Blog Generator":
    import blog_generator
    blog_generator.run()
elif page == "Review Search Tool":
    import review_search
    review_search.run()
