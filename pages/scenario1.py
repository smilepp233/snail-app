import streamlit as st
import time
import uuid


def generate_response():
    """
    Function to generate the assistant's response with a typing effect.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """
    response = "Snails sleep for a bit. It’s not very clear how long, though."
    for char in response:
        yield char
        time.sleep(0.005)


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():
    st.title("Snail Sleep Duration Chat")

    with st.expander("Chatbot Description"):
        st.markdown(
            """
                **Chatbot Description:**

                This intelligent tool is designed to provide detailed answers to your questions about snail sleep habits. Once you ask a question, the chatbot will respond by streaming its answer word-by-word, creating a dynamic and engaging experience. In addition, where applicable, relevant video references are displayed to offer extra visual context about the topic. Dive in and discover fascinating facts about snails in an interactive way!
                """
        )
    # Initialize chat history and feedback
    if "history" not in st.session_state:
        st.session_state.history = []
    if "likes" not in st.session_state:
        st.session_state.likes = 0
    if "dislikes" not in st.session_state:
        st.session_state.dislikes = 0

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Initialize feedback keys if they don't exist
    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle new user input
    if prompt := st.chat_input("How long do snails sleep?"):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect
        assistant_response = "".join(generate_response())
        assistant_message = {"role": "assistant",
                             "content": assistant_response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)
        with st.chat_message("assistant"):

            st.markdown(assistant_response)

            col1, col2 = st.columns([3, 1])
            with col1:
                st.feedback("thumbs", key=uuid.uuid4())
            with col2:
                st.button("👍 100")


if __name__ == "__main__":
    main()
