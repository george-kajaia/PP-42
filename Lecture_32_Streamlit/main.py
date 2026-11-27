import streamlit as st

# st.set_page_config(
#     page_title="IT Step",
#     page_icon="_"
# )

# #st.title("Title STEP")
# st.header("IT STEP")
# st.subheader("Welcome to IT Step")
# st.text("text")
# st.write("write text")
# st.markdown("**Bold** and *italic*")
# st.markdown("""
# ```python
# import random
# random_number = random.randomint(1, 100)
# """)

# name = st.text_input("Enter your name")
# st.header(name)

# age = st.slider("your age", 10, 50, 25)

# color = st.selectbox("Choose color", ["red", "yellow", "green"])
# st.header(color)

# agree = st.checkbox("Agree")

# file = st.file_uploader("upload a csv file")

# clicked = st.button("Submit")

# birth_date = st.date_input("Your birthdate")
# st.header(birth_date)

# # col1, col2, col3, col4, col5 = st.columns(5)
# # with col1:
# #     st.write("Left")
# # with col2:
# #     st.write("Right")
# # with col3:
# #     st.write("Three")
# # with col4:
# #     st.write("Four")
# # with col5:
# #     st.write("Five")

# st.sidebar.title("Settings")
# option = st.sidebar.radio("View", ["Home", "About", "Contact"])
# st.header(option)

# tab1, tab2 = st.tabs(["Data", "Chart"])
# with tab1:
#     st.write("data")
# with tab2:
#     st.write("View")


# with st.expander("Details"):
#     st.write("Hidden contacts")
#     st.write("Titles")
#     # agr = st.checkbox("Agree")


import pandas as pd
# df = pd.DataFrame({
#     "x": range(10),
#     "y": range(10, 20)
# })
# st.dataframe(df)
# st.table(df)
# st.line_chart(df)
# st.bar_chart(df)

# st.metric(
#     label="Bitcoin",
#     value="10",
#     delta = "+0.15"
# )

#---------------------------------------------

# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# if st.button("Increment"):
#     st.session_state.counter += 1

# st.write("Count", st.session_state.counter)

#---------------------------------------------

# #st.title("CSV Explorer")
# uploaded_file = st.file_uploader("Upload the file", type = "csv")

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.dataframe(df)

#     #st.line_chart(df)

#---------------------------------------------

st.write("Simple AI Chat Demo")
 
# "AI brain" - just a dict mapping keywords to responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm just code, but I'm doing great!",
    "streamlit": "Streamlit makes building web apps in Python super easy.",
    "bye": "Goodbye! Have a great day.",
}
default_response = "Sorry, I don't understand. Try: hello, how are you, streamlit, bye."
 
# all chats live in one dict: {chat_name: [list of messages]}
if "chats" not in st.session_state:
    st.session_state.chats = {"Chat 1": []}
 
if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"
 
# Sidebar-------------
with st.sidebar:
    st.header("Saved Chats")
 
    if st.button("+ New Chat"):
        new_name = f"Chat {len(st.session_state.chats) + 1}"
        st.session_state.chats[new_name] = []
        st.session_state.current_chat = new_name
 
    # list existing chats as selectable buttons
    for chat_name in st.session_state.chats:
        if st.button(chat_name, key=f"select_{chat_name}"):
            st.session_state.current_chat = chat_name
 
# Main chat area ----------------
current = st.session_state.current_chat
st.subheader(current)
 
messages = st.session_state.chats[current]
 
# show past messages for the selected chat
for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
 
# chat input box
user_input = st.chat_input("Type a message...")
 
if user_input:
    # show user message
    messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
 
    # pick a response from the dict (simple keyword match)
    reply = default_response
    for key, value in responses.items():
        if key in user_input.lower():
            reply = value
            break
 
    # show assistant message
    messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
 
