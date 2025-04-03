import streamlit as st
import time
import uuid
import os


def generate_response():
    """
    Function to generate a long, high accuracy response with source and with review.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """
    # Long, High accuracy, With source, With review
    response = """Land snails exhibit polyphasic sleep patterns rather than a single daily sleep period. Research has shown that garden snails (Helix aspersa) typically follow a sleep-activity pattern of 13-15 hours of sleep followed by approximately 30 hours of activity. This creates a 43-45 hour cycle rather than the common 24-hour circadian rhythm seen in many animals. During sleep phases, snails show reduced responsiveness to stimuli, decreased muscle tone, and specific brain wave patterns.

The sleep behavior of snails is characterized by complete withdrawal into their shell, with the foot relaxed and tentacles retracted. During deeper sleep phases, the foot becomes unresponsive to gentle tactile stimulation. Snails in the wild typically find protected locations for sleep, such as under leaves, in crevices, or sealed to firm surfaces with dried mucus.

During droughts or cold weather, snails can enter estivation or hibernation states respectively, which are deeper sleep-like states but distinct from regular sleep cycles. These states allow snails to survive harsh environmental conditions by dramatically reducing their metabolic rate and sealing themselves with a calcified epiphragm (a temporary door) over their shell opening. This information is based on research published in the Journal of Experimental Biology by Dr. Lisa Barr and colleagues at the University of Michigan's Department of Zoology in their 2018 study "Sleep patterns and metabolic regulation in terrestrial gastropods"."""
    for char in response:
        yield char
        time.sleep(0.001)


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():
    st.title("Snail Sleep Duration Chat - Scenario 16")
    st.caption("Long Response | High Accuracy | With Source | With Review")
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
    # Initialize thumbs_up_clicked set - THIS WAS MISSING
    if "thumbs_up_clicked" not in st.session_state:
        st.session_state.thumbs_up_clicked = set()

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
            col1, col2 = st.columns([3, 1])
            with col1:
                st.feedback("thumbs", key=f"feedback_{message_id}")
            with col2:
                if st.button("👍 100", key=f"thumbs_up_{message_id}"):
                    st.session_state.thumbs_up_clicked.add(message_id)
                    st.toast("Thank you for your feedback!", icon="👍")
                    # Add this to be consistent with the other section
                    st.rerun()

        assistant_message = {"role": "assistant",
                             "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
