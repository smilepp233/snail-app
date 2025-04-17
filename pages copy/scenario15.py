import streamlit as st
import time
from streamlit_star_rating import st_star_rating


st.markdown(
    """
    <style>
    [data-testid="stChatMessageContent"] h2{
        font-size: 16px;
    }
   
    ### Custom CSS for the chat message container
    </style>
    """, unsafe_allow_html=True
)


def generate_response():
    """
    Function to generate the assistant's response with a typing effect.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """

    response = (
        "## Introduction to the British Museum \n"
        "The British Museum, located in Bloomsbury, London, is one of the world's largest and most important museums of human history and culture. Established in 1753, it was the first public national museum, founded on the collections of Sir Hans Sloane. The museum opened to the public in 1759 and has since grown to become a premier cultural institution [1].\n\n"
        "## Location and Architecture\n"
        "Situated on Great Russell Street, the museum is easily accessible via several London Underground stations. Its iconic Great Court, designed by Foster and Partners, is a notable architectural feature, providing a spacious environment for visitors to explore. The museum's location in Bloomsbury makes it a central hub for cultural activities in London [2].\n\n"
        "## Collection Size and Significance\n"
        "The British Museum houses over 8 million objects, documenting human culture from its beginnings to the present. This vast collection includes artifacts such as the Rosetta Stone and the Elgin Marbles. These items are not only significant for their historical value but also for their cultural and educational importance. The collection spans over two million years of human history, making it one of the most comprehensive in the world [3].\n\n"
        "## Visitor Numbers\n"
        "In recent years, the British Museum has consistently been one of the most visited attractions in the UK. In 2024, it welcomed approximately 6.5 million visitors, marking a significant increase from previous years. This high attendance is attributed to its engaging exhibitions and its status as a cultural icon [4].\n\n"
        "## Notable Recent Exhibitions\n"
        "Recent exhibitions have included \"Legion: life in the Roman army\" and \"Michelangelo: the last decades,\" which have been particularly popular among visitors [1]. These exhibitions highlight the museum's ability to curate engaging and educational displays that attract a wide audience. Additionally, the museum's temporary exhibitions often feature artifacts from around the world, showcasing its global reach and influence [4].\n\n"
        "References:\n"
        "1. British Museum. (2024). Home. Retrieved from https://www.britishmuseum.org\n"
        "2. Williams, R. T. (2023). Preserving history through innovation: The British Museum's Architecture. Journal of Museum Architecture, 45(2), 134–150. Retrieved from https://www.jmth.org/articles/digital-britishmuseum\n"
        "3. UK Heritage Council. (2024). National museum performance report. Retrieved from https://www.ukheritage.org\n"
        "4. British Museum. (2024). Explore the museum virtually. Retrieved from https://www.britishmuseum.org/virtual-tour\n\n"

    )
    for char in response:
        yield char
        if char in ['.', '!', '?', '\n']:
            # Slightly longer pause after sentences and line breaks
            time.sleep(0.01)
        else:
            time.sleep(0.002)  # Faster typing for regular characters


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():

    st.markdown("""
        <style>
        .title {
            font-size: 20px;  /* Bigger title */
            color: #2E8B57;
            text-align: left;
            font-weight: bold;
        }
        .blue-bg {
            background-color: #0000FF;  /* Blue background */
            color: white;  /* White text for contrast */
            padding: 2px 5px;  /* Small padding for better appearance */
            border-radius: 3px;  /* Slight rounding */
        }
      
        </style>
        """,
                unsafe_allow_html=True
                )
    st.markdown(
        """
            <div class="title">
                Instruction: Please copy the following question to receive background information: <span class="blue-bg">"Discuss the history of the British Museum, including its location, collection size, visitor numbers, and notable recent exhibitions."</span>
            </div>
            """,
        unsafe_allow_html=True
    )
    st.caption(
        "Scenario 15 | 0 ALL | 1 High Source | 1 High Self Rating | 0 Low Public Rating")

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

   # Initialize rating default value (but don't store in session_state yet)
    fixed_rating = 1.5
    rating_count = "120.3K"

    if "rating" not in st.session_state:
        st.session_state.rating = fixed_rating

    with st.container(border=True):
        st.markdown(
            """
            <h4>"Z" AI Background</h4>
            """,
            unsafe_allow_html=True
        )
        col1, col2 = st.columns([1, 3])
        with col1:
            st_star_rating(
                label="",
                maxValue=5,
                size=20,
                defaultValue=fixed_rating,
                key="rating",
                customCSS="div { margin-bottom: 0px; }",
                read_only=True
            )

        with col2:
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; height: 100%;">
                    <span style="font-size: 24px; font-weight: bold;">
                        {fixed_rating}/5.0 (rated by {rating_count})
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
            """
            <div style="margin-top: 10px; margin-bottom: 30px;">
                "Z" AI is an advanced artificial intelligence-powered search engine and chatbot tool that utilizes large language models (LLMs) to provide detailed and accurate information in response to user queries.
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

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

    # Handle new user input
    if prompt := st.chat_input("Discuss the history of the British Museum, including its location, collection size, visitor numbers, and notable recent exhibitions."):
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
            st.markdown(
                """
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 Confidence Level: 8/10
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        "Z" AI: I would rate the confidence level of my output as an 8 out of 10.
                    </span>
                </div>
                <div style="margin-top: 20px; text-align: center;">
                    <a href="https://hkbu.questionpro.com/t/AVqX2Z5xKf" target="_blank" style="text-decoration: none;">
                        <button style="
                            background-color: #4CAF50; 
                            color: white; 
                            padding: 10px 20px; 
                            font-size: 16px; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer;">
                            Start Survey S15
                        </button>
                    </a>
                </div>
                
                """,
                unsafe_allow_html=True
            )
        assistant_message = {"role": "assistant",
                             "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
