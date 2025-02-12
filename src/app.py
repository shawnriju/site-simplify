
import streamlit as st
import validators
from langchain_core.messages import AIMessage, HumanMessage

def get_response(input):
    return "Default response"

def display_chat_interface(url):

    if url and validators.url(url):
    # if url is not None:
        user_input = st.chat_input("Type here...")
        if user_input is not None and user_input!="":
            response = get_response(user_input)
            st.session_state.chat_history.append(HumanMessage(content=user_input))
            st.session_state.chat_history.append(AIMessage(content=response))

        for message in st.session_state.chat_history:
            if isinstance(message,AIMessage):
                with st.chat_message("ai"):
                    st.write(message.content)
            elif isinstance(message,HumanMessage):
                with st.chat_message("user"):
                    st.write(message.content)
    else:
        st.info("Please enter a valid URL to talk to the assistant")

if "website_url" not in st.session_state:
    st.session_state.website_url = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Your SiteSimplify AI assistant here, how can I help you?")
    ]

st.set_page_config (page_title="Site Simplify",page_icon="")
st.title("Site Simplify")

with st.sidebar:
    st.header("Settings")
    url_input = st.text_input("Website URL", value=st.session_state.website_url)
    if st.button("Submit"):
        st.session_state.website_url = url_input

display_chat_interface(st.session_state.website_url)






