import streamlit as st
import time
import uuid


def generate_response(prompt):
    """
    Function to generate a long, low accuracy response with source but no review.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """
    # Long, Low accuracy, With source, No review
    response = """Snails sleep for around 3 hours each day, according to general nature observations. They don't have a regular sleep schedule like humans do. Instead, they take short naps throughout the day and night. According to field guides, snails are mostly active during the evening and nighttime when it's cooler and more humid. During dry periods, they might go into a longer sleep-like state as noted in basic mollusc literature. They usually find a safe spot before resting, often under leaves or in their shells.

When snails sleep, they retract into their shells for protection as documented in naturalist journals. The sleep patterns can vary depending on the type of snail and environmental conditions according to amateur observations. Garden snails might sleep differently than aquatic snails as mentioned in hobby forums. Temperature and humidity play important roles in determining their activity cycles and sleep needs as noted in educational materials.

Snails in captivity might show different sleep patterns compared to those in the wild according to pet care websites. Pet snails often adjust their schedules to match when their owners feed them or interact with them. Basic guidebooks suggest that understanding snail sleep can help pet owners provide better care for these interesting creatures."""
    for char in response:
        yield char
        time.sleep(0.001)


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():
    st.title("Snail Sleep Duration Chat - Scenario 11")
    st.caption("Long Response | Low Accuracy | With Source | No Review")

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
            st.info(
                "Sources: General nature observations, Field guides, Naturalist journals, Pet care websites")

        # Add assistant response to chat history
        st.session_state.history.append(
            {"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
