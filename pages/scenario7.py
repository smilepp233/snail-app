import streamlit as st
import time
import uuid
import os


def generate_response():
    """
    Function to generate a short, high accuracy response with source but no review.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """
    # Short, High accuracy, With source, No review
    response = "Snails can sleep for up to 13-15 hours at a time, according to studies on snail behavior."
    for char in response:
        yield char
        time.sleep(0.001)


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():
    st.title("Snail Sleep Duration Chat - Scenario 7")
    st.caption("Short Response | High Accuracy | With Source | No Review")
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

    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Display chat history
    for i, message in enumerate(st.session_state.messages):
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

        # Create a unique but consistent key for this message
        message_id = len(st.session_state.messages) - 1

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response())
            st.info("Source: General nature observations")

            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_dir)
            video_path = os.path.join(
                project_root, "videos", "snail_sleep.mp4")

            st.video(video_path)
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
