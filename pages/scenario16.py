import streamlit as st
import time
import uuid


def generate_response(prompt):
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

    # Initialize chat history and feedback
    if "history" not in st.session_state:
        st.session_state.history = []
    if "likes" not in st.session_state:
        st.session_state.likes = 0
    if "dislikes" not in st.session_state:
        st.session_state.dislikes = 0

    # Initialize feedback keys if they don't exist
    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Handle new user input
    if prompt := st.chat_input("How long do snails sleep?"):
        # Add user message to chat history
        st.session_state.history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect
        with st.chat_message("assistant"):
            response = st.write_stream(generate_response(prompt))

            col1, col2 = st.columns([3, 1])
            with col1:
                st.feedback(
                    "thumbs",
                    key=uuid.uuid4(),
                    on_change=save_feedback,
                    args=[len(st.session_state.history) - 1],
                )
            with col2:
                st.button(f"👍 {st.session_state.likes}")

            # Show source information
            st.info("Source: Journal of Experimental Biology, 2018, \"Sleep patterns and metabolic regulation in terrestrial gastropods\" by Dr. Lisa Barr et al., University of Michigan's Department of Zoology")

            # Show review information
            st.success(
                "This information has been reviewed by malacologists and sleep researchers specializing in invertebrate rest patterns.")

        # Add assistant response to chat history
        st.session_state.history.append(
            {"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
