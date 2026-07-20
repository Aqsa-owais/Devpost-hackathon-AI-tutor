import streamlit as st

from tutor import run_cs_tutor_agent

# -----------------------
# Page Config
# -----------------------

st.set_page_config(
    page_title="AI Computer Science Tutor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Computer Science Tutor")

st.write("Ask any Computer Science question.")

# -----------------------
# Read textbook
# -----------------------

with open("textbook.txt","r",encoding="utf-8") as f:
    textbook_context = f.read()

# -----------------------
# Sidebar
# -----------------------

st.sidebar.title("Student Profile")

weaknesses = st.sidebar.multiselect(

    "Select Weak Areas",

    [
        "Programming",
        "Loops",
        "Functions",
        "Variables",
        "Arrays",
        "Database",
        "Networking",
        "OOP"
    ]

)

# -----------------------
# User Question
# -----------------------

question = st.text_area(

    "Enter your question",

    height=150

)

# -----------------------
# Button
# -----------------------

if st.button("Ask Tutor"):

    if question == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            answer = run_cs_tutor_agent(

                question,

                weaknesses,

                textbook_context

            )

        st.success("Answer")

        st.write(answer)