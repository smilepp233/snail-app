import streamlit as st
import time


def generate_response():
    """
    Function to generate the assistant's response with a typing effect.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """
    response = "Snails sleep for a bit. It's not very clear how long, though."
    for char in response.split():
        yield char + " "
        time.sleep(0.05)


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():
    st.title("Snail Sleep Duration Chat")
    st.caption("Short Response | Low Accuracy | No Source | With Review")
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
    if "thumbs_up_clicked" not in st.session_state:
        st.session_state.thumbs_up_clicked = set()

    # Initialize feedback keys if they don't exist
    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Display chat history
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Add feedback buttons for assistant messages
            if message["role"] == "assistant":
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.feedback("thumbs", key=f"feedback_{i}")
                with col2:
                    # Only show the button if it hasn't been clicked already
                    button_key = f"thumbs_up_{i}"
                    if st.button("👍 100", key=button_key):
                        if i not in st.session_state.thumbs_up_clicked:
                            st.session_state.thumbs_up_clicked.add(i)
                            st.toast("Thank you for your feedback!", icon="👍")
                            # This forces a rerun to update the UI
                            st.rerun()

    # Handle new user input
    if prompt := st.chat_input("How long do snails sleep?"):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect

        # Create a unique but consistent key for this message
        message_id = len(st.session_state.messages) - 1

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response())
            thumb_up = [":material/thumb_down:"]
            col1, col2 = st.columns([3, 1])
            with col1:
                st.feedback("thumbs", key=f"feedback_{message_id}")
            with col2:
                if st.button("👍 100", key=f"thumbs_up_{message_id}"):
                    st.session_state.thumbs_up_clicked.add(message_id)
                    st.toast("Thank you for your feedback!", icon="👍")

        assistant_message = {"role": "assistant",
                             "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
